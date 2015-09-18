# -*- coding: utf-8 -*-
#
# TARGET arch is: []
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16

# if local wordsize is same as target, keep ctypes pointer function.
if ctypes.sizeof(ctypes.c_void_p) == 8:
    POINTER_T = ctypes.POINTER
else:
    # required to access _ctypes
    import _ctypes
    # Emulate a pointer class using the approriate c_int32/c_int64 type
    # The new class should have :
    # ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
    # but the class should be submitted to a unique instance for each base type
    # to that if A == B, POINTER_T(A) == POINTER_T(B)
    ctypes._pointer_t_type_cache = {}
    def POINTER_T(pointee):
        # a pointer should have the same length as LONG
        fake_ptr_base_type = ctypes.c_uint64 
        # specific case for c_void_p
        if pointee is None: # VOID pointer type. c_void_p.
            pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
            clsname = 'c_void'
        else:
            clsname = pointee.__name__
        if clsname in ctypes._pointer_t_type_cache:
            return ctypes._pointer_t_type_cache[clsname]
        # make template
        class _T(_ctypes._SimpleCData,):
            _type_ = 'L'
            _subtype_ = pointee
            def _sub_addr_(self):
                return self.value
            def __repr__(self):
                return '%s(%d)'%(clsname, self.value)
            def contents(self):
                raise TypeError('This is not a ctypes pointer.')
            def __init__(self, **args):
                raise TypeError('This is not a ctypes pointer. It is not instanciable.')
        _class = type('LP_%d_%s'%(8, clsname), (_T,),{}) 
        ctypes._pointer_t_type_cache[clsname] = _class
        return _class



class struct_c__SA__G_fpos_t(ctypes.Structure):
    pass

class struct_c__SA___mbstate_t(ctypes.Structure):
    pass

class union_c__SA___mbstate_t_0(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('__wch', ctypes.c_uint32),
    ('__wchb', ctypes.c_char * 4),
     ]

struct_c__SA___mbstate_t._pack_ = True # source:False
struct_c__SA___mbstate_t._fields_ = [
    ('__count', ctypes.c_int32),
    ('__value', union_c__SA___mbstate_t_0),
]

__mbstate_t = struct_c__SA___mbstate_t
struct_c__SA__G_fpos_t._pack_ = True # source:False
struct_c__SA__G_fpos_t._fields_ = [
    ('__pos', ctypes.c_int64),
    ('__state', globals()['__mbstate_t']),
]

_G_fpos_t = struct_c__SA__G_fpos_t
class struct_c__SA__G_fpos64_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__pos', ctypes.c_int64),
    ('__state', globals()['__mbstate_t']),
     ]

_G_fpos64_t = struct_c__SA__G_fpos64_t
_IO_lock_t = None
class struct__IO_marker(ctypes.Structure):
    pass

class struct__IO_FILE(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('PADDING_0', ctypes.c_ubyte),
     ]

struct__IO_marker._pack_ = True # source:False
struct__IO_marker._fields_ = [
    ('_next', POINTER_T(struct__IO_marker)),
    ('_sbuf', POINTER_T(struct__IO_FILE)),
    ('_pos', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
]


# values for enumeration '__codecvt_result'
__codecvt_result = ctypes.c_int # enum
_IO_FILE = struct__IO_FILE
__io_read_fn = ctypes.CFUNCTYPE(ctypes.c_int64, POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32)
__io_write_fn = ctypes.CFUNCTYPE(ctypes.c_int64, POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32)
__io_seek_fn = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(ctypes.c_int64), ctypes.c_int32)
__io_close_fn = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None))
class struct_aes_key_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('rd_key', ctypes.c_uint32 * 60),
    ('rounds', ctypes.c_int32),
     ]

AES_KEY = struct_aes_key_st
class struct_stack_st_X509_ALGOR(ctypes.Structure):
    pass

class struct_stack_st(ctypes.Structure):
    pass

struct_stack_st._pack_ = True # source:False
struct_stack_st._fields_ = [
    ('num', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('data', POINTER_T(POINTER_T(ctypes.c_char))),
    ('sorted', ctypes.c_int32),
    ('num_alloc', ctypes.c_int32),
    ('comp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(None)))),
]

_STACK = struct_stack_st
struct_stack_st_X509_ALGOR._pack_ = True # source:False
struct_stack_st_X509_ALGOR._fields_ = [
    ('stack', _STACK),
]

class struct_asn1_ctx_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('p', POINTER_T(ctypes.c_ubyte)),
    ('eos', ctypes.c_int32),
    ('error', ctypes.c_int32),
    ('inf', ctypes.c_int32),
    ('tag', ctypes.c_int32),
    ('xclass', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('slen', ctypes.c_int64),
    ('max', POINTER_T(ctypes.c_ubyte)),
    ('q', POINTER_T(ctypes.c_ubyte)),
    ('pp', POINTER_T(POINTER_T(ctypes.c_ubyte))),
    ('line', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
     ]

ASN1_CTX = struct_asn1_ctx_st
class struct_asn1_const_ctx_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('p', POINTER_T(ctypes.c_ubyte)),
    ('eos', ctypes.c_int32),
    ('error', ctypes.c_int32),
    ('inf', ctypes.c_int32),
    ('tag', ctypes.c_int32),
    ('xclass', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('slen', ctypes.c_int64),
    ('max', POINTER_T(ctypes.c_ubyte)),
    ('q', POINTER_T(ctypes.c_ubyte)),
    ('pp', POINTER_T(POINTER_T(ctypes.c_ubyte))),
    ('line', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
     ]

ASN1_const_CTX = struct_asn1_const_ctx_st
class struct_asn1_object_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sn', POINTER_T(ctypes.c_char)),
    ('ln', POINTER_T(ctypes.c_char)),
    ('nid', ctypes.c_int32),
    ('length', ctypes.c_int32),
    ('data', POINTER_T(ctypes.c_ubyte)),
    ('flags', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

ASN1_OBJECT = struct_asn1_object_st
class struct_ASN1_ENCODING_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('enc', POINTER_T(ctypes.c_ubyte)),
    ('len', ctypes.c_int64),
    ('modified', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

ASN1_ENCODING = struct_ASN1_ENCODING_st
class struct_asn1_string_table_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('nid', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('minsize', ctypes.c_int64),
    ('maxsize', ctypes.c_int64),
    ('mask', ctypes.c_uint64),
    ('flags', ctypes.c_uint64),
     ]

ASN1_STRING_TABLE = struct_asn1_string_table_st
class struct_stack_st_ASN1_STRING_TABLE(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

i2d_of_void = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(POINTER_T(ctypes.c_ubyte)))
d2i_of_void = ctypes.CFUNCTYPE(POINTER_T(None), POINTER_T(POINTER_T(None)), POINTER_T(POINTER_T(ctypes.c_ubyte)), ctypes.c_int64)
class struct_stack_st_ASN1_INTEGER(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_stack_st_ASN1_GENERALSTRING(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_asn1_type_st(ctypes.Structure):
    pass

class union_asn1_type_st_0(ctypes.Union):
    pass

class struct_asn1_string_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('length', ctypes.c_int32),
    ('type', ctypes.c_int32),
    ('data', POINTER_T(ctypes.c_ubyte)),
    ('flags', ctypes.c_int64),
     ]

union_asn1_type_st_0._pack_ = True # source:False
union_asn1_type_st_0._fields_ = [
    ('ptr', POINTER_T(ctypes.c_char)),
    ('boolean', ctypes.c_int32),
    ('asn1_string', POINTER_T(struct_asn1_string_st)),
    ('object', POINTER_T(struct_asn1_object_st)),
    ('integer', POINTER_T(struct_asn1_string_st)),
    ('enumerated', POINTER_T(struct_asn1_string_st)),
    ('bit_string', POINTER_T(struct_asn1_string_st)),
    ('octet_string', POINTER_T(struct_asn1_string_st)),
    ('printablestring', POINTER_T(struct_asn1_string_st)),
    ('t61string', POINTER_T(struct_asn1_string_st)),
    ('ia5string', POINTER_T(struct_asn1_string_st)),
    ('generalstring', POINTER_T(struct_asn1_string_st)),
    ('bmpstring', POINTER_T(struct_asn1_string_st)),
    ('universalstring', POINTER_T(struct_asn1_string_st)),
    ('utctime', POINTER_T(struct_asn1_string_st)),
    ('generalizedtime', POINTER_T(struct_asn1_string_st)),
    ('visiblestring', POINTER_T(struct_asn1_string_st)),
    ('utf8string', POINTER_T(struct_asn1_string_st)),
    ('set', POINTER_T(struct_asn1_string_st)),
    ('sequence', POINTER_T(struct_asn1_string_st)),
    ('asn1_value', POINTER_T(None)),
]

struct_asn1_type_st._pack_ = True # source:False
struct_asn1_type_st._fields_ = [
    ('type', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('value', union_asn1_type_st_0),
]

ASN1_TYPE = struct_asn1_type_st
class struct_stack_st_ASN1_TYPE(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

ASN1_SEQUENCE_ANY = struct_stack_st_ASN1_TYPE
class struct_NETSCAPE_X509_st(ctypes.Structure):
    pass

class struct_x509_st(ctypes.Structure):
    pass

class struct_x509_cinf_st(ctypes.Structure):
    pass

class struct_X509_name_st(ctypes.Structure):
    pass

class struct_stack_st_X509_NAME_ENTRY(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_buf_mem_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('PADDING_0', ctypes.c_ubyte),
     ]

struct_X509_name_st._pack_ = True # source:False
struct_X509_name_st._fields_ = [
    ('entries', POINTER_T(struct_stack_st_X509_NAME_ENTRY)),
    ('modified', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('bytes', POINTER_T(struct_buf_mem_st)),
    ('canon_enc', POINTER_T(ctypes.c_ubyte)),
    ('canon_enclen', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
]

class struct_X509_pubkey_st(ctypes.Structure):
    pass

class struct_X509_algor_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('algorithm', POINTER_T(struct_asn1_object_st)),
    ('parameter', POINTER_T(struct_asn1_type_st)),
     ]

class struct_evp_pkey_st(ctypes.Structure):
    pass

class union_evp_pkey_st_0(ctypes.Union):
    pass

class struct_dh_st(ctypes.Structure):
    pass

class struct_crypto_ex_data_st(ctypes.Structure):
    pass

class struct_stack_st_void(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

struct_crypto_ex_data_st._pack_ = True # source:False
struct_crypto_ex_data_st._fields_ = [
    ('sk', POINTER_T(struct_stack_st_void)),
    ('dummy', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
]

CRYPTO_EX_DATA = struct_crypto_ex_data_st
class struct_bn_mont_ctx_st(ctypes.Structure):
    pass

class struct_bignum_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('d', POINTER_T(ctypes.c_uint64)),
    ('top', ctypes.c_int32),
    ('dmax', ctypes.c_int32),
    ('neg', ctypes.c_int32),
    ('flags', ctypes.c_int32),
     ]

BIGNUM = struct_bignum_st
struct_bn_mont_ctx_st._pack_ = True # source:False
struct_bn_mont_ctx_st._fields_ = [
    ('ri', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('RR', BIGNUM),
    ('N', BIGNUM),
    ('Ni', BIGNUM),
    ('n0', ctypes.c_uint64 * 2),
    ('flags', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
]

class struct_dh_method(ctypes.Structure):
    pass

class struct_bn_gencb_st(ctypes.Structure):
    pass

struct_dh_method._pack_ = True # source:False
struct_dh_method._fields_ = [
    ('name', POINTER_T(ctypes.c_char)),
    ('generate_key', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dh_st)))),
    ('compute_key', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(ctypes.c_ubyte), POINTER_T(struct_bignum_st), POINTER_T(struct_dh_st)))),
    ('bn_mod_exp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dh_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(None), POINTER_T(struct_bn_mont_ctx_st)))),
    ('init', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dh_st)))),
    ('finish', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dh_st)))),
    ('flags', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('app_data', POINTER_T(ctypes.c_char)),
    ('generate_params', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dh_st), ctypes.c_int32, ctypes.c_int32, POINTER_T(struct_bn_gencb_st)))),
]

struct_dh_st._pack_ = True # source:False
struct_dh_st._fields_ = [
    ('pad', ctypes.c_int32),
    ('version', ctypes.c_int32),
    ('p', POINTER_T(struct_bignum_st)),
    ('g', POINTER_T(struct_bignum_st)),
    ('length', ctypes.c_int64),
    ('pub_key', POINTER_T(struct_bignum_st)),
    ('priv_key', POINTER_T(struct_bignum_st)),
    ('flags', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('method_mont_p', POINTER_T(struct_bn_mont_ctx_st)),
    ('q', POINTER_T(struct_bignum_st)),
    ('j', POINTER_T(struct_bignum_st)),
    ('seed', POINTER_T(ctypes.c_ubyte)),
    ('seedlen', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('counter', POINTER_T(struct_bignum_st)),
    ('references', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
    ('ex_data', CRYPTO_EX_DATA),
    ('meth', POINTER_T(struct_dh_method)),
    ('engine', POINTER_T(None)),
]

class struct_dsa_st(ctypes.Structure):
    pass

class struct_dsa_method(ctypes.Structure):
    pass

class struct_DSA_SIG_st(ctypes.Structure):
    pass

struct_dsa_method._pack_ = True # source:False
struct_dsa_method._fields_ = [
    ('name', POINTER_T(ctypes.c_char)),
    ('dsa_do_sign', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(struct_DSA_SIG_st), POINTER_T(ctypes.c_ubyte), ctypes.c_int32, POINTER_T(struct_dsa_st)))),
    ('dsa_sign_setup', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dsa_st), POINTER_T(None), POINTER_T(POINTER_T(struct_bignum_st)), POINTER_T(POINTER_T(struct_bignum_st))))),
    ('dsa_do_verify', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_int32, POINTER_T(struct_DSA_SIG_st), POINTER_T(struct_dsa_st)))),
    ('dsa_mod_exp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dsa_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(None), POINTER_T(struct_bn_mont_ctx_st)))),
    ('bn_mod_exp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dsa_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(None), POINTER_T(struct_bn_mont_ctx_st)))),
    ('init', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dsa_st)))),
    ('finish', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dsa_st)))),
    ('flags', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('app_data', POINTER_T(ctypes.c_char)),
    ('dsa_paramgen', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dsa_st), ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_int32, POINTER_T(ctypes.c_int32), POINTER_T(ctypes.c_uint64), POINTER_T(struct_bn_gencb_st)))),
    ('dsa_keygen', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_dsa_st)))),
]

