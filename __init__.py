# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pyncptl')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pyncptl')
    _pyncptl = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyncptl', [dirname(__file__)])
        except ImportError:
            import _pyncptl
            return _pyncptl
        try:
            _mod = imp.load_module('_pyncptl', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pyncptl = swig_import_helper()
    del swig_import_helper
else:
    import _pyncptl
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def ncptl_fatal(arg1):
    return _pyncptl.ncptl_fatal(arg1)
ncptl_fatal = _pyncptl.ncptl_fatal

def ncptl_allocate_timing_flag():
    return _pyncptl.ncptl_allocate_timing_flag()
ncptl_allocate_timing_flag = _pyncptl.ncptl_allocate_timing_flag

def ncptl_reset_timing_flag(arg1):
    return _pyncptl.ncptl_reset_timing_flag(arg1)
ncptl_reset_timing_flag = _pyncptl.ncptl_reset_timing_flag

def ncptl_test_timing_flag(arg1):
    return _pyncptl.ncptl_test_timing_flag(arg1)
ncptl_test_timing_flag = _pyncptl.ncptl_test_timing_flag

def ncptl_free_timing_flag(arg1):
    return _pyncptl.ncptl_free_timing_flag(arg1)
ncptl_free_timing_flag = _pyncptl.ncptl_free_timing_flag
NCPTL_RUN_TIME_VERSION = _pyncptl.NCPTL_RUN_TIME_VERSION
PRId64 = _pyncptl.PRId64
PRIu64 = _pyncptl.PRIu64
PRIx64 = _pyncptl.PRIx64
NICS = _pyncptl.NICS
NCPTL_FUNC_NO_AGGREGATE = _pyncptl.NCPTL_FUNC_NO_AGGREGATE
NCPTL_FUNC_MEAN = _pyncptl.NCPTL_FUNC_MEAN
NCPTL_FUNC_HARMONIC_MEAN = _pyncptl.NCPTL_FUNC_HARMONIC_MEAN
NCPTL_FUNC_GEOMETRIC_MEAN = _pyncptl.NCPTL_FUNC_GEOMETRIC_MEAN
NCPTL_FUNC_MEDIAN = _pyncptl.NCPTL_FUNC_MEDIAN
NCPTL_FUNC_MAD = _pyncptl.NCPTL_FUNC_MAD
NCPTL_FUNC_STDEV = _pyncptl.NCPTL_FUNC_STDEV
NCPTL_FUNC_VARIANCE = _pyncptl.NCPTL_FUNC_VARIANCE
NCPTL_FUNC_SUM = _pyncptl.NCPTL_FUNC_SUM
NCPTL_FUNC_MINIMUM = _pyncptl.NCPTL_FUNC_MINIMUM
NCPTL_FUNC_MAXIMUM = _pyncptl.NCPTL_FUNC_MAXIMUM
NCPTL_FUNC_FINAL = _pyncptl.NCPTL_FUNC_FINAL
NCPTL_FUNC_PERCENTILE = _pyncptl.NCPTL_FUNC_PERCENTILE
NCPTL_FUNC_ONLY = _pyncptl.NCPTL_FUNC_ONLY
NCPTL_FUNC_HISTOGRAM = _pyncptl.NCPTL_FUNC_HISTOGRAM

def ncptl_init(arg1, arg2):
    return _pyncptl.ncptl_init(arg1, arg2)
ncptl_init = _pyncptl.ncptl_init

def ncptl_finalize():
    return _pyncptl.ncptl_finalize()
ncptl_finalize = _pyncptl.ncptl_finalize

def ncptl_fill_buffer(arg1, arg2, arg3):
    return _pyncptl.ncptl_fill_buffer(arg1, arg2, arg3)
ncptl_fill_buffer = _pyncptl.ncptl_fill_buffer

def ncptl_verify(arg1, arg2):
    return _pyncptl.ncptl_verify(arg1, arg2)
ncptl_verify = _pyncptl.ncptl_verify

def ncptl_permit_signal(arg1):
    return _pyncptl.ncptl_permit_signal(arg1)
ncptl_permit_signal = _pyncptl.ncptl_permit_signal

def ncptl_parse_command_line(arg1, arg2, arg3, arg4):
    return _pyncptl.ncptl_parse_command_line(arg1, arg2, arg3, arg4)
ncptl_parse_command_line = _pyncptl.ncptl_parse_command_line

def ncptl_time():
    return _pyncptl.ncptl_time()
ncptl_time = _pyncptl.ncptl_time

def ncptl_set_flag_after_usecs(arg1, arg2):
    return _pyncptl.ncptl_set_flag_after_usecs(arg1, arg2)
ncptl_set_flag_after_usecs = _pyncptl.ncptl_set_flag_after_usecs

def ncptl_udelay(arg1, arg2):
    return _pyncptl.ncptl_udelay(arg1, arg2)
ncptl_udelay = _pyncptl.ncptl_udelay

def ncptl_seed_random_task(arg1, arg2):
    return _pyncptl.ncptl_seed_random_task(arg1, arg2)
ncptl_seed_random_task = _pyncptl.ncptl_seed_random_task

def ncptl_random_task(arg1, arg2, arg3):
    return _pyncptl.ncptl_random_task(arg1, arg2, arg3)
ncptl_random_task = _pyncptl.ncptl_random_task

def ncptl_allocate_task_map(arg1):
    return _pyncptl.ncptl_allocate_task_map(arg1)
ncptl_allocate_task_map = _pyncptl.ncptl_allocate_task_map

def ncptl_point_to_task_map(arg1):
    return _pyncptl.ncptl_point_to_task_map(arg1)
ncptl_point_to_task_map = _pyncptl.ncptl_point_to_task_map

def ncptl_conditionally_copy_task_map(arg1):
    return _pyncptl.ncptl_conditionally_copy_task_map(arg1)
ncptl_conditionally_copy_task_map = _pyncptl.ncptl_conditionally_copy_task_map

def ncptl_virtual_to_physical(arg1, arg2):
    return _pyncptl.ncptl_virtual_to_physical(arg1, arg2)
ncptl_virtual_to_physical = _pyncptl.ncptl_virtual_to_physical

def ncptl_physical_to_virtual(arg1, arg2):
    return _pyncptl.ncptl_physical_to_virtual(arg1, arg2)
ncptl_physical_to_virtual = _pyncptl.ncptl_physical_to_virtual

def ncptl_assign_processor(arg1, arg2, arg3, arg4):
    return _pyncptl.ncptl_assign_processor(arg1, arg2, arg3, arg4)
ncptl_assign_processor = _pyncptl.ncptl_assign_processor

def ncptl_malloc(arg1, arg2):
    return _pyncptl.ncptl_malloc(arg1, arg2)
ncptl_malloc = _pyncptl.ncptl_malloc

def ncptl_free(arg1):
    return _pyncptl.ncptl_free(arg1)
ncptl_free = _pyncptl.ncptl_free

def ncptl_realloc(arg1, arg2, arg3):
    return _pyncptl.ncptl_realloc(arg1, arg2, arg3)
ncptl_realloc = _pyncptl.ncptl_realloc

def ncptl_malloc_message(arg1, arg2, arg3, arg4):
    return _pyncptl.ncptl_malloc_message(arg1, arg2, arg3, arg4)
ncptl_malloc_message = _pyncptl.ncptl_malloc_message

def ncptl_malloc_misaligned(arg1, arg2):
    return _pyncptl.ncptl_malloc_misaligned(arg1, arg2)
ncptl_malloc_misaligned = _pyncptl.ncptl_malloc_misaligned

def ncptl_get_message_buffer(arg1):
    return _pyncptl.ncptl_get_message_buffer(arg1)
ncptl_get_message_buffer = _pyncptl.ncptl_get_message_buffer

def ncptl_touch_data(arg1, arg2):
    return _pyncptl.ncptl_touch_data(arg1, arg2)
ncptl_touch_data = _pyncptl.ncptl_touch_data

def ncptl_touch_memory(arg1, arg2, arg3, arg4, arg5, arg6):
    return _pyncptl.ncptl_touch_memory(arg1, arg2, arg3, arg4, arg5, arg6)
ncptl_touch_memory = _pyncptl.ncptl_touch_memory

def ncptl_log_add_comment(arg1, arg2):
    return _pyncptl.ncptl_log_add_comment(arg1, arg2)
ncptl_log_add_comment = _pyncptl.ncptl_log_add_comment

def ncptl_log_open(arg1, arg2):
    return _pyncptl.ncptl_log_open(arg1, arg2)
ncptl_log_open = _pyncptl.ncptl_log_open

def ncptl_log_lookup_string(arg1, arg2):
    return _pyncptl.ncptl_log_lookup_string(arg1, arg2)
ncptl_log_lookup_string = _pyncptl.ncptl_log_lookup_string

def ncptl_log_generate_uuid():
    return _pyncptl.ncptl_log_generate_uuid()
ncptl_log_generate_uuid = _pyncptl.ncptl_log_generate_uuid

def ncptl_log_write(arg1, arg2, arg3, arg4, arg5, arg6):
    return _pyncptl.ncptl_log_write(arg1, arg2, arg3, arg4, arg5, arg6)
ncptl_log_write = _pyncptl.ncptl_log_write

def ncptl_log_write_prologue(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    return _pyncptl.ncptl_log_write_prologue(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
ncptl_log_write_prologue = _pyncptl.ncptl_log_write_prologue

def ncptl_log_write_epilogue(arg1):
    return _pyncptl.ncptl_log_write_epilogue(arg1)
ncptl_log_write_epilogue = _pyncptl.ncptl_log_write_epilogue

def ncptl_log_compute_aggregates(arg1):
    return _pyncptl.ncptl_log_compute_aggregates(arg1)
ncptl_log_compute_aggregates = _pyncptl.ncptl_log_compute_aggregates

def ncptl_log_commit_data(arg1):
    return _pyncptl.ncptl_log_commit_data(arg1)
ncptl_log_commit_data = _pyncptl.ncptl_log_commit_data

def ncptl_log_get_contents(arg1):
    return _pyncptl.ncptl_log_get_contents(arg1)
ncptl_log_get_contents = _pyncptl.ncptl_log_get_contents

def ncptl_log_close(arg1):
    return _pyncptl.ncptl_log_close(arg1)
ncptl_log_close = _pyncptl.ncptl_log_close

def ncptl_func_sqrt(arg1):
    return _pyncptl.ncptl_func_sqrt(arg1)
ncptl_func_sqrt = _pyncptl.ncptl_func_sqrt

def ncptl_dfunc_sqrt(arg1):
    return _pyncptl.ncptl_dfunc_sqrt(arg1)
ncptl_dfunc_sqrt = _pyncptl.ncptl_dfunc_sqrt

def ncptl_func_cbrt(arg1):
    return _pyncptl.ncptl_func_cbrt(arg1)
ncptl_func_cbrt = _pyncptl.ncptl_func_cbrt

def ncptl_dfunc_cbrt(arg1):
    return _pyncptl.ncptl_dfunc_cbrt(arg1)
ncptl_dfunc_cbrt = _pyncptl.ncptl_dfunc_cbrt

def ncptl_func_root(arg1, arg2):
    return _pyncptl.ncptl_func_root(arg1, arg2)
ncptl_func_root = _pyncptl.ncptl_func_root

def ncptl_dfunc_root(arg1, arg2):
    return _pyncptl.ncptl_dfunc_root(arg1, arg2)
ncptl_dfunc_root = _pyncptl.ncptl_dfunc_root

def ncptl_func_bits(arg1):
    return _pyncptl.ncptl_func_bits(arg1)
ncptl_func_bits = _pyncptl.ncptl_func_bits

def ncptl_dfunc_bits(arg1):
    return _pyncptl.ncptl_dfunc_bits(arg1)
ncptl_dfunc_bits = _pyncptl.ncptl_dfunc_bits

def ncptl_func_shift_left(arg1, arg2):
    return _pyncptl.ncptl_func_shift_left(arg1, arg2)
ncptl_func_shift_left = _pyncptl.ncptl_func_shift_left

def ncptl_dfunc_shift_left(arg1, arg2):
    return _pyncptl.ncptl_dfunc_shift_left(arg1, arg2)
ncptl_dfunc_shift_left = _pyncptl.ncptl_dfunc_shift_left

def ncptl_func_log10(arg1):
    return _pyncptl.ncptl_func_log10(arg1)
ncptl_func_log10 = _pyncptl.ncptl_func_log10

def ncptl_dfunc_log10(arg1):
    return _pyncptl.ncptl_dfunc_log10(arg1)
ncptl_dfunc_log10 = _pyncptl.ncptl_dfunc_log10

def ncptl_func_factor10(arg1):
    return _pyncptl.ncptl_func_factor10(arg1)
ncptl_func_factor10 = _pyncptl.ncptl_func_factor10

def ncptl_dfunc_factor10(arg1):
    return _pyncptl.ncptl_dfunc_factor10(arg1)
ncptl_dfunc_factor10 = _pyncptl.ncptl_dfunc_factor10

def ncptl_func_abs(arg1):
    return _pyncptl.ncptl_func_abs(arg1)
ncptl_func_abs = _pyncptl.ncptl_func_abs

def ncptl_dfunc_abs(arg1):
    return _pyncptl.ncptl_dfunc_abs(arg1)
ncptl_dfunc_abs = _pyncptl.ncptl_dfunc_abs

def ncptl_func_power(arg1, arg2):
    return _pyncptl.ncptl_func_power(arg1, arg2)
ncptl_func_power = _pyncptl.ncptl_func_power

def ncptl_dfunc_power(arg1, arg2):
    return _pyncptl.ncptl_dfunc_power(arg1, arg2)
ncptl_dfunc_power = _pyncptl.ncptl_dfunc_power

def ncptl_func_modulo(arg1, arg2):
    return _pyncptl.ncptl_func_modulo(arg1, arg2)
ncptl_func_modulo = _pyncptl.ncptl_func_modulo

def ncptl_dfunc_modulo(arg1, arg2):
    return _pyncptl.ncptl_dfunc_modulo(arg1, arg2)
ncptl_dfunc_modulo = _pyncptl.ncptl_dfunc_modulo

def ncptl_func_floor(arg1):
    return _pyncptl.ncptl_func_floor(arg1)
ncptl_func_floor = _pyncptl.ncptl_func_floor

def ncptl_dfunc_floor(arg1):
    return _pyncptl.ncptl_dfunc_floor(arg1)
ncptl_dfunc_floor = _pyncptl.ncptl_dfunc_floor

def ncptl_func_ceiling(arg1):
    return _pyncptl.ncptl_func_ceiling(arg1)
ncptl_func_ceiling = _pyncptl.ncptl_func_ceiling

def ncptl_dfunc_ceiling(arg1):
    return _pyncptl.ncptl_dfunc_ceiling(arg1)
ncptl_dfunc_ceiling = _pyncptl.ncptl_dfunc_ceiling

def ncptl_func_round(arg1):
    return _pyncptl.ncptl_func_round(arg1)
ncptl_func_round = _pyncptl.ncptl_func_round

def ncptl_dfunc_round(arg1):
    return _pyncptl.ncptl_dfunc_round(arg1)
ncptl_dfunc_round = _pyncptl.ncptl_dfunc_round

def ncptl_func_tree_parent(arg1, arg2):
    return _pyncptl.ncptl_func_tree_parent(arg1, arg2)
ncptl_func_tree_parent = _pyncptl.ncptl_func_tree_parent

def ncptl_dfunc_tree_parent(arg1, arg2):
    return _pyncptl.ncptl_dfunc_tree_parent(arg1, arg2)
ncptl_dfunc_tree_parent = _pyncptl.ncptl_dfunc_tree_parent

def ncptl_func_tree_child(arg1, arg2, arg3):
    return _pyncptl.ncptl_func_tree_child(arg1, arg2, arg3)
ncptl_func_tree_child = _pyncptl.ncptl_func_tree_child

def ncptl_dfunc_tree_child(arg1, arg2, arg3):
    return _pyncptl.ncptl_dfunc_tree_child(arg1, arg2, arg3)
ncptl_dfunc_tree_child = _pyncptl.ncptl_dfunc_tree_child

def ncptl_func_mesh_coord(arg1, arg2, arg3, arg4, arg5):
    return _pyncptl.ncptl_func_mesh_coord(arg1, arg2, arg3, arg4, arg5)
ncptl_func_mesh_coord = _pyncptl.ncptl_func_mesh_coord

def ncptl_dfunc_mesh_coord(arg1, arg2, arg3, arg4, arg5):
    return _pyncptl.ncptl_dfunc_mesh_coord(arg1, arg2, arg3, arg4, arg5)
ncptl_dfunc_mesh_coord = _pyncptl.ncptl_dfunc_mesh_coord

def ncptl_func_mesh_neighbor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    return _pyncptl.ncptl_func_mesh_neighbor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
ncptl_func_mesh_neighbor = _pyncptl.ncptl_func_mesh_neighbor

def ncptl_dfunc_mesh_neighbor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    return _pyncptl.ncptl_dfunc_mesh_neighbor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
ncptl_dfunc_mesh_neighbor = _pyncptl.ncptl_dfunc_mesh_neighbor

def ncptl_func_mesh_distance(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    return _pyncptl.ncptl_func_mesh_distance(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
ncptl_func_mesh_distance = _pyncptl.ncptl_func_mesh_distance

def ncptl_dfunc_mesh_distance(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    return _pyncptl.ncptl_dfunc_mesh_distance(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
ncptl_dfunc_mesh_distance = _pyncptl.ncptl_dfunc_mesh_distance

def ncptl_func_knomial_parent(arg1, arg2, arg3):
    return _pyncptl.ncptl_func_knomial_parent(arg1, arg2, arg3)
ncptl_func_knomial_parent = _pyncptl.ncptl_func_knomial_parent

def ncptl_dfunc_knomial_parent(arg1, arg2, arg3):
    return _pyncptl.ncptl_dfunc_knomial_parent(arg1, arg2, arg3)
ncptl_dfunc_knomial_parent = _pyncptl.ncptl_dfunc_knomial_parent

def ncptl_func_knomial_child(arg1, arg2, arg3, arg4, arg5):
    return _pyncptl.ncptl_func_knomial_child(arg1, arg2, arg3, arg4, arg5)
ncptl_func_knomial_child = _pyncptl.ncptl_func_knomial_child

def ncptl_dfunc_knomial_child(arg1, arg2, arg3, arg4, arg5):
    return _pyncptl.ncptl_dfunc_knomial_child(arg1, arg2, arg3, arg4, arg5)
ncptl_dfunc_knomial_child = _pyncptl.ncptl_dfunc_knomial_child

def ncptl_func_random_uniform(arg1, arg2):
    return _pyncptl.ncptl_func_random_uniform(arg1, arg2)
ncptl_func_random_uniform = _pyncptl.ncptl_func_random_uniform

def ncptl_dfunc_random_uniform(arg1, arg2):
    return _pyncptl.ncptl_dfunc_random_uniform(arg1, arg2)
ncptl_dfunc_random_uniform = _pyncptl.ncptl_dfunc_random_uniform

def ncptl_func_random_gaussian(arg1, arg2):
    return _pyncptl.ncptl_func_random_gaussian(arg1, arg2)
ncptl_func_random_gaussian = _pyncptl.ncptl_func_random_gaussian

def ncptl_dfunc_random_gaussian(arg1, arg2):
    return _pyncptl.ncptl_dfunc_random_gaussian(arg1, arg2)
ncptl_dfunc_random_gaussian = _pyncptl.ncptl_dfunc_random_gaussian

def ncptl_func_random_poisson(arg1):
    return _pyncptl.ncptl_func_random_poisson(arg1)
ncptl_func_random_poisson = _pyncptl.ncptl_func_random_poisson

def ncptl_dfunc_random_poisson(arg1):
    return _pyncptl.ncptl_dfunc_random_poisson(arg1)
ncptl_dfunc_random_poisson = _pyncptl.ncptl_dfunc_random_poisson

def ncptl_func_random_pareto(arg1, arg2, arg3):
    return _pyncptl.ncptl_func_random_pareto(arg1, arg2, arg3)
ncptl_func_random_pareto = _pyncptl.ncptl_func_random_pareto

def ncptl_dfunc_random_pareto(arg1, arg2, arg3):
    return _pyncptl.ncptl_dfunc_random_pareto(arg1, arg2, arg3)
ncptl_dfunc_random_pareto = _pyncptl.ncptl_dfunc_random_pareto

def ncptl_func_file_data(arg1, arg2, arg3, arg4, arg5):
    return _pyncptl.ncptl_func_file_data(arg1, arg2, arg3, arg4, arg5)
ncptl_func_file_data = _pyncptl.ncptl_func_file_data

def ncptl_dfunc_file_data(arg1, arg2, arg3, arg4, arg5):
    return _pyncptl.ncptl_dfunc_file_data(arg1, arg2, arg3, arg4, arg5)
ncptl_dfunc_file_data = _pyncptl.ncptl_dfunc_file_data
# This file is compatible with both classic and new-style classes.

cvar = _pyncptl.cvar

