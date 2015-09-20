#!/bin/sh

clang2py ctypes_openssl.c -o records_openssl_32.py -i --target i386-linux
clang2py ctypes_openssl.c -o records_openssl_64.py -i --target x86_64

# lets assume ssh.memorydump.1212 is the memory dump of a ssh process
haystack --dumpname ssh.memorydump.1212/ --string search records_openssl_32.struct_evp_cipher_ctx_st --constraints_file openssl.constraints
## this will return the addresses of the 2 OpenSSL session context records. (in, out)
