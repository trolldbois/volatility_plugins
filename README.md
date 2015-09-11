
Usage:

1. Install volatility as per instructions
2. `git clone https://github.com/trolldbois/volatility_plugins.git`
3. `vol.py --plugins=volatility_plugins/src/ -f <path_to_memory_dump> haystack -r haystack.structures.win32.winxp_32.HEAP -c winxpheap.constraints`


For example, to list all WinXP x86 Heaps in the zeus.vmem image
`vol.py --plugins=volatility_plugins/src -f ~/outputs/vol/zeus.vmem haystack -p 1668 -r haystack.structures.win32.winxp_32.HEAP -c  winxpheap.constraints` 

This will print out the PID and the address of HEAPs