struct_dsa_st._pack_ = True # source:False
struct_dsa_st._fields_ = [
    ('pad', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('version', ctypes.c_int64),
    ('write_params', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('p', POINTER_T(struct_bignum_st)),
    ('q', POINTER_T(struct_bignum_st)),
    ('g', POINTER_T(struct_bignum_st)),
    ('pub_key', POINTER_T(struct_bignum_st)),
    ('priv_key', POINTER_T(struct_bignum_st)),
    ('kinv', POINTER_T(struct_bignum_st)),
    ('r', POINTER_T(struct_bignum_st)),
    ('flags', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
    ('method_mont_p', POINTER_T(struct_bn_mont_ctx_st)),
    ('references', ctypes.c_int32),
    ('PADDING_3', ctypes.c_ubyte * 4),
    ('ex_data', CRYPTO_EX_DATA),
    ('meth', POINTER_T(struct_dsa_method)),
    ('engine', POINTER_T(None)),
]

class struct_rsa_st(ctypes.Structure):
    pass

class struct_rsa_meth_st(ctypes.Structure):
    pass

struct_rsa_meth_st._pack_ = True # source:False
struct_rsa_meth_st._fields_ = [
    ('name', POINTER_T(ctypes.c_char)),
    ('rsa_pub_enc', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_ubyte), POINTER_T(struct_rsa_st), ctypes.c_int32))),
    ('rsa_pub_dec', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_ubyte), POINTER_T(struct_rsa_st), ctypes.c_int32))),
    ('rsa_priv_enc', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_ubyte), POINTER_T(struct_rsa_st), ctypes.c_int32))),
    ('rsa_priv_dec', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_ubyte), POINTER_T(struct_rsa_st), ctypes.c_int32))),
    ('rsa_mod_exp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_rsa_st), POINTER_T(None)))),
    ('bn_mod_exp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(struct_bignum_st), POINTER_T(None), POINTER_T(struct_bn_mont_ctx_st)))),
    ('init', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_rsa_st)))),
    ('finish', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_rsa_st)))),
    ('flags', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('app_data', POINTER_T(ctypes.c_char)),
    ('rsa_sign', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_uint32), POINTER_T(struct_rsa_st)))),
    ('rsa_verify', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(struct_rsa_st)))),
    ('rsa_keygen', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_rsa_st), ctypes.c_int32, POINTER_T(struct_bignum_st), POINTER_T(struct_bn_gencb_st)))),
]

struct_rsa_st._pack_ = True # source:False
struct_rsa_st._fields_ = [
    ('pad', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('version', ctypes.c_int64),
    ('meth', POINTER_T(struct_rsa_meth_st)),
    ('engine', POINTER_T(None)),
    ('n', POINTER_T(struct_bignum_st)),
    ('e', POINTER_T(struct_bignum_st)),
    ('d', POINTER_T(struct_bignum_st)),
    ('p', POINTER_T(struct_bignum_st)),
    ('q', POINTER_T(struct_bignum_st)),
    ('dmp1', POINTER_T(struct_bignum_st)),
    ('dmq1', POINTER_T(struct_bignum_st)),
    ('iqmp', POINTER_T(struct_bignum_st)),
    ('ex_data', CRYPTO_EX_DATA),
    ('references', ctypes.c_int32),
    ('flags', ctypes.c_int32),
    ('_method_mod_n', POINTER_T(struct_bn_mont_ctx_st)),
    ('_method_mod_p', POINTER_T(struct_bn_mont_ctx_st)),
    ('_method_mod_q', POINTER_T(struct_bn_mont_ctx_st)),
    ('bignum_data', POINTER_T(ctypes.c_char)),
    ('blinding', POINTER_T(None)),
    ('mt_blinding', POINTER_T(None)),
]

union_evp_pkey_st_0._pack_ = True # source:False
union_evp_pkey_st_0._fields_ = [
    ('ptr', POINTER_T(ctypes.c_char)),
    ('rsa', POINTER_T(struct_rsa_st)),
    ('dsa', POINTER_T(struct_dsa_st)),
    ('dh', POINTER_T(struct_dh_st)),
    ('ec', POINTER_T(None)),
]

class struct_stack_st_X509_ATTRIBUTE(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

struct_evp_pkey_st._pack_ = True # source:False
struct_evp_pkey_st._fields_ = [
    ('type', ctypes.c_int32),
    ('save_type', ctypes.c_int32),
    ('references', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('ameth', POINTER_T(None)),
    ('engine', POINTER_T(None)),
    ('pkey', union_evp_pkey_st_0),
    ('save_parameters', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('attributes', POINTER_T(struct_stack_st_X509_ATTRIBUTE)),
]

struct_X509_pubkey_st._pack_ = True # source:False
struct_X509_pubkey_st._fields_ = [
    ('algor', POINTER_T(struct_X509_algor_st)),
    ('public_key', POINTER_T(struct_asn1_string_st)),
    ('pkey', POINTER_T(struct_evp_pkey_st)),
]

class struct_X509_val_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('notBefore', POINTER_T(struct_asn1_string_st)),
    ('notAfter', POINTER_T(struct_asn1_string_st)),
     ]

class struct_stack_st_X509_EXTENSION(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

struct_x509_cinf_st._pack_ = True # source:False
struct_x509_cinf_st._fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('serialNumber', POINTER_T(struct_asn1_string_st)),
    ('signature', POINTER_T(struct_X509_algor_st)),
    ('issuer', POINTER_T(struct_X509_name_st)),
    ('validity', POINTER_T(struct_X509_val_st)),
    ('subject', POINTER_T(struct_X509_name_st)),
    ('key', POINTER_T(struct_X509_pubkey_st)),
    ('issuerUID', POINTER_T(struct_asn1_string_st)),
    ('subjectUID', POINTER_T(struct_asn1_string_st)),
    ('extensions', POINTER_T(struct_stack_st_X509_EXTENSION)),
    ('enc', ASN1_ENCODING),
]

class struct_x509_cert_aux_st(ctypes.Structure):
    pass

class struct_stack_st_ASN1_OBJECT(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

struct_x509_cert_aux_st._pack_ = True # source:False
struct_x509_cert_aux_st._fields_ = [
    ('trust', POINTER_T(struct_stack_st_ASN1_OBJECT)),
    ('reject', POINTER_T(struct_stack_st_ASN1_OBJECT)),
    ('alias', POINTER_T(struct_asn1_string_st)),
    ('keyid', POINTER_T(struct_asn1_string_st)),
    ('other', POINTER_T(struct_stack_st_X509_ALGOR)),
]

struct_x509_st._pack_ = True # source:False
struct_x509_st._fields_ = [
    ('cert_info', POINTER_T(struct_x509_cinf_st)),
    ('sig_alg', POINTER_T(struct_X509_algor_st)),
    ('signature', POINTER_T(struct_asn1_string_st)),
    ('valid', ctypes.c_int32),
    ('references', ctypes.c_int32),
    ('name', POINTER_T(ctypes.c_char)),
    ('ex_data', CRYPTO_EX_DATA),
    ('ex_pathlen', ctypes.c_int64),
    ('ex_pcpathlen', ctypes.c_int64),
    ('ex_flags', ctypes.c_uint64),
    ('ex_kusage', ctypes.c_uint64),
    ('ex_xkusage', ctypes.c_uint64),
    ('ex_nscert', ctypes.c_uint64),
    ('skid', POINTER_T(struct_asn1_string_st)),
    ('akid', POINTER_T(None)),
    ('policy_cache', POINTER_T(None)),
    ('crldp', POINTER_T(None)),
    ('altname', POINTER_T(None)),
    ('nc', POINTER_T(None)),
    ('sha1_hash', ctypes.c_ubyte * 20),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('aux', POINTER_T(struct_x509_cert_aux_st)),
]

struct_NETSCAPE_X509_st._pack_ = True # source:False
struct_NETSCAPE_X509_st._fields_ = [
    ('header', POINTER_T(struct_asn1_string_st)),
    ('cert', POINTER_T(struct_x509_st)),
]

NETSCAPE_X509 = struct_NETSCAPE_X509_st
class struct_BIT_STRING_BITNAME_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('bitnum', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('lname', POINTER_T(ctypes.c_char)),
    ('sname', POINTER_T(ctypes.c_char)),
     ]

BIT_STRING_BITNAME = struct_BIT_STRING_BITNAME_st
class struct_bio_st(ctypes.Structure):
    pass

class struct_bio_method_st(ctypes.Structure):
    pass

struct_bio_method_st._pack_ = True # source:False
struct_bio_method_st._fields_ = [
    ('type', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('name', POINTER_T(ctypes.c_char)),
    ('bwrite', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bio_st), POINTER_T(ctypes.c_char), ctypes.c_int32))),
    ('bread', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bio_st), POINTER_T(ctypes.c_char), ctypes.c_int32))),
    ('bputs', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bio_st), POINTER_T(ctypes.c_char)))),
    ('bgets', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bio_st), POINTER_T(ctypes.c_char), ctypes.c_int32))),
    ('ctrl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int64, POINTER_T(struct_bio_st), ctypes.c_int32, ctypes.c_int64, POINTER_T(None)))),
    ('create', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bio_st)))),
    ('destroy', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bio_st)))),
    ('callback_ctrl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int64, POINTER_T(struct_bio_st), ctypes.c_int32, POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(struct_bio_st), ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32, ctypes.c_int64, ctypes.c_int64))))),
]

struct_bio_st._pack_ = True # source:False
struct_bio_st._fields_ = [
    ('method', POINTER_T(struct_bio_method_st)),
    ('callback', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int64, POINTER_T(struct_bio_st), ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32, ctypes.c_int64, ctypes.c_int64))),
    ('cb_arg', POINTER_T(ctypes.c_char)),
    ('init', ctypes.c_int32),
    ('shutdown', ctypes.c_int32),
    ('flags', ctypes.c_int32),
    ('retry_reason', ctypes.c_int32),
    ('num', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('ptr', POINTER_T(None)),
    ('next_bio', POINTER_T(struct_bio_st)),
    ('prev_bio', POINTER_T(struct_bio_st)),
    ('references', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('num_read', ctypes.c_uint64),
    ('num_write', ctypes.c_uint64),
    ('ex_data', CRYPTO_EX_DATA),
]

BIO = struct_bio_st
bio_info_cb = ctypes.CFUNCTYPE(None, POINTER_T(struct_bio_st), ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32, ctypes.c_int64, ctypes.c_int64)
BIO_METHOD = struct_bio_method_st
class struct_stack_st_BIO(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_bio_f_buffer_ctx_struct(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ibuf_size', ctypes.c_int32),
    ('obuf_size', ctypes.c_int32),
    ('ibuf', POINTER_T(ctypes.c_char)),
    ('ibuf_len', ctypes.c_int32),
    ('ibuf_off', ctypes.c_int32),
    ('obuf', POINTER_T(ctypes.c_char)),
    ('obuf_len', ctypes.c_int32),
    ('obuf_off', ctypes.c_int32),
     ]

BIO_F_BUFFER_CTX = struct_bio_f_buffer_ctx_struct
asn1_ps_func = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_bio_st), POINTER_T(POINTER_T(ctypes.c_ubyte)), POINTER_T(ctypes.c_int32), POINTER_T(None))
class struct_bf_key_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('P', ctypes.c_uint32 * 18),
    ('S', ctypes.c_uint32 * 1024),
     ]

