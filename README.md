
Usage:

1. Install volatility as per instructions
2. `git clone https://github.com/trolldbois/volatility_plugins.git`
3. `vol.py --plugins=volatility_plugins/src/ -f <path_to_memory_dump> haystack -p <pid> -r <record name> -c <constraint_file>`

For example, to list all WinXP x86 Heaps in the zeus.vmem image
`vol.py --plugins=volatility_plugins/src -f ~/outputs/vol/zeus.vmem haystack -r haystack.structures.win32.winxp_32.HEAP -c  winxpheap.constraints -p4` 

  ************************************************************************
  Pid:      4
  Record HEAP at 0x70000
  
  real	2m28.363s
  user	2m20.109s
  sys	0m8.132s

This will print out the PID and the address of HEAPs.

If you want to search for more that just HEAP structures provided by haystack, 
you can use ctypeslib to generate your own structures frmo your favorite C headers. 

You might want to look at https://github.com/trolldbois/ctypeslib to produce your own records.

For example, Work in progress is ongoing to get SSH/SSL record from sslsnoop updated to the latest version of haystack. 
