"""
Plugin to find records using the haystack library.

python vol.py --plugins=contrib/plugins -f ...

"""
import ctypes
import os
import re
import struct

from itertools import groupby

import volatility

import volatility.plugins.taskmods as taskmods
from volatility.renderers import TreeGrid

class Haystack(taskmods.DllList):
    """Display process command-line arguments"""

    def unified_output(self, data):
        # blank header in case there is no shimcache data
        return TreeGrid([("Process", str),
                       ("PID", int),
                       ("CommandLine", str),
                       ], self.generator(data))

    def generator(self, data):
        raise RuntimeError('qw;fjqw')
        for task in data:
            cmdline = ""
            if task.Peb:
                cmdline = "{0}".format(str(task.Peb.ProcessParameters.CommandLine or '')).strip()
            yield (0, [str(task.ImageFileName), int(task.UniqueProcessId), str(cmdline)])

    def render_text(self, outfd, data):
        raise ValueError('qw;fjqw')
        for task in data:
            pid = task.UniqueProcessId

            outfd.write("*" * 72 + "\n")
            outfd.write("{0} pid: {1:6}\n".format(task.ImageFileName, pid))

            if task.Peb:
                outfd.write("Command line : {0}\n".format(str(task.Peb.ProcessParameters.CommandLine or '')))



def get_heaps(task):
    """
    Given a task, return the mapped sections corresponding to that task's
    heaps.
    """
    for vma in task.get_proc_maps():
        if (vma.vm_start <= task.mm.start_brk and vma.vm_end >= task.mm.brk):
            yield vma