BF_KEY = struct_bf_key_st
class union_bn_gencb_st_0(ctypes.Union):
    pass

union_bn_gencb_st_0._pack_ = True # source:False
union_bn_gencb_st_0._fields_ = [
    ('cb_1', POINTER_T(ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_int32, POINTER_T(None)))),
    ('cb_2', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, POINTER_T(struct_bn_gencb_st)))),
]

class struct_cast_key_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_uint32 * 32),
    ('short_key', ctypes.c_int32),
     ]

CAST_KEY = struct_cast_key_st
class struct_openssl_item_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('PADDING_0', ctypes.c_ubyte),
     ]

OPENSSL_ITEM = struct_openssl_item_st
class struct_c__SA_CRYPTO_dynlock(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('references', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('data', POINTER_T(None)),
     ]

CRYPTO_dynlock = struct_c__SA_CRYPTO_dynlock
BIO_dummy = struct_bio_st
class struct_crypto_ex_data_func_st(ctypes.Structure):
    pass

struct_crypto_ex_data_func_st._pack_ = True # source:False
struct_crypto_ex_data_func_st._fields_ = [
    ('argl', ctypes.c_int64),
    ('argp', POINTER_T(None)),
    ('new_func', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(None), POINTER_T(struct_crypto_ex_data_st), ctypes.c_int32, ctypes.c_int64, POINTER_T(None)))),
    ('free_func', POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None), POINTER_T(None), POINTER_T(struct_crypto_ex_data_st), ctypes.c_int32, ctypes.c_int64, POINTER_T(None)))),
    ('dup_func', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_crypto_ex_data_st), POINTER_T(struct_crypto_ex_data_st), POINTER_T(None), ctypes.c_int32, ctypes.c_int64, POINTER_T(None)))),
]

CRYPTO_EX_DATA_FUNCS = struct_crypto_ex_data_func_st
class struct_stack_st_CRYPTO_EX_DATA_FUNCS(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_crypto_threadid_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ptr', POINTER_T(None)),
    ('val', ctypes.c_uint64),
     ]

CRYPTO_THREADID = struct_crypto_threadid_st
CRYPTO_MEM_LEAK_CB = ctypes.CFUNCTYPE(POINTER_T(None), ctypes.c_uint64, POINTER_T(ctypes.c_char), ctypes.c_int32, ctypes.c_int32, POINTER_T(None))
DES_cblock = ctypes.c_ubyte * 8
const_DES_cblock = ctypes.c_ubyte * 8
class struct_DES_ks(ctypes.Structure):
    pass

class union_DES_ks_0(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('cblock', ctypes.c_ubyte * 8),
    ('deslong', ctypes.c_uint32 * 2),
     ]

struct_DES_ks._pack_ = True # source:False
struct_DES_ks._fields_ = [
    ('ks', union_DES_ks_0 * 16),
]

DES_key_schedule = struct_DES_ks
_shadow_DES_check_key = None # Variable ctypes.c_int32
_shadow_DES_rw_mode = None # Variable ctypes.c_int32
_ossl_old_des_cblock = ctypes.c_ubyte * 8
class struct__ossl_old_des_ks_struct(ctypes.Structure):
    pass

class union__ossl_old_des_ks_struct_0(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('_', ctypes.c_ubyte * 8),
    ('pad', ctypes.c_uint32 * 2),
     ]

struct__ossl_old_des_ks_struct._pack_ = True # source:False
struct__ossl_old_des_ks_struct._fields_ = [
    ('ks', union__ossl_old_des_ks_struct_0),
]

_ossl_old_des_key_schedule = struct__ossl_old_des_ks_struct * 16
struct_DSA_SIG_st._pack_ = True # source:False
struct_DSA_SIG_st._fields_ = [
    ('r', POINTER_T(struct_bignum_st)),
    ('s', POINTER_T(struct_bignum_st)),
]

DSA_SIG = struct_DSA_SIG_st

# values for enumeration 'c__EA_point_conversion_form_t'
c__EA_point_conversion_form_t = ctypes.c_int # enum
point_conversion_form_t = c__EA_point_conversion_form_t
class struct_c__SA_EC_builtin_curve(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('nid', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('comment', POINTER_T(ctypes.c_char)),
     ]

EC_builtin_curve = struct_c__SA_EC_builtin_curve
class struct_ECDSA_SIG_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('r', POINTER_T(struct_bignum_st)),
    ('s', POINTER_T(struct_bignum_st)),
     ]

ECDSA_SIG = struct_ECDSA_SIG_st
class struct_ENGINE_CMD_DEFN_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('cmd_num', ctypes.c_uint32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('cmd_name', POINTER_T(ctypes.c_char)),
    ('cmd_desc', POINTER_T(ctypes.c_char)),
    ('cmd_flags', ctypes.c_uint32),
    ('PADDING_1', ctypes.c_ubyte * 4),
     ]

ENGINE_CMD_DEFN = struct_ENGINE_CMD_DEFN_st
ENGINE_GEN_FUNC_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32))
ENGINE_GEN_INT_FUNC_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None)))
ENGINE_CTRL_FUNC_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), ctypes.c_int32, ctypes.c_int64, POINTER_T(None), POINTER_T(ctypes.CFUNCTYPE(None))))
ENGINE_LOAD_KEY_PTR = POINTER_T(ctypes.CFUNCTYPE(POINTER_T(struct_evp_pkey_st), POINTER_T(None), POINTER_T(ctypes.c_char), POINTER_T(None), POINTER_T(None)))
class struct_stack_st_X509_NAME(ctypes.Structure):
    pass

class struct_stack_st_X509(ctypes.Structure):
    pass

ENGINE_SSL_CLIENT_CERT_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(None), POINTER_T(struct_stack_st_X509_NAME), POINTER_T(POINTER_T(struct_x509_st)), POINTER_T(POINTER_T(struct_evp_pkey_st)), POINTER_T(POINTER_T(struct_stack_st_X509)), POINTER_T(None), POINTER_T(None)))
class struct_evp_cipher_st(ctypes.Structure):
    pass

ENGINE_CIPHERS_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(POINTER_T(struct_evp_cipher_st)), POINTER_T(POINTER_T(ctypes.c_int32)), ctypes.c_int32))
class struct_env_md_st(ctypes.Structure):
    pass

ENGINE_DIGESTS_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(POINTER_T(struct_env_md_st)), POINTER_T(POINTER_T(ctypes.c_int32)), ctypes.c_int32))
ENGINE_PKEY_METHS_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(POINTER_T(None)), POINTER_T(POINTER_T(ctypes.c_int32)), ctypes.c_int32))
ENGINE_PKEY_ASN1_METHS_PTR = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(POINTER_T(None)), POINTER_T(POINTER_T(ctypes.c_int32)), ctypes.c_int32))
dyn_MEM_malloc_cb = POINTER_T(ctypes.CFUNCTYPE(POINTER_T(None)))
dyn_MEM_realloc_cb = POINTER_T(ctypes.CFUNCTYPE(POINTER_T(None), POINTER_T(None), ctypes.c_int32))
dyn_MEM_free_cb = POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None)))
class struct_st_dynamic_MEM_fns(ctypes.Structure):
    pass

struct_st_dynamic_MEM_fns._pack_ = True # source:False
struct_st_dynamic_MEM_fns._fields_ = [
    ('malloc_cb', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(None)))),
    ('realloc_cb', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(None), POINTER_T(None), ctypes.c_int32))),
    ('free_cb', POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None)))),
]

dynamic_MEM_fns = struct_st_dynamic_MEM_fns
dyn_lock_locking_cb = POINTER_T(ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32))
dyn_lock_add_lock_cb = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(ctypes.c_int32), ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32))
dyn_dynlock_create_cb = POINTER_T(ctypes.CFUNCTYPE(POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32))
dyn_dynlock_lock_cb = POINTER_T(ctypes.CFUNCTYPE(None, ctypes.c_int32, POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32))
dyn_dynlock_destroy_cb = POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32))
class struct_st_dynamic_LOCK_fns(ctypes.Structure):
    pass

struct_st_dynamic_LOCK_fns._pack_ = True # source:False
struct_st_dynamic_LOCK_fns._fields_ = [
    ('lock_locking_cb', POINTER_T(ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32))),
    ('lock_add_lock_cb', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(ctypes.c_int32), ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32))),
    ('dynlock_create_cb', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32))),
    ('dynlock_lock_cb', POINTER_T(ctypes.CFUNCTYPE(None, ctypes.c_int32, POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32))),
    ('dynlock_destroy_cb', POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None), POINTER_T(ctypes.c_char), ctypes.c_int32))),
]

dynamic_LOCK_fns = struct_st_dynamic_LOCK_fns
class struct_st_dynamic_fns(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('static_state', POINTER_T(None)),
    ('err_fns', POINTER_T(None)),
    ('ex_data_fns', POINTER_T(None)),
    ('mem_fns', dynamic_MEM_fns),
    ('lock_fns', dynamic_LOCK_fns),
     ]

dynamic_fns = struct_st_dynamic_fns
dynamic_v_check_fn = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_uint64))
dynamic_bind_engine = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(ctypes.c_char), POINTER_T(struct_st_dynamic_fns)))
class struct_err_state_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tid', CRYPTO_THREADID),
    ('err_flags', ctypes.c_int32 * 16),
    ('err_buffer', ctypes.c_uint64 * 16),
    ('err_data', POINTER_T(ctypes.c_char) * 16),
    ('err_data_flags', ctypes.c_int32 * 16),
    ('err_file', POINTER_T(ctypes.c_char) * 16),
    ('err_line', ctypes.c_int32 * 16),
    ('top', ctypes.c_int32),
    ('bottom', ctypes.c_int32),
     ]

ERR_STATE = struct_err_state_st
class struct_ERR_string_data_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('error', ctypes.c_uint64),
    ('string', POINTER_T(ctypes.c_char)),
     ]

ERR_STRING_DATA = struct_ERR_string_data_st
evp_sign_method = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_uint32), POINTER_T(None))
evp_verify_method = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(None))
class struct_evp_cipher_info_st(ctypes.Structure):
    pass

class struct_evp_cipher_ctx_st(ctypes.Structure):
    pass

struct_evp_cipher_st._pack_ = True # source:False
struct_evp_cipher_st._fields_ = [
    ('nid', ctypes.c_int32),
    ('block_size', ctypes.c_int32),
    ('key_len', ctypes.c_int32),
    ('iv_len', ctypes.c_int32),
    ('flags', ctypes.c_uint64),
    ('init', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_evp_cipher_ctx_st), POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_ubyte), ctypes.c_int32))),
    ('do_cipher', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_evp_cipher_ctx_st), POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_ubyte), ctypes.c_int32))),
    ('cleanup', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_evp_cipher_ctx_st)))),
    ('ctx_size', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('set_asn1_parameters', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_evp_cipher_ctx_st), POINTER_T(struct_asn1_type_st)))),
    ('get_asn1_parameters', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_evp_cipher_ctx_st), POINTER_T(struct_asn1_type_st)))),
    ('ctrl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_evp_cipher_ctx_st), ctypes.c_int32, ctypes.c_int32, POINTER_T(None)))),
    ('app_data', POINTER_T(None)),
]

struct_evp_cipher_info_st._pack_ = True # source:False
struct_evp_cipher_info_st._fields_ = [
    ('cipher', POINTER_T(struct_evp_cipher_st)),
    ('iv', ctypes.c_ubyte * 16),
]

EVP_CIPHER_INFO = struct_evp_cipher_info_st
class struct_evp_Encode_Ctx_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num', ctypes.c_int32),
    ('length', ctypes.c_int32),
    ('enc_data', ctypes.c_ubyte * 80),
    ('line_num', ctypes.c_int32),
    ('expect_nl', ctypes.c_int32),
     ]

EVP_ENCODE_CTX = struct_evp_Encode_Ctx_st
EVP_PBE_KEYGEN = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_evp_cipher_ctx_st), POINTER_T(ctypes.c_char), ctypes.c_int32, POINTER_T(struct_asn1_type_st), POINTER_T(struct_evp_cipher_st), POINTER_T(struct_env_md_st), ctypes.c_int32)
EVP_PKEY_gen_cb = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None))
class struct_hmac_ctx_st(ctypes.Structure):
    pass

