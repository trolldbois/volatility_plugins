
import ctypes

# if local wordsize is same as target, keep ctypes pointer function.
if ctypes.sizeof(ctypes.c_void_p) == 4:
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
        fake_ptr_base_type = ctypes.c_uint32
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
            _type_ = 'I'
            _subtype_ = pointee
            def _sub_addr_(self):
                return self.value
            def __repr__(self):
                return '%s(%d)'%(clsname, self.value)
            def contents(self):
                raise TypeError('This is not a ctypes pointer.')
            def __init__(self, **args):
                raise TypeError('This is not a ctypes pointer. It is not instanciable.')
        _class = type('LP_%d_%s'%(4, clsname), (_T,),{})
        ctypes._pointer_t_type_cache[clsname] = _class
        return _class


# Note: It doesn't actually matter if Py_TRACE_REF is defined, that just means
# there are more structures at the beginning, which we don't care about

class struct__PyStringObject(ctypes.Structure):
    _fields_ = [
        ('ob_refcnt', ctypes.c_size_t), # 0 Py_ssize_t = ssize_t
        ('ob_type', POINTER_T(None)), # 8
        ('ob_size', ctypes.c_size_t), # 16 Py_ssize_t = ssize_t
        ('ob_shash', ctypes.c_longlong), # 24, long long
        ('ob_sstate', ctypes.c_int), # 32
        ('ob_sval', ctypes.c_char) # 36, ['array', 1, ['char']]]
        ]

class struct__PyDictEntry(ctypes.Structure):
    _fields_ = [
        ('me_hash', ctypes.c_size_t), # 0 Py_ssize_t = ssize_t
        ('me_key', POINTER_T(struct__PyStringObject)), # 8 _PyStringObject
        ('me_value', POINTER_T(struct__PyStringObject)), # 16 _PyStringObject
        ]

