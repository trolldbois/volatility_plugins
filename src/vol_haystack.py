"""
Plugin to find records using the haystack library.

python vol.py --plugins=contrib/plugins -f ...

"""

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
    """Display process command-line arguments"""
    def __init__(self, config, *args, **kwargs):
        self.config = config
        taskmods.DllList.__init__(self, config, *args, **kwargs)
        config.add_option('RECORD_NAME', short_option='r', default= None,
                          help='Search for this record type',
                          action='store', type='str')
        config.add_option('CONSTRAINT_FILE', short_option='c', default= None,
                          help='Using this constraint file',
                          action='store', type='str')

    def unified_output(self, data):
        # blank header in case there is no shimcache data
        return TreeGrid([("PID", int), ("Address", int)
                       ], self.generator(data))

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

    def _search(self, task):
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

        # import the record class in the haystack model
        module = memory_handler.get_model().import_module(self.modulename)
        struct_type = getattr(module, self.classname)
        for res in self.make_results(memory_handler, struct_type, self.my_constraints):
            yield pid, res

    def make_results(self, memory_handler, struct_type, my_constraints):
            # do the search
            # do not use the haystack HEAP parsing capabilities
            if False:
                ## PROD - use API
                results = api.search_record(memory_handler, struct_type, my_constraints, extended_search=True)
                # output handling
                ret = api.output_to_python(memory_handler, results)
                for instance, addr in ret:
                    yield addr
            else:
                ## DEBUG - use optimised search space for HEAP
                my_searcher = searcher.AnyOffsetRecordSearcher(memory_handler, my_constraints)
                for mapping in memory_handler.get_mappings():
                    res = my_searcher._search_in(mapping, struct_type, nb=1, align=0x1000)
                    if res:
                        instance, addr = api.output_to_python(memory_handler, res)[0]
                        yield addr
            ## use direct load
            # results = api.load_record(memory_handler, struct_type, 0x150000, load_constraints=None)

    def render_text(self, outfd, data):
        self._init_haystack()
        for task in data:
            outfd.write("*" * 72 + "\n")
            outfd.write("Pid: {0:6}\n".format(task.UniqueProcessId))
            for res in self._search(task):
                x, addr = res
                outfd.write('Record %s at 0x%x\n' % (self.classname, addr))

    def generator(self, data):
        self._init_haystack()
        for task in data:
            yield self._search(task)