class struct_env_md_ctx_st(ctypes.Structure):
    pass

struct_env_md_st._pack_ = True # source:False
struct_env_md_st._fields_ = [
    ('type', ctypes.c_int32),
    ('pkey_type', ctypes.c_int32),
    ('md_size', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('flags', ctypes.c_uint64),
    ('init', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_env_md_ctx_st)))),
    ('update', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_env_md_ctx_st), POINTER_T(None), ctypes.c_int32))),
    ('final', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_env_md_ctx_st), POINTER_T(ctypes.c_ubyte)))),
    ('copy', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_env_md_ctx_st), POINTER_T(struct_env_md_ctx_st)))),
    ('cleanup', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_env_md_ctx_st)))),
    ('sign', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(ctypes.c_ubyte), POINTER_T(ctypes.c_uint32), POINTER_T(None)))),
    ('verify', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(ctypes.c_ubyte), ctypes.c_uint32, POINTER_T(None)))),
    ('required_pkey_type', ctypes.c_int32 * 5),
    ('block_size', ctypes.c_int32),
    ('ctx_size', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('md_ctrl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_env_md_ctx_st), ctypes.c_int32, ctypes.c_int32, POINTER_T(None)))),
]

struct_env_md_ctx_st._pack_ = True # source:False
struct_env_md_ctx_st._fields_ = [
    ('digest', POINTER_T(struct_env_md_st)),
    ('engine', POINTER_T(None)),
    ('flags', ctypes.c_uint64),
    ('md_data', POINTER_T(None)),
    ('pctx', POINTER_T(None)),
    ('update', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_env_md_ctx_st), POINTER_T(None), ctypes.c_int32))),
]

EVP_MD_CTX = struct_env_md_ctx_st
struct_hmac_ctx_st._pack_ = True # source:False
struct_hmac_ctx_st._fields_ = [
    ('md', POINTER_T(struct_env_md_st)),
    ('md_ctx', EVP_MD_CTX),
    ('i_ctx', EVP_MD_CTX),
    ('o_ctx', EVP_MD_CTX),
    ('key_length', ctypes.c_uint32),
    ('key', ctypes.c_ubyte * 128),
    ('PADDING_0', ctypes.c_ubyte * 4),
]

HMAC_CTX = struct_hmac_ctx_st
class struct_lhash_node_st(ctypes.Structure):
    pass

struct_lhash_node_st._pack_ = True # source:False
struct_lhash_node_st._fields_ = [
    ('data', POINTER_T(None)),
    ('next', POINTER_T(struct_lhash_node_st)),
    ('hash', ctypes.c_uint64),
]

LHASH_NODE = struct_lhash_node_st
LHASH_COMP_FN_TYPE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(None)))
LHASH_HASH_FN_TYPE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None)))
LHASH_DOALL_FN_TYPE = POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None)))
LHASH_DOALL_ARG_FN_TYPE = POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None), POINTER_T(None)))
class struct_lhash_st(ctypes.Structure):
    pass

struct_lhash_st._pack_ = True # source:False
struct_lhash_st._fields_ = [
    ('b', POINTER_T(POINTER_T(struct_lhash_node_st))),
    ('comp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(None)))),
    ('hash', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None)))),
    ('num_nodes', ctypes.c_uint32),
    ('num_alloc_nodes', ctypes.c_uint32),
    ('p', ctypes.c_uint32),
    ('pmax', ctypes.c_uint32),
    ('up_load', ctypes.c_uint64),
    ('down_load', ctypes.c_uint64),
    ('num_items', ctypes.c_uint64),
    ('num_expands', ctypes.c_uint64),
    ('num_expand_reallocs', ctypes.c_uint64),
    ('num_contracts', ctypes.c_uint64),
    ('num_contract_reallocs', ctypes.c_uint64),
    ('num_hash_calls', ctypes.c_uint64),
    ('num_comp_calls', ctypes.c_uint64),
    ('num_insert', ctypes.c_uint64),
    ('num_replace', ctypes.c_uint64),
    ('num_delete', ctypes.c_uint64),
    ('num_no_delete', ctypes.c_uint64),
    ('num_retrieve', ctypes.c_uint64),
    ('num_retrieve_miss', ctypes.c_uint64),
    ('num_hash_comps', ctypes.c_uint64),
    ('error', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
]

_LHASH = struct_lhash_st
class struct_lhash_st_OPENSSL_STRING(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('dummy', ctypes.c_int32),
     ]

class struct_lhash_st_OPENSSL_CSTRING(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('dummy', ctypes.c_int32),
     ]

class struct_obj_name_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('type', ctypes.c_int32),
    ('alias', ctypes.c_int32),
    ('name', POINTER_T(ctypes.c_char)),
    ('data', POINTER_T(ctypes.c_char)),
     ]

OBJ_NAME = struct_obj_name_st
obj_cleanup_defer = None # Variable ctypes.c_int32
ASN1_INTEGER = struct_asn1_string_st
ASN1_ENUMERATED = struct_asn1_string_st
ASN1_BIT_STRING = struct_asn1_string_st
ASN1_OCTET_STRING = struct_asn1_string_st
ASN1_PRINTABLESTRING = struct_asn1_string_st
ASN1_T61STRING = struct_asn1_string_st
ASN1_IA5STRING = struct_asn1_string_st
ASN1_GENERALSTRING = struct_asn1_string_st
ASN1_UNIVERSALSTRING = struct_asn1_string_st
ASN1_BMPSTRING = struct_asn1_string_st
ASN1_UTCTIME = struct_asn1_string_st
ASN1_TIME = struct_asn1_string_st
ASN1_GENERALIZEDTIME = struct_asn1_string_st
ASN1_VISIBLESTRING = struct_asn1_string_st
ASN1_UTF8STRING = struct_asn1_string_st
ASN1_STRING = struct_asn1_string_st
ASN1_BOOLEAN = ctypes.c_int32
ASN1_NULL = ctypes.c_int32
BN_MONT_CTX = struct_bn_mont_ctx_st
class struct_bn_recp_ctx_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('N', BIGNUM),
    ('Nr', BIGNUM),
    ('num_bits', ctypes.c_int32),
    ('shift', ctypes.c_int32),
    ('flags', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

BN_RECP_CTX = struct_bn_recp_ctx_st
struct_bn_gencb_st._pack_ = True # source:False
struct_bn_gencb_st._fields_ = [
    ('ver', ctypes.c_uint32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('arg', POINTER_T(None)),
    ('cb', union_bn_gencb_st_0),
]

BN_GENCB = struct_bn_gencb_st
BUF_MEM = struct_buf_mem_st
EVP_CIPHER = struct_evp_cipher_st
struct_evp_cipher_ctx_st._pack_ = True # source:False
struct_evp_cipher_ctx_st._fields_ = [
    ('cipher', POINTER_T(struct_evp_cipher_st)),
    ('engine', POINTER_T(None)),
    ('encrypt', ctypes.c_int32),
    ('buf_len', ctypes.c_int32),
    ('oiv', ctypes.c_ubyte * 16),
    ('iv', ctypes.c_ubyte * 16),
    ('buf', ctypes.c_ubyte * 32),
    ('num', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('app_data', POINTER_T(None)),
    ('key_len', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('flags', ctypes.c_uint64),
    ('cipher_data', POINTER_T(None)),
    ('final_used', ctypes.c_int32),
    ('block_mask', ctypes.c_int32),
    ('final', ctypes.c_ubyte * 32),
]

EVP_CIPHER_CTX = struct_evp_cipher_ctx_st
EVP_MD = struct_env_md_st
EVP_PKEY = struct_evp_pkey_st
DH = struct_dh_st
DH_METHOD = struct_dh_method
DSA = struct_dsa_st
DSA_METHOD = struct_dsa_method
RSA = struct_rsa_st
RSA_METHOD = struct_rsa_meth_st
class struct_rand_meth_st(ctypes.Structure):
    pass

struct_rand_meth_st._pack_ = True # source:False
struct_rand_meth_st._fields_ = [
    ('seed', POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None), ctypes.c_int32))),
    ('bytes', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_int32))),
    ('cleanup', POINTER_T(ctypes.CFUNCTYPE(None))),
    ('add', POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None), ctypes.c_int32, ctypes.c_double))),
    ('pseudorand', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_int32))),
    ('status', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32))),
]

RAND_METHOD = struct_rand_meth_st
X509 = struct_x509_st
X509_ALGOR = struct_X509_algor_st
class struct_X509_crl_st(ctypes.Structure):
    pass

class struct_X509_crl_info_st(ctypes.Structure):
    pass

class struct_stack_st_X509_REVOKED(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

struct_X509_crl_info_st._pack_ = True # source:False
struct_X509_crl_info_st._fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('sig_alg', POINTER_T(struct_X509_algor_st)),
    ('issuer', POINTER_T(struct_X509_name_st)),
    ('lastUpdate', POINTER_T(struct_asn1_string_st)),
    ('nextUpdate', POINTER_T(struct_asn1_string_st)),
    ('revoked', POINTER_T(struct_stack_st_X509_REVOKED)),
    ('extensions', POINTER_T(struct_stack_st_X509_EXTENSION)),
    ('enc', ASN1_ENCODING),
]

struct_X509_crl_st._pack_ = True # source:False
struct_X509_crl_st._fields_ = [
    ('crl', POINTER_T(struct_X509_crl_info_st)),
    ('sig_alg', POINTER_T(struct_X509_algor_st)),
    ('signature', POINTER_T(struct_asn1_string_st)),
    ('references', ctypes.c_int32),
    ('flags', ctypes.c_int32),
    ('akid', POINTER_T(None)),
    ('idp', POINTER_T(None)),
    ('idp_flags', ctypes.c_int32),
    ('idp_reasons', ctypes.c_int32),
    ('crl_number', POINTER_T(struct_asn1_string_st)),
    ('base_crl_number', POINTER_T(struct_asn1_string_st)),
    ('sha1_hash', ctypes.c_ubyte * 20),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('issuers', POINTER_T(None)),
    ('meth', POINTER_T(None)),
    ('meth_data', POINTER_T(None)),
]

X509_CRL = struct_X509_crl_st
class struct_x509_revoked_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serialNumber', POINTER_T(struct_asn1_string_st)),
    ('revocationDate', POINTER_T(struct_asn1_string_st)),
    ('extensions', POINTER_T(struct_stack_st_X509_EXTENSION)),
    ('issuer', POINTER_T(None)),
    ('reason', ctypes.c_int32),
    ('sequence', ctypes.c_int32),
     ]

X509_REVOKED = struct_x509_revoked_st
X509_NAME = struct_X509_name_st
X509_PUBKEY = struct_X509_pubkey_st
class struct_x509_store_st(ctypes.Structure):
    pass

class struct_x509_store_ctx_st(ctypes.Structure):
    pass

