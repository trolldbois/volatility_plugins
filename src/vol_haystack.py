"""
Plugin to find records using the haystack library.

python vol.py --plugins=contrib/plugins -f ...

"""

import sys
import os

import haystack
from haystack import target
from haystack.mappings import base
from haystack.mappings import vol as hvol
from haystack import api
from haystack.search import searcher
from haystack import constraints


import volatility.plugins.taskmods as taskmods
from volatility.renderers import TreeGrid

class Haystack(taskmods.DllList):
    """
    Search for a record in all the memory space.
    """

    def _do_haystack(self, task):
        pid = task.UniqueProcessId
        my_mappings = []
        # get the mappings
        address_space = task.get_process_address_space()
        for vad in task.VadRoot.traverse():
            # print type(vad)
            if vad is None:
                continue
            offset = vad.obj_offset
            start = vad.Start
            end = vad.End
            tag = vad.Tag
            flags = str(vad.u.VadFlags)
            perms = hvol.PERMS_PROTECTION[vad.u.VadFlags.Protection.v() & 7]
            pathname = ''
            if vad.u.VadFlags.PrivateMemory == 1 or not vad.ControlArea:
                pathname = ''
            elif vad.FileObject:
                pathname = str(vad.FileObject.FileName or '')

            pmap = hvol.VolatilityProcessMappingA(
                address_space,
                start,
                end,
                permissions=perms,
                pathname=pathname)

            my_mappings.append(pmap)
        # now build the memory_handler

        # get the platform
        profile = None
        my_target = None
        if 'WinXP' in self.config.PROFILE:
            profile = 'winxp'
        elif 'Win7' in self.config.PROFILE:
            profile = 'win7'
        else:
            raise ValueError('Profile %s not supported' % self.config.PROFILE)

        if 'x86' in self.config.PROFILE:
            my_target = target.TargetPlatform.make_target_win_32(profile)
        elif 'x64' in self.config.PROFILE:
            my_target = target.TargetPlatform.make_target_win_64(profile)

        # create a memory handler
        memory_handler = base.MemoryHandler(my_mappings, my_target, self.config.LOCATION)

        for res in self.make_results(pid, memory_handler):
            yield res

    def make_results(self, pid, memory_handler):
        raise NotImplementedError('Implement me')


class HaystackSearch(Haystack):
    """
    Search for a record in all the memory space.
    """
    def __init__(self, config, *args, **kwargs):
        self.config = config
        taskmods.DllList.__init__(self, config, *args, **kwargs)
        config.add_option('RECORD_NAME', short_option='r', default= None,
                          help='Search for this record type',
                          action='store', type='str')
        config.add_option('CONSTRAINT_FILE', short_option='c', default= None,
                          help='Using this constraint file',
                          action='store', type='str')

    def _init_haystack(self):
        # get the structure name and type
        self.modulename, sep, self.classname = self.config.RECORD_NAME.rpartition('.')
        # parse the constraint file
        if self.config.CONSTRAINT_FILE:
            handler = constraints.ConstraintsConfigHandler()
            self.my_constraints = handler.read(self.config.CONSTRAINT_FILE)
        else:
            self.my_constraints = None
        return

    def make_results(self, pid, memory_handler):
        # import the record class in the haystack model
        # we need pwd in path
        sys.path.append(os.getcwd())
        module = memory_handler.get_model().import_module(self.modulename)
        struct_type = getattr(module, self.classname)
        for res in self.make_search_results(memory_handler, struct_type, self.my_constraints):
            yield pid, res

    def make_search_results(self, memory_handler, struct_type, my_constraints):
        # do the search
        # do not use the haystack HEAP parsing capabilities
        ## PROD - use API
        results = api.search_record(memory_handler, struct_type, my_constraints, extended_search=True)
        # output handling
        ret = api.output_to_python(memory_handler, results)
        for instance, addr in ret:
            yield addr

    #def generator(self, data):
    #    self._init_haystack()
    #    for task in data:
    #        yield self._search(task)

    def calculate(self):
        self._init_haystack()
        tasks = taskmods.DllList.calculate(self)
        results = []
        for task in tasks:
            results.extend([(pid, addr) for pid, addr in self._do_haystack(task)])
        return results

    def render_text(self, outfd, data):
        prevpid= None
        for pid, addr in data:
            if pid != prevpid:
                outfd.write("*" * 72 + "\n")
                outfd.write("Pid: {0:6}\n".format(pid))
                prevpid = pid
            outfd.write('Record %s at 0x%x\n' % (self.classname, addr))