class struct_stack_st_X509_OBJECT(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_stack_st_X509_LOOKUP(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_X509_VERIFY_PARAM_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('name', POINTER_T(ctypes.c_char)),
    ('check_time', ctypes.c_int64),
    ('inh_flags', ctypes.c_uint64),
    ('flags', ctypes.c_uint64),
    ('purpose', ctypes.c_int32),
    ('trust', ctypes.c_int32),
    ('depth', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('policies', POINTER_T(struct_stack_st_ASN1_OBJECT)),
     ]

class struct_stack_st_X509_CRL(ctypes.Structure):
    pass

struct_x509_store_st._pack_ = True # source:False
struct_x509_store_st._fields_ = [
    ('cache', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('objs', POINTER_T(struct_stack_st_X509_OBJECT)),
    ('get_cert_methods', POINTER_T(struct_stack_st_X509_LOOKUP)),
    ('param', POINTER_T(struct_X509_VERIFY_PARAM_st)),
    ('verify', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('verify_cb', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('get_issuer', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(POINTER_T(struct_x509_st)), POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_x509_st)))),
    ('check_issued', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_x509_st), POINTER_T(struct_x509_st)))),
    ('check_revocation', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('get_crl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(POINTER_T(struct_X509_crl_st)), POINTER_T(struct_x509_st)))),
    ('check_crl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_crl_st)))),
    ('cert_crl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_crl_st), POINTER_T(struct_x509_st)))),
    ('lookup_certs', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(struct_stack_st_X509), POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_name_st)))),
    ('lookup_crls', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(struct_stack_st_X509_CRL), POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_name_st)))),
    ('cleanup', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('ex_data', CRYPTO_EX_DATA),
    ('references', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
]

X509_STORE = struct_x509_store_st
struct_stack_st_X509._pack_ = True # source:False
struct_stack_st_X509._fields_ = [
    ('stack', _STACK),
]

struct_stack_st_X509_CRL._pack_ = True # source:False
struct_stack_st_X509_CRL._fields_ = [
    ('stack', _STACK),
]

struct_x509_store_ctx_st._pack_ = True # source:False
struct_x509_store_ctx_st._fields_ = [
    ('ctx', POINTER_T(struct_x509_store_st)),
    ('current_method', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('cert', POINTER_T(struct_x509_st)),
    ('untrusted', POINTER_T(struct_stack_st_X509)),
    ('crls', POINTER_T(struct_stack_st_X509_CRL)),
    ('param', POINTER_T(struct_X509_VERIFY_PARAM_st)),
    ('other_ctx', POINTER_T(None)),
    ('verify', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('verify_cb', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('get_issuer', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(POINTER_T(struct_x509_st)), POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_x509_st)))),
    ('check_issued', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_x509_st), POINTER_T(struct_x509_st)))),
    ('check_revocation', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('get_crl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(POINTER_T(struct_X509_crl_st)), POINTER_T(struct_x509_st)))),
    ('check_crl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_crl_st)))),
    ('cert_crl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_crl_st), POINTER_T(struct_x509_st)))),
    ('check_policy', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('lookup_certs', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(struct_stack_st_X509), POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_name_st)))),
    ('lookup_crls', POINTER_T(ctypes.CFUNCTYPE(POINTER_T(struct_stack_st_X509_CRL), POINTER_T(struct_x509_store_ctx_st), POINTER_T(struct_X509_name_st)))),
    ('cleanup', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_store_ctx_st)))),
    ('valid', ctypes.c_int32),
    ('last_untrusted', ctypes.c_int32),
    ('chain', POINTER_T(struct_stack_st_X509)),
    ('tree', POINTER_T(None)),
    ('explicit_policy', ctypes.c_int32),
    ('error_depth', ctypes.c_int32),
    ('error', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('current_cert', POINTER_T(struct_x509_st)),
    ('current_issuer', POINTER_T(struct_x509_st)),
    ('current_crl', POINTER_T(struct_X509_crl_st)),
    ('current_crl_score', ctypes.c_int32),
    ('current_reasons', ctypes.c_uint32),
    ('parent', POINTER_T(struct_x509_store_ctx_st)),
    ('ex_data', CRYPTO_EX_DATA),
]

X509_STORE_CTX = struct_x509_store_ctx_st
class struct_pkcs8_priv_key_info_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('broken', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('version', POINTER_T(struct_asn1_string_st)),
    ('pkeyalg', POINTER_T(struct_X509_algor_st)),
    ('pkey', POINTER_T(struct_asn1_type_st)),
    ('attributes', POINTER_T(struct_stack_st_X509_ATTRIBUTE)),
     ]

PKCS8_PRIV_KEY_INFO = struct_pkcs8_priv_key_info_st
CRYPTO_EX_new = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(None), POINTER_T(struct_crypto_ex_data_st), ctypes.c_int32, ctypes.c_int64, POINTER_T(None))
CRYPTO_EX_free = ctypes.CFUNCTYPE(None, POINTER_T(None), POINTER_T(None), POINTER_T(struct_crypto_ex_data_st), ctypes.c_int32, ctypes.c_int64, POINTER_T(None))
CRYPTO_EX_dup = ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_crypto_ex_data_st), POINTER_T(struct_crypto_ex_data_st), POINTER_T(None), ctypes.c_int32, ctypes.c_int64, POINTER_T(None))
class struct_pkcs7_issuer_and_serial_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('issuer', POINTER_T(struct_X509_name_st)),
    ('serial', POINTER_T(struct_asn1_string_st)),
     ]

PKCS7_ISSUER_AND_SERIAL = struct_pkcs7_issuer_and_serial_st
class struct_pkcs7_signer_info_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('issuer_and_serial', POINTER_T(struct_pkcs7_issuer_and_serial_st)),
    ('digest_alg', POINTER_T(struct_X509_algor_st)),
    ('auth_attr', POINTER_T(struct_stack_st_X509_ATTRIBUTE)),
    ('digest_enc_alg', POINTER_T(struct_X509_algor_st)),
    ('enc_digest', POINTER_T(struct_asn1_string_st)),
    ('unauth_attr', POINTER_T(struct_stack_st_X509_ATTRIBUTE)),
    ('pkey', POINTER_T(struct_evp_pkey_st)),
     ]

PKCS7_SIGNER_INFO = struct_pkcs7_signer_info_st
class struct_stack_st_PKCS7_SIGNER_INFO(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_pkcs7_recip_info_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('issuer_and_serial', POINTER_T(struct_pkcs7_issuer_and_serial_st)),
    ('key_enc_algor', POINTER_T(struct_X509_algor_st)),
    ('enc_key', POINTER_T(struct_asn1_string_st)),
    ('cert', POINTER_T(struct_x509_st)),
     ]

PKCS7_RECIP_INFO = struct_pkcs7_recip_info_st
class struct_stack_st_PKCS7_RECIP_INFO(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_pkcs7_signed_st(ctypes.Structure):
    pass

class struct_pkcs7_st(ctypes.Structure):
    pass

class union_pkcs7_st_0(ctypes.Union):
    pass

class struct_pkcs7_encrypted_st(ctypes.Structure):
    pass

class struct_pkcs7_enc_content_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('content_type', POINTER_T(struct_asn1_object_st)),
    ('algorithm', POINTER_T(struct_X509_algor_st)),
    ('enc_data', POINTER_T(struct_asn1_string_st)),
    ('cipher', POINTER_T(struct_evp_cipher_st)),
     ]

struct_pkcs7_encrypted_st._pack_ = True # source:False
struct_pkcs7_encrypted_st._fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('enc_data', POINTER_T(struct_pkcs7_enc_content_st)),
]

class struct_pkcs7_signedandenveloped_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('md_algs', POINTER_T(struct_stack_st_X509_ALGOR)),
    ('cert', POINTER_T(struct_stack_st_X509)),
    ('crl', POINTER_T(struct_stack_st_X509_CRL)),
    ('signer_info', POINTER_T(struct_stack_st_PKCS7_SIGNER_INFO)),
    ('enc_data', POINTER_T(struct_pkcs7_enc_content_st)),
    ('recipientinfo', POINTER_T(struct_stack_st_PKCS7_RECIP_INFO)),
     ]

class struct_pkcs7_enveloped_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('recipientinfo', POINTER_T(struct_stack_st_PKCS7_RECIP_INFO)),
    ('enc_data', POINTER_T(struct_pkcs7_enc_content_st)),
     ]

class struct_pkcs7_digest_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('md', POINTER_T(struct_X509_algor_st)),
    ('contents', POINTER_T(struct_pkcs7_st)),
    ('digest', POINTER_T(struct_asn1_string_st)),
     ]

union_pkcs7_st_0._pack_ = True # source:False
union_pkcs7_st_0._fields_ = [
    ('ptr', POINTER_T(ctypes.c_char)),
    ('data', POINTER_T(struct_asn1_string_st)),
    ('sign', POINTER_T(struct_pkcs7_signed_st)),
    ('enveloped', POINTER_T(struct_pkcs7_enveloped_st)),
    ('signed_and_enveloped', POINTER_T(struct_pkcs7_signedandenveloped_st)),
    ('digest', POINTER_T(struct_pkcs7_digest_st)),
    ('encrypted', POINTER_T(struct_pkcs7_encrypted_st)),
    ('other', POINTER_T(struct_asn1_type_st)),
]

struct_pkcs7_st._pack_ = True # source:False
struct_pkcs7_st._fields_ = [
    ('asn1', POINTER_T(ctypes.c_ubyte)),
    ('length', ctypes.c_int64),
    ('state', ctypes.c_int32),
    ('detached', ctypes.c_int32),
    ('type', POINTER_T(struct_asn1_object_st)),
    ('d', union_pkcs7_st_0),
]

struct_pkcs7_signed_st._pack_ = True # source:False
struct_pkcs7_signed_st._fields_ = [
    ('version', POINTER_T(struct_asn1_string_st)),
    ('md_algs', POINTER_T(struct_stack_st_X509_ALGOR)),
    ('cert', POINTER_T(struct_stack_st_X509)),
    ('crl', POINTER_T(struct_stack_st_X509_CRL)),
    ('signer_info', POINTER_T(struct_stack_st_PKCS7_SIGNER_INFO)),
    ('contents', POINTER_T(struct_pkcs7_st)),
]

PKCS7_SIGNED = struct_pkcs7_signed_st
PKCS7_ENC_CONTENT = struct_pkcs7_enc_content_st
PKCS7_ENVELOPE = struct_pkcs7_enveloped_st
PKCS7_SIGN_ENVELOPE = struct_pkcs7_signedandenveloped_st
PKCS7_DIGEST = struct_pkcs7_digest_st
PKCS7_ENCRYPT = struct_pkcs7_encrypted_st
PKCS7 = struct_pkcs7_st
class struct_stack_st_PKCS7(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_rc4_key_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_uint32),
    ('y', ctypes.c_uint32),
    ('data', ctypes.c_uint32 * 256),
     ]

RC4_KEY = struct_rc4_key_st
class struct_rsa_pss_params_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('hashAlgorithm', POINTER_T(struct_X509_algor_st)),
    ('maskGenAlgorithm', POINTER_T(struct_X509_algor_st)),
    ('saltLength', POINTER_T(struct_asn1_string_st)),
    ('trailerField', POINTER_T(struct_asn1_string_st)),
     ]

RSA_PSS_PARAMS = struct_rsa_pss_params_st
OPENSSL_STRING = POINTER_T(ctypes.c_char)
OPENSSL_CSTRING = POINTER_T(ctypes.c_char)
class struct_stack_st_OPENSSL_STRING(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

OPENSSL_BLOCK = POINTER_T(None)
class struct_stack_st_OPENSSL_BLOCK(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_SHAstate_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('h0', ctypes.c_uint32),
    ('h1', ctypes.c_uint32),
    ('h2', ctypes.c_uint32),
    ('h3', ctypes.c_uint32),
    ('h4', ctypes.c_uint32),
    ('Nl', ctypes.c_uint32),
    ('Nh', ctypes.c_uint32),
    ('data', ctypes.c_uint32 * 16),
    ('num', ctypes.c_uint32),
     ]

SHA_CTX = struct_SHAstate_st
class struct_SHA256state_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('h', ctypes.c_uint32 * 8),
    ('Nl', ctypes.c_uint32),
    ('Nh', ctypes.c_uint32),
    ('data', ctypes.c_uint32 * 16),
    ('num', ctypes.c_uint32),
    ('md_len', ctypes.c_uint32),
     ]

SHA256_CTX = struct_SHA256state_st
class struct_SHA512state_st(ctypes.Structure):
    pass

class union_SHA512state_st_0(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('d', ctypes.c_uint64 * 16),
    ('p', ctypes.c_ubyte * 128),
     ]

struct_SHA512state_st._pack_ = True # source:False
struct_SHA512state_st._fields_ = [
    ('h', ctypes.c_uint64 * 8),
    ('Nl', ctypes.c_uint64),
    ('Nh', ctypes.c_uint64),
    ('u', union_SHA512state_st_0),
    ('num', ctypes.c_uint32),
    ('md_len', ctypes.c_uint32),
]

SHA512_CTX = struct_SHA512state_st
class struct_stack_st_UI_STRING(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]


# values for enumeration 'UI_string_types'
UI_string_types = ctypes.c_int # enum
class struct_X509_objects_st(ctypes.Structure):
    pass

struct_X509_objects_st._pack_ = True # source:False
struct_X509_objects_st._fields_ = [
    ('nid', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('a2i', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32))),
    ('i2a', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32))),
]

X509_OBJECTS = struct_X509_objects_st
X509_ALGORS = struct_stack_st_X509_ALGOR
X509_VAL = struct_X509_val_st
class struct_X509_sig_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('algor', POINTER_T(struct_X509_algor_st)),
    ('digest', POINTER_T(struct_asn1_string_st)),
     ]

X509_SIG = struct_X509_sig_st
class struct_X509_name_entry_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('object', POINTER_T(struct_asn1_object_st)),
    ('value', POINTER_T(struct_asn1_string_st)),
    ('set', ctypes.c_int32),
    ('size', ctypes.c_int32),
     ]

X509_NAME_ENTRY = struct_X509_name_entry_st
struct_stack_st_X509_NAME._pack_ = True # source:False
struct_stack_st_X509_NAME._fields_ = [
    ('stack', _STACK),
]

class struct_X509_extension_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('object', POINTER_T(struct_asn1_object_st)),
    ('critical', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('value', POINTER_T(struct_asn1_string_st)),
     ]

X509_EXTENSION = struct_X509_extension_st
X509_EXTENSIONS = struct_stack_st_X509_EXTENSION
class struct_x509_attributes_st(ctypes.Structure):
    pass

class union_x509_attributes_st_0(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('ptr', POINTER_T(ctypes.c_char)),
    ('set', POINTER_T(struct_stack_st_ASN1_TYPE)),
    ('single', POINTER_T(struct_asn1_type_st)),
     ]

struct_x509_attributes_st._pack_ = True # source:False
struct_x509_attributes_st._fields_ = [
    ('object', POINTER_T(struct_asn1_object_st)),
    ('single', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('value', union_x509_attributes_st_0),
]

X509_ATTRIBUTE = struct_x509_attributes_st
class struct_X509_req_info_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('enc', ASN1_ENCODING),
    ('version', POINTER_T(struct_asn1_string_st)),
    ('subject', POINTER_T(struct_X509_name_st)),
    ('pubkey', POINTER_T(struct_X509_pubkey_st)),
    ('attributes', POINTER_T(struct_stack_st_X509_ATTRIBUTE)),
     ]

X509_REQ_INFO = struct_X509_req_info_st
class struct_X509_req_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('req_info', POINTER_T(struct_X509_req_info_st)),
    ('sig_alg', POINTER_T(struct_X509_algor_st)),
    ('signature', POINTER_T(struct_asn1_string_st)),
    ('references', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

X509_REQ = struct_X509_req_st
X509_CINF = struct_x509_cinf_st
X509_CERT_AUX = struct_x509_cert_aux_st
class struct_x509_trust_st(ctypes.Structure):
    pass

struct_x509_trust_st._pack_ = True # source:False
struct_x509_trust_st._fields_ = [
    ('trust', ctypes.c_int32),
    ('flags', ctypes.c_int32),
    ('check_trust', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_trust_st), POINTER_T(struct_x509_st), ctypes.c_int32))),
    ('name', POINTER_T(ctypes.c_char)),
    ('arg1', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('arg2', POINTER_T(None)),
]

X509_TRUST = struct_x509_trust_st
class struct_stack_st_X509_TRUST(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_x509_cert_pair_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('forward', POINTER_T(struct_x509_st)),
    ('reverse', POINTER_T(struct_x509_st)),
     ]

X509_CERT_PAIR = struct_x509_cert_pair_st
X509_CRL_INFO = struct_X509_crl_info_st
class struct_private_key_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('enc_algor', POINTER_T(struct_X509_algor_st)),
    ('enc_pkey', POINTER_T(struct_asn1_string_st)),
    ('dec_pkey', POINTER_T(struct_evp_pkey_st)),
    ('key_length', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('key_data', POINTER_T(ctypes.c_char)),
    ('key_free', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
    ('cipher', EVP_CIPHER_INFO),
    ('references', ctypes.c_int32),
    ('PADDING_3', ctypes.c_ubyte * 4),
     ]

X509_PKEY = struct_private_key_st
class struct_X509_info_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x509', POINTER_T(struct_x509_st)),
    ('crl', POINTER_T(struct_X509_crl_st)),
    ('x_pkey', POINTER_T(struct_private_key_st)),
    ('enc_cipher', EVP_CIPHER_INFO),
    ('enc_len', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('enc_data', POINTER_T(ctypes.c_char)),
    ('references', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
     ]

X509_INFO = struct_X509_info_st
class struct_stack_st_X509_INFO(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

class struct_Netscape_spkac_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pubkey', POINTER_T(struct_X509_pubkey_st)),
    ('challenge', POINTER_T(struct_asn1_string_st)),
     ]

NETSCAPE_SPKAC = struct_Netscape_spkac_st
class struct_Netscape_spki_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('spkac', POINTER_T(struct_Netscape_spkac_st)),
    ('sig_algor', POINTER_T(struct_X509_algor_st)),
    ('signature', POINTER_T(struct_asn1_string_st)),
     ]

NETSCAPE_SPKI = struct_Netscape_spki_st
class struct_Netscape_certificate_sequence(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('type', POINTER_T(struct_asn1_object_st)),
    ('certs', POINTER_T(struct_stack_st_X509)),
     ]

NETSCAPE_CERT_SEQUENCE = struct_Netscape_certificate_sequence
class struct_PBEPARAM_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('salt', POINTER_T(struct_asn1_string_st)),
    ('iter', POINTER_T(struct_asn1_string_st)),
     ]

PBEPARAM = struct_PBEPARAM_st
class struct_PBE2PARAM_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('keyfunc', POINTER_T(struct_X509_algor_st)),
    ('encryption', POINTER_T(struct_X509_algor_st)),
     ]

PBE2PARAM = struct_PBE2PARAM_st
class struct_PBKDF2PARAM_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('salt', POINTER_T(struct_asn1_type_st)),
    ('iter', POINTER_T(struct_asn1_string_st)),
    ('keylength', POINTER_T(struct_asn1_string_st)),
    ('prf', POINTER_T(struct_X509_algor_st)),
     ]

PBKDF2PARAM = struct_PBKDF2PARAM_st
class struct_x509_file_st(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_paths', ctypes.c_int32),
    ('num_alloced', ctypes.c_int32),
    ('paths', POINTER_T(POINTER_T(ctypes.c_char))),
    ('path_type', POINTER_T(ctypes.c_int32)),
     ]

X509_CERT_FILE_CTX = struct_x509_file_st
class struct_x509_object_st(ctypes.Structure):
    pass

class union_x509_object_st_0(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('ptr', POINTER_T(ctypes.c_char)),
    ('x509', POINTER_T(struct_x509_st)),
    ('crl', POINTER_T(struct_X509_crl_st)),
    ('pkey', POINTER_T(struct_evp_pkey_st)),
     ]

struct_x509_object_st._pack_ = True # source:False
struct_x509_object_st._fields_ = [
    ('type', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('data', union_x509_object_st_0),
]

X509_OBJECT = struct_x509_object_st
class struct_x509_lookup_st(ctypes.Structure):
    pass

class struct_x509_lookup_method_st(ctypes.Structure):
    pass

struct_x509_lookup_method_st._pack_ = True # source:False
struct_x509_lookup_method_st._fields_ = [
    ('name', POINTER_T(ctypes.c_char)),
    ('new_item', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st)))),
    ('free', POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(struct_x509_lookup_st)))),
    ('init', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st)))),
    ('shutdown', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st)))),
    ('ctrl', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st), ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int64, POINTER_T(POINTER_T(ctypes.c_char))))),
    ('get_by_subject', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st), ctypes.c_int32, POINTER_T(struct_X509_name_st), POINTER_T(struct_x509_object_st)))),
    ('get_by_issuer_serial', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st), ctypes.c_int32, POINTER_T(struct_X509_name_st), POINTER_T(struct_asn1_string_st), POINTER_T(struct_x509_object_st)))),
    ('get_by_fingerprint', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st), ctypes.c_int32, POINTER_T(ctypes.c_ubyte), ctypes.c_int32, POINTER_T(struct_x509_object_st)))),
    ('get_by_alias', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(struct_x509_lookup_st), ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_int32, POINTER_T(struct_x509_object_st)))),
]

struct_x509_lookup_st._pack_ = True # source:False
struct_x509_lookup_st._fields_ = [
    ('init', ctypes.c_int32),
    ('skip', ctypes.c_int32),
    ('method', POINTER_T(struct_x509_lookup_method_st)),
    ('method_data', POINTER_T(ctypes.c_char)),
    ('store_ctx', POINTER_T(struct_x509_store_st)),
]

X509_LOOKUP = struct_x509_lookup_st
X509_LOOKUP_METHOD = struct_x509_lookup_method_st
X509_VERIFY_PARAM = struct_X509_VERIFY_PARAM_st
class struct_stack_st_X509_VERIFY_PARAM(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stack', _STACK),
     ]

FILE = struct__IO_FILE
__FILE = struct__IO_FILE
va_list = ctypes.c_int32
off_t = ctypes.c_int64
ssize_t = ctypes.c_int64
fpos_t = struct_c__SA__G_fpos_t
stdin = POINTER_T(struct__IO_FILE) # Variable POINTER_T(struct__IO_FILE)
stdout = POINTER_T(struct__IO_FILE) # Variable POINTER_T(struct__IO_FILE)
stderr = POINTER_T(struct__IO_FILE) # Variable POINTER_T(struct__IO_FILE)
class union_c__UA___WAIT_STATUS(ctypes.Union):
    pass

class union_wait(ctypes.Union):
    pass

class struct_wait_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__w_stopval', ctypes.c_uint32, 8),
    ('__w_stopsig', ctypes.c_uint32, 8),
    ('_2', ctypes.c_uint32, 16),
     ]

class struct_wait_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__w_termsig', ctypes.c_uint32, 7),
    ('__w_coredump', ctypes.c_uint32, 1),
    ('__w_retcode', ctypes.c_uint32, 8),
    ('_3', ctypes.c_uint32, 16),
     ]

union_wait._pack_ = True # source:False
union_wait._fields_ = [
    ('w_status', ctypes.c_int32),
    ('__wait_terminated', struct_wait_0),
    ('__wait_stopped', struct_wait_1),
]

union_c__UA___WAIT_STATUS._pack_ = True # source:False
union_c__UA___WAIT_STATUS._fields_ = [
    ('__uptr', POINTER_T(union_wait)),
    ('__iptr', POINTER_T(ctypes.c_int32)),
]

__WAIT_STATUS = union_c__UA___WAIT_STATUS
class struct_c__SA_div_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('quot', ctypes.c_int32),
    ('rem', ctypes.c_int32),
     ]

div_t = struct_c__SA_div_t
class struct_c__SA_ldiv_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('quot', ctypes.c_int64),
    ('rem', ctypes.c_int64),
     ]

ldiv_t = struct_c__SA_ldiv_t
class struct_c__SA_lldiv_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('quot', ctypes.c_int64),
    ('rem', ctypes.c_int64),
     ]

lldiv_t = struct_c__SA_lldiv_t
class struct_random_data(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('fptr', POINTER_T(ctypes.c_int32)),
    ('rptr', POINTER_T(ctypes.c_int32)),
    ('state', POINTER_T(ctypes.c_int32)),
    ('rand_type', ctypes.c_int32),
    ('rand_deg', ctypes.c_int32),
    ('rand_sep', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('end_ptr', POINTER_T(ctypes.c_int32)),
     ]

class struct_drand48_data(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__x', ctypes.c_uint16 * 3),
    ('__old_x', ctypes.c_uint16 * 3),
    ('__c', ctypes.c_uint16),
    ('__init', ctypes.c_uint16),
    ('__a', ctypes.c_uint64),
     ]

__compar_fn_t = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), POINTER_T(None)))
clock_t = ctypes.c_int64
time_t = ctypes.c_int64
clockid_t = ctypes.c_int32
timer_t = POINTER_T(None)
class struct_timespec(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tv_sec', ctypes.c_int64),
    ('tv_nsec', ctypes.c_int64),
     ]

class struct_tm(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tm_sec', ctypes.c_int32),
    ('tm_min', ctypes.c_int32),
    ('tm_hour', ctypes.c_int32),
    ('tm_mday', ctypes.c_int32),
    ('tm_mon', ctypes.c_int32),
    ('tm_year', ctypes.c_int32),
    ('tm_wday', ctypes.c_int32),
    ('tm_yday', ctypes.c_int32),
    ('tm_isdst', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('tm_gmtoff', ctypes.c_int64),
    ('tm_zone', POINTER_T(ctypes.c_char)),
     ]

class struct_itimerspec(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('it_interval', struct_timespec),
    ('it_value', struct_timespec),
     ]

__tzname = POINTER_T(ctypes.c_char) * 2 # Variable POINTER_T(ctypes.c_char) * 2
__daylight = None # Variable ctypes.c_int32
__timezone = None # Variable ctypes.c_int64
tzname = POINTER_T(ctypes.c_char) * 2 # Variable POINTER_T(ctypes.c_char) * 2
daylight = None # Variable ctypes.c_int32
timezone = None # Variable ctypes.c_int64
pthread_t = ctypes.c_uint64
class union_pthread_attr_t(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('__size', ctypes.c_char * 56),
    ('__align', ctypes.c_int64),
    ('PADDING_0', ctypes.c_ubyte * 48),
     ]

pthread_attr_t = union_pthread_attr_t
class struct___pthread_internal_list(ctypes.Structure):
    pass

struct___pthread_internal_list._pack_ = True # source:False
struct___pthread_internal_list._fields_ = [
    ('__prev', POINTER_T(struct___pthread_internal_list)),
    ('__next', POINTER_T(struct___pthread_internal_list)),
]

__pthread_list_t = struct___pthread_internal_list
class union_c__UA_pthread_mutex_t(ctypes.Union):
    pass

class struct___pthread_mutex_s(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__lock', ctypes.c_int32),
    ('__count', ctypes.c_uint32),
    ('__owner', ctypes.c_int32),
    ('__nusers', ctypes.c_uint32),
    ('__kind', ctypes.c_int32),
    ('__spins', ctypes.c_int16),
    ('__elision', ctypes.c_int16),
    ('__list', globals()['__pthread_list_t']),
     ]

union_c__UA_pthread_mutex_t._pack_ = True # source:False
union_c__UA_pthread_mutex_t._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', ctypes.c_char * 40),
    ('__align', ctypes.c_int64),
    ('PADDING_0', ctypes.c_ubyte * 32),
]