#    def unified_output(self, data):
#        # blank header in case there is no shimcache data
#        return TreeGrid([("PID", int), ("Address", int)
#                       ], self.generator(data))


class HaystackHeap(HaystackSearch):
    """
    Search for a record in an optimised way, suitable for windows HEAP search.
    """
    def make_search_results(self, memory_handler, struct_type, my_constraints):
        ## DEBUG - use optimised search space for HEAP
        my_searcher = searcher.AnyOffsetRecordSearcher(memory_handler, my_constraints)
        for mapping in memory_handler.get_mappings():
            res = my_searcher._search_in(mapping, struct_type, nb=1, align=0x1000)
            if res:
                instance, addr = api.output_to_python(memory_handler, res)[0]
                yield addr
            ## use direct load
            # results = api.load_record(memory_handler, struct_type, 0x150000, load_constraints=None)

class HaystackAllocated(HaystackSearch):
    """
    Search for a record only in allocated memory chunks.
    """
    def make_search_results(self, memory_handler, struct_type, my_constraints):
        # do the search
        # USE the haystack HEAP parsing capabilities
        ## PROD - use API
        results = api.search_record(memory_handler, struct_type, my_constraints, extended_search=False)
        # output handling
        ret = api.output_to_python(memory_handler, results)
        for instance, addr in ret:
            yield addr

class HaystackShow(HaystackSearch):
    """
    Show the record value
    """
    def __init__(self, config, *args, **kwargs):
        HaystackSearch.__init__(self, config, *args, **kwargs)
        config.add_option('ADDRESS', short_option='a', default= None,
                          help='Using this address (hex) to load the record',
                          action='store', type='str')

    def make_search_results(self, memory_handler, struct_type, my_constraints):
        addr = int(self.config.ADDRESS, 16)
        results = api.load_record(memory_handler, struct_type, addr, load_constraints=my_constraints)
        instance = api.output_to_string(memory_handler, [results])
        yield (instance, addr)

    def render_text(self, outfd, data):
        for pid, (instance, addr) in data:
            outfd.write("*" * 72 + "\n")
            outfd.write("Pid: {0:6}\n".format(pid))
            outfd.write('Record %s at 0x%x\n' % (self.classname, addr))
            outfd.write('Record content:\n')
            outfd.write(instance)



class HaystackReverse(Haystack):
    """
    Reverse all the allocated records of a process memory.
    """
    def __init__(self, config, *args, **kwargs):
        self.config = config
        taskmods.DllList.__init__(self, config, *args, **kwargs)

    def make_results(self, pid, memory_handler):
        from haystack.reverse import context
        log.debug('[+] Loading the memory dump ')
        ctx = context.get_context(dumpname)
        try:
            if not os.access(config.get_record_cache_folder_name(ctx.dumpname), os.F_OK):
                os.mkdir(config.get_record_cache_folder_name(ctx.dumpname))

            log.info("[+] Cache created in %s", config.get_record_cache_folder_name(ctx.dumpname))

            # we use common allocators to find structures.
            #log.debug('Reversing malloc')
            #mallocRev = MallocReverser()
            #ctx = mallocRev.reverse(ctx)
            # mallocRev.check_inuse(ctx)

            # try to find some logical constructs.
            log.debug('Reversing DoubleLinkedListReverser')
            doublelink = DoubleLinkedListReverser(ctx)
            ctx = doublelink.reverse(ctx)

            # decode bytes contents to find basic types.
            log.debug('Reversing Fields')
            fr = FieldReverser(ctx)
            ctx = fr.reverse(ctx)

            # identify pointer relation between structures
            log.debug('Reversing PointerFields')
            pfr = PointerFieldReverser(ctx)
            ctx = pfr.reverse(ctx)

            # graph pointer relations between structures
            log.debug('Reversing PointerGraph')
            ptrgraph = PointerGraphReverser(ctx)
            ctx = ptrgraph.reverse(ctx)
            ptrgraph._saveStructures(ctx)

            # save to file
            save_headers(ctx)
            # fr._saveStructures(ctx)
            ##libRev = KnowStructReverser('libQt')
            ##ctx = libRev.reverse(ctx)
            # we have more enriched context

            # etc
        except KeyboardInterrupt as e:
            # except IOError,e:
            log.warning(e)
            log.info('[+] %d structs extracted' % (ctx.structuresCount()))
            raise e
            pass
        pass