pthread_mutex_t = union_c__UA_pthread_mutex_t
class union_c__UA_pthread_mutexattr_t(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('__size', ctypes.c_char * 4),
    ('__align', ctypes.c_int32),
     ]

pthread_mutexattr_t = union_c__UA_pthread_mutexattr_t
class union_c__UA_pthread_cond_t(ctypes.Union):
    pass

class struct_c__UA_pthread_cond_t_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__lock', ctypes.c_int32),
    ('__futex', ctypes.c_uint32),
    ('__total_seq', ctypes.c_uint64),
    ('__wakeup_seq', ctypes.c_uint64),
    ('__woken_seq', ctypes.c_uint64),
    ('__mutex', POINTER_T(None)),
    ('__nwaiters', ctypes.c_uint32),
    ('__broadcast_seq', ctypes.c_uint32),
     ]

union_c__UA_pthread_cond_t._pack_ = True # source:False
union_c__UA_pthread_cond_t._fields_ = [
    ('__data', struct_c__UA_pthread_cond_t_0),
    ('__size', ctypes.c_char * 48),
    ('__align', ctypes.c_int64),
    ('PADDING_0', ctypes.c_ubyte * 40),
]

pthread_cond_t = union_c__UA_pthread_cond_t
class union_c__UA_pthread_condattr_t(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('__size', ctypes.c_char * 4),
    ('__align', ctypes.c_int32),
     ]

pthread_condattr_t = union_c__UA_pthread_condattr_t
pthread_key_t = ctypes.c_uint32
pthread_once_t = ctypes.c_int32
class union_c__UA_pthread_rwlock_t(ctypes.Union):
    pass

class struct_c__UA_pthread_rwlock_t_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__lock', ctypes.c_int32),
    ('__nr_readers', ctypes.c_uint32),
    ('__readers_wakeup', ctypes.c_uint32),
    ('__writer_wakeup', ctypes.c_uint32),
    ('__nr_readers_queued', ctypes.c_uint32),
    ('__nr_writers_queued', ctypes.c_uint32),
    ('__writer', ctypes.c_int32),
    ('__shared', ctypes.c_int32),
    ('__pad1', ctypes.c_uint64),
    ('__pad2', ctypes.c_uint64),
    ('__flags', ctypes.c_uint32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

union_c__UA_pthread_rwlock_t._pack_ = True # source:False
union_c__UA_pthread_rwlock_t._fields_ = [
    ('__data', struct_c__UA_pthread_rwlock_t_0),
    ('__size', ctypes.c_char * 56),
    ('__align', ctypes.c_int64),
    ('PADDING_0', ctypes.c_ubyte * 48),
]

pthread_rwlock_t = union_c__UA_pthread_rwlock_t
class union_c__UA_pthread_rwlockattr_t(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('__size', ctypes.c_char * 8),
    ('__align', ctypes.c_int64),
     ]

pthread_rwlockattr_t = union_c__UA_pthread_rwlockattr_t
pthread_spinlock_t = ctypes.c_int32
class union_c__UA_pthread_barrier_t(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('__size', ctypes.c_char * 32),
    ('__align', ctypes.c_int64),
    ('PADDING_0', ctypes.c_ubyte * 24),
     ]

pthread_barrier_t = union_c__UA_pthread_barrier_t
class union_c__UA_pthread_barrierattr_t(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('__size', ctypes.c_char * 4),
    ('__align', ctypes.c_int32),
     ]

pthread_barrierattr_t = union_c__UA_pthread_barrierattr_t
__sig_atomic_t = ctypes.c_int32
class struct_c__SA___sigset_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__val', ctypes.c_uint64 * 16),
     ]

__sigset_t = struct_c__SA___sigset_t
sys_nerr = None # Variable ctypes.c_int32
sys_errlist = POINTER_T(ctypes.c_char) * 0 # Variable POINTER_T(ctypes.c_char) * 0
class struct_timeval(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tv_sec', ctypes.c_int64),
    ('tv_usec', ctypes.c_int64),
     ]

__u_char = ctypes.c_ubyte
__u_short = ctypes.c_uint16
__u_int = ctypes.c_uint32
__u_long = ctypes.c_uint64
__int8_t = ctypes.c_byte
__uint8_t = ctypes.c_ubyte
__int16_t = ctypes.c_int16
__uint16_t = ctypes.c_uint16
__int32_t = ctypes.c_int32
__uint32_t = ctypes.c_uint32
__int64_t = ctypes.c_int64
__uint64_t = ctypes.c_uint64
__quad_t = ctypes.c_int64
__u_quad_t = ctypes.c_uint64
__dev_t = ctypes.c_uint64
__uid_t = ctypes.c_uint32
__gid_t = ctypes.c_uint32
__ino_t = ctypes.c_uint64
__ino64_t = ctypes.c_uint64
__mode_t = ctypes.c_uint32
__nlink_t = ctypes.c_uint64
__off_t = ctypes.c_int64
__off64_t = ctypes.c_int64
__pid_t = ctypes.c_int32
class struct_c__SA___fsid_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__val', ctypes.c_int32 * 2),
     ]

__fsid_t = struct_c__SA___fsid_t
__clock_t = ctypes.c_int64
__rlim_t = ctypes.c_uint64
__rlim64_t = ctypes.c_uint64
__id_t = ctypes.c_uint32
__time_t = ctypes.c_int64
__useconds_t = ctypes.c_uint32
__suseconds_t = ctypes.c_int64
__daddr_t = ctypes.c_int32
__key_t = ctypes.c_int32
__clockid_t = ctypes.c_int32
__timer_t = POINTER_T(None)
__blksize_t = ctypes.c_int64
__blkcnt_t = ctypes.c_int64
__blkcnt64_t = ctypes.c_int64
__fsblkcnt_t = ctypes.c_uint64
__fsblkcnt64_t = ctypes.c_uint64
__fsfilcnt_t = ctypes.c_uint64
__fsfilcnt64_t = ctypes.c_uint64
__fsword_t = ctypes.c_int64
__ssize_t = ctypes.c_int64
__syscall_slong_t = ctypes.c_int64
__syscall_ulong_t = ctypes.c_uint64
__loff_t = ctypes.c_int64
__qaddr_t = POINTER_T(ctypes.c_int64)
__caddr_t = POINTER_T(ctypes.c_char)
__intptr_t = ctypes.c_int64
__socklen_t = ctypes.c_uint32

# values for enumeration 'c__EA_idtype_t'
c__EA_idtype_t = ctypes.c_int # enum
idtype_t = c__EA_idtype_t
sigset_t = struct_c__SA___sigset_t
suseconds_t = ctypes.c_int64
__fd_mask = ctypes.c_int64
class struct_c__SA_fd_set(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__fds_bits', ctypes.c_int64 * 16),
     ]

fd_set = struct_c__SA_fd_set
fd_mask = ctypes.c_int64
u_char = ctypes.c_ubyte
u_short = ctypes.c_uint16
u_int = ctypes.c_uint32
u_long = ctypes.c_uint64
quad_t = ctypes.c_int64
u_quad_t = ctypes.c_uint64
fsid_t = struct_c__SA___fsid_t
loff_t = ctypes.c_int64
ino_t = ctypes.c_uint64
dev_t = ctypes.c_uint64
gid_t = ctypes.c_uint32
mode_t = ctypes.c_uint32
nlink_t = ctypes.c_uint64
uid_t = ctypes.c_uint32
pid_t = ctypes.c_int32
id_t = ctypes.c_uint32
daddr_t = ctypes.c_int32
caddr_t = POINTER_T(ctypes.c_char)
key_t = ctypes.c_int32
ulong = ctypes.c_uint64
ushort = ctypes.c_uint16
uint = ctypes.c_uint32
int8_t = ctypes.c_int8
int16_t = ctypes.c_int16
int32_t = ctypes.c_int32
int64_t = ctypes.c_int64
u_int8_t = ctypes.c_ubyte
u_int16_t = ctypes.c_uint16
u_int32_t = ctypes.c_uint32
u_int64_t = ctypes.c_uint64
register_t = ctypes.c_int64
blksize_t = ctypes.c_int64
blkcnt_t = ctypes.c_int64
fsblkcnt_t = ctypes.c_uint64
fsfilcnt_t = ctypes.c_uint64
class struct___locale_struct(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__locales', POINTER_T(None) * 13),
    ('__ctype_b', POINTER_T(ctypes.c_uint16)),
    ('__ctype_tolower', POINTER_T(ctypes.c_int32)),
    ('__ctype_toupper', POINTER_T(ctypes.c_int32)),
    ('__names', POINTER_T(ctypes.c_char) * 13),
     ]

__locale_t = POINTER_T(struct___locale_struct)
locale_t = POINTER_T(struct___locale_struct)
__all__ = \
    ['__int16_t', 'X509_REVOKED', 'struct_crypto_ex_data_func_st',
    'union_c__UA_pthread_cond_t', 'div_t', '__off64_t',
    'struct_x509_st', 'struct_x509_lookup_method_st',
    'union__ossl_old_des_ks_struct_0', '_STACK', 'struct_bf_key_st',
    'fpos_t', 'X509', 'struct_c__SA_EC_builtin_curve',
    'struct_lhash_node_st', 'dyn_dynlock_create_cb', '__FILE',
    'union_DES_ks_0', 'struct_pkcs7_signed_st',
    'struct_Netscape_spki_st', 'BIO_METHOD', 'struct_pkcs7_st',
    'EVP_ENCODE_CTX', '__suseconds_t', 'X509_SIG',
    'struct_hmac_ctx_st', 'struct_stack_st_ASN1_GENERALSTRING',
    'stderr', 'ASN1_IA5STRING', 'fsfilcnt_t', 'dynamic_v_check_fn',
    '__uint64_t', 'struct_PBKDF2PARAM_st', 'u_long', 'PKCS7_ENVELOPE',
    'PBEPARAM', 'X509_NAME_ENTRY', '__clockid_t',
    'struct_evp_cipher_info_st', 'id_t', 'dyn_MEM_malloc_cb',
    'ASN1_BIT_STRING', '_G_fpos_t', 'struct_rand_meth_st',
    'struct_stack_st_BIO', 'struct_buf_mem_st', '__u_long', 'DSA_SIG',
    'DSA', 'struct_err_state_st', 'RC4_KEY', 'pthread_t',
    'union_c__UA_pthread_barrierattr_t', 'struct_x509_store_ctx_st',
    'u_int8_t', 'ENGINE_GEN_FUNC_PTR', 'DES_cblock', '__mode_t',
    'struct_stack_st_void', 'struct_X509_pubkey_st',
    'struct_stack_st', 'union_c__UA_pthread_mutexattr_t',
    'struct_SHAstate_st', 'u_quad_t', 'daddr_t',
    'union_c__UA_pthread_rwlock_t', 'ENGINE_PKEY_ASN1_METHS_PTR',
    'struct_timeval', 'X509_OBJECTS', 'struct_c__SA___sigset_t',
    'CRYPTO_EX_DATA', '__int8_t', 'HMAC_CTX',
    'struct_ENGINE_CMD_DEFN_st', 'struct_dsa_st',
    'union_pthread_attr_t', 'pthread_barrierattr_t',
    'CRYPTO_THREADID', 'struct_stack_st_X509_NAME', 'EVP_CIPHER_CTX',
    'pid_t', 'RSA_METHOD', 'timer_t', 'struct_rsa_st',
    'struct_stack_st_X509', '__fsfilcnt64_t', 'struct_x509_trust_st',
    'dyn_MEM_free_cb', '_IO_FILE', 'struct_x509_cert_aux_st',
    'pthread_key_t', 'struct_x509_cinf_st', 'X509_PUBKEY',
    '__io_read_fn', '__loff_t', 'SHA_CTX', 'off_t', '__fsblkcnt_t',
    '__locale_t', 'ENGINE_LOAD_KEY_PTR', 'CRYPTO_EX_dup',
    'OPENSSL_BLOCK', 'union_c__SA___mbstate_t_0',
    'struct_asn1_string_st', 'ASN1_NULL', 'time_t',
    'struct_stack_st_ASN1_TYPE', 'CRYPTO_EX_new',
    'CRYPTO_EX_DATA_FUNCS', 'key_t', 'union_bn_gencb_st_0',
    'struct_pkcs7_signer_info_st', 'DH_METHOD',
    'struct_SHA256state_st', 'struct_Netscape_spkac_st',
    'struct_stack_st_UI_STRING', 'stdin', 'RSA', '__u_int', 'ssize_t',
    '__clock_t', '__fsfilcnt_t', 'struct_X509_VERIFY_PARAM_st',
    'struct_obj_name_st', 'X509_PKEY', 'evp_verify_method',
    '__time_t', 'FILE', 'pthread_mutexattr_t', 'SHA512_CTX',
    'struct_tm', 'CRYPTO_MEM_LEAK_CB', 'struct_x509_attributes_st',
    'struct_stack_st_X509_INFO', '__syscall_slong_t',
    'struct_bignum_st', '__qaddr_t', 'DES_key_schedule',
    'struct___pthread_internal_list', 'X509_CERT_PAIR', 'uid_t',
    'u_int64_t', 'ASN1_STRING', 'c__EA_idtype_t', 'sigset_t',
    'ASN1_CTX', '__int32_t', 'NETSCAPE_SPKI', 'struct_random_data',
    'struct_c__SA_lldiv_t', '__fsword_t', '__fd_mask',
    'dynamic_MEM_fns', 'struct_stack_st_ASN1_STRING_TABLE', 'clock_t',
    'struct_pkcs7_issuer_and_serial_st', '__useconds_t',
    'struct_ASN1_ENCODING_st', 'ASN1_VISIBLESTRING',
    'dynamic_LOCK_fns', 'struct_c__SA_div_t', 'struct_X509_val_st',
    'pthread_barrier_t', 'X509_LOOKUP_METHOD', 'struct_timespec',
    'BIGNUM', 'pthread_rwlock_t', 'EVP_CIPHER_INFO', 'AES_KEY',
    'PKCS7_ISSUER_AND_SERIAL', 'struct_c__UA_pthread_rwlock_t_0',
    'struct_stack_st_ASN1_INTEGER', '__pthread_list_t',
    'struct_lhash_st_OPENSSL_CSTRING', 'struct_x509_object_st',
    'pthread_attr_t', 'EVP_MD', 'uint', 'ASN1_BOOLEAN', '__rlim64_t',
    'ino_t', 'union_c__UA_pthread_condattr_t', '__daylight',
    'struct_rc4_key_st', 'struct_pkcs7_enc_content_st',
    '_shadow_DES_check_key', 'union_wait', 'OPENSSL_CSTRING',
    'dyn_dynlock_lock_cb', 'struct_x509_lookup_st',
    'ASN1_OCTET_STRING', '__blksize_t', 'struct_asn1_string_table_st',
    'ENGINE_CMD_DEFN', 'pthread_spinlock_t', 'struct_st_dynamic_fns',
    'struct_env_md_ctx_st', 'struct_stack_st_OPENSSL_STRING',
    'BIO_F_BUFFER_CTX', 'struct_rsa_meth_st', 'X509_REQ_INFO',
    'struct_pkcs7_digest_st', 'struct_pkcs7_signedandenveloped_st',
    'ERR_STATE', 'struct_bio_method_st', '__mbstate_t',
    'ASN1_ENCODING', 'BUF_MEM', 'LHASH_NODE', '__u_char', '__caddr_t',
    '__blkcnt64_t', 'struct_ECDSA_SIG_st', 'RAND_METHOD',
    'ASN1_PRINTABLESTRING', 'quad_t', 'struct_evp_pkey_st', 'tzname',
    'X509_LOOKUP', 'ASN1_UNIVERSALSTRING', 'struct_dsa_method',
    '__tzname', 'X509_OBJECT', 'pthread_cond_t', 'DH',
    'X509_CERT_AUX', '__rlim_t', 'BIO', 'nlink_t',
    'struct_c__UA_pthread_cond_t_0', '__io_seek_fn',
    'UI_string_types', 'struct_c__SA___mbstate_t', 'BIO_dummy',
    'NETSCAPE_CERT_SEQUENCE', 'union_asn1_type_st_0',
    'dyn_lock_locking_cb', 'struct_X509_sig_st', 'int8_t', 'OBJ_NAME',
    'struct___pthread_mutex_s', 'struct_lhash_st',
    'c__EA_point_conversion_form_t', 'PKCS8_PRIV_KEY_INFO',
    'X509_CRL', 'fsblkcnt_t', 'struct_DES_ks',
    'struct_pkcs7_encrypted_st', '__quad_t', '__key_t', 'X509_VAL',
    'dev_t', '__uid_t', '__uint16_t', 'LHASH_DOALL_ARG_FN_TYPE',
    'struct_bio_f_buffer_ctx_struct', 'struct_cast_key_st',
    'struct_stack_st_X509_TRUST', 'struct_lhash_st_OPENSSL_STRING',
    '__uint8_t', 'mode_t', 'PKCS7_SIGNER_INFO', 'struct_c__SA_ldiv_t',
    'point_conversion_form_t', 'EVP_PKEY', 'CRYPTO_EX_free',
    'struct_pkcs7_enveloped_st', 'ENGINE_SSL_CLIENT_CERT_PTR',
    '_ossl_old_des_cblock', 'X509_INFO', 'RSA_PSS_PARAMS',
    'bio_info_cb', 'ASN1_const_CTX', 'struct_openssl_item_st',
    'struct_x509_cert_pair_st', 'struct_X509_name_st',
    'struct_X509_objects_st', 'ldiv_t', 'PKCS7_SIGN_ENVELOPE',
    'va_list', 'pthread_once_t', 'fd_mask', 'ASN1_TYPE',
    'PKCS7_SIGNED', '__timer_t', '__ssize_t', 'BF_KEY',
    'OPENSSL_STRING', 'OPENSSL_ITEM', 'int16_t', 'BN_GENCB',
    '__sigset_t', 'X509_TRUST', 'X509_STORE',
    'struct_X509_name_entry_st', 'union_evp_pkey_st_0',
    'struct_X509_crl_info_st', 'X509_STORE_CTX',
    'struct_rsa_pss_params_st', 'ASN1_TIME', 'ENGINE_CTRL_FUNC_PTR',
    '__intptr_t', 'SHA256_CTX', 'struct_X509_algor_st', 'ushort',
    '__blkcnt_t', 'struct__ossl_old_des_ks_struct', 'clockid_t',
    'asn1_ps_func', 'BN_RECP_CTX', 'ASN1_BMPSTRING',
    'EVP_PKEY_gen_cb', 'struct_x509_file_st', 'int32_t',
    '__WAIT_STATUS', 'X509_CRL_INFO', 'dynamic_fns', 'struct_dh_st',
    'sys_nerr', 'blkcnt_t', 'i2d_of_void', 'LHASH_HASH_FN_TYPE',
    'struct_PBE2PARAM_st', 'ENGINE_GEN_INT_FUNC_PTR',
    'struct_itimerspec', 'struct_stack_st_OPENSSL_BLOCK',
    'struct_st_dynamic_LOCK_fns', 'union_c__UA_pthread_rwlockattr_t',
    'EVP_PBE_KEYGEN', '__dev_t', 'ASN1_UTCTIME',
    'dynamic_bind_engine', 'struct_aes_key_st',
    'struct_stack_st_X509_ALGOR', 'struct_crypto_ex_data_st',
    'ECDSA_SIG', 'DSA_METHOD', 'EVP_CIPHER', 'BIT_STRING_BITNAME',
    'PKCS7_RECIP_INFO', 'struct_stack_st_ASN1_OBJECT',
    'struct_stack_st_X509_VERIFY_PARAM', 'stdout', 'int64_t',
    'struct_crypto_threadid_st', 'struct_x509_revoked_st',
    'X509_VERIFY_PARAM', 'ASN1_INTEGER', 'u_short',
    'union_x509_object_st_0', '_LHASH', '_ossl_old_des_key_schedule',
    'struct_bio_st', '__fsblkcnt64_t', 'ASN1_GENERALSTRING', 'PKCS7',
    'pthread_rwlockattr_t', 'union_pkcs7_st_0',
    'struct_st_dynamic_MEM_fns', 'union_c__UA_pthread_barrier_t',
    'struct_drand48_data', '__io_write_fn', 'struct_SHA512state_st',
    'caddr_t', '__ino_t', 'X509_CINF', '_IO_lock_t', 'PKCS7_ENCRYPT',
    'NETSCAPE_SPKAC', 'idtype_t', 'struct_c__SA___fsid_t', 'u_char',
    'dyn_lock_add_lock_cb', 'pthread_mutex_t', '__int64_t',
    'ENGINE_CIPHERS_PTR', 'LHASH_DOALL_FN_TYPE', 'suseconds_t',
    'ASN1_OBJECT', 'NETSCAPE_X509', 'struct_PBEPARAM_st',
    '__timezone', 'CRYPTO_dynlock', 'pthread_condattr_t',
    'PKCS7_DIGEST', '__fsid_t', 'ERR_STRING_DATA', 'u_int16_t',
    '__uint32_t', 'fd_set', '__ino64_t', '__u_quad_t', '__u_short',
    'loff_t', 'PBE2PARAM', 'struct_evp_cipher_st', 'blksize_t',
    'struct_evp_cipher_ctx_st', 'struct__IO_marker',
    'struct_stack_st_X509_REVOKED', 'u_int32_t',
    'struct_private_key_st', 'register_t', 'ASN1_UTF8STRING',
    'dyn_MEM_realloc_cb', '_G_fpos64_t', 'struct_NETSCAPE_X509_st',
    'PBKDF2PARAM', 'struct_dh_method', '__nlink_t', '__compar_fn_t',
    'CAST_KEY', 'EC_builtin_curve', '__syscall_ulong_t',
    'struct_X509_crl_st', 'X509_ATTRIBUTE', '__off_t',
    'struct_evp_Encode_Ctx_st', '__pid_t', 'X509_ALGOR',
    'ASN1_SEQUENCE_ANY', '__id_t', 'struct_stack_st_X509_LOOKUP',
    'const_DES_cblock', 'dyn_dynlock_destroy_cb', 'ulong',
    'struct_stack_st_X509_NAME_ENTRY', 'X509_EXTENSION',
    'union_x509_attributes_st_0', 'struct_ERR_string_data_st',
    'struct_bn_recp_ctx_st', 'struct_stack_st_X509_ATTRIBUTE',
    '__io_close_fn', 'ENGINE_DIGESTS_PTR',
    'union_c__UA___WAIT_STATUS', '__codecvt_result',
    '_shadow_DES_rw_mode', 'struct_c__SA__G_fpos64_t',
    'struct___locale_struct', 'ASN1_STRING_TABLE', 'sys_errlist',
    'X509_EXTENSIONS', 'BN_MONT_CTX', 'X509_REQ',
    'struct_x509_store_st', 'X509_NAME', 'LHASH_COMP_FN_TYPE',
    '__gid_t', 'struct_pkcs7_recip_info_st', 'struct_c__SA__G_fpos_t',
    'd2i_of_void', 'struct_X509_req_info_st', '__daddr_t',
    '__sig_atomic_t', 'struct_env_md_st', 'struct_stack_st_PKCS7',
    'u_int', 'ASN1_T61STRING', 'struct_bn_mont_ctx_st',
    'struct_pkcs8_priv_key_info_st', 'struct_asn1_type_st', 'gid_t',
    'ASN1_ENUMERATED', 'daylight', 'ENGINE_PKEY_METHS_PTR',
    'struct_X509_extension_st', 'struct_stack_st_X509_CRL',
    'struct_stack_st_CRYPTO_EX_DATA_FUNCS', 'timezone',
    'union_c__UA_pthread_mutex_t', 'ASN1_GENERALIZEDTIME',
    'PKCS7_ENC_CONTENT', 'struct_c__SA_CRYPTO_dynlock', 'lldiv_t',
    'struct_asn1_ctx_st', 'EVP_MD_CTX', 'struct_asn1_object_st',
    'struct_X509_req_st', 'obj_cleanup_defer',
    'union_SHA512state_st_0', 'struct_stack_st_X509_OBJECT', 'fsid_t',
    'struct_asn1_const_ctx_st', 'struct_X509_info_st',
    'struct_stack_st_PKCS7_RECIP_INFO', 'evp_sign_method',
    'struct_Netscape_certificate_sequence', 'struct_bn_gencb_st',
    'struct_DSA_SIG_st', 'struct__IO_FILE', 'struct_c__SA_fd_set',
    'locale_t', 'X509_ALGORS', '__socklen_t',
    'struct_stack_st_PKCS7_SIGNER_INFO', 'struct_wait_1',
    'struct_wait_0', 'struct_BIT_STRING_BITNAME_st',
    'struct_stack_st_X509_EXTENSION', 'X509_CERT_FILE_CTX']
