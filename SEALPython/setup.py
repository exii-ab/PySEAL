import os, sys
from distutils.core import setup, Extension
from distutils import sysconfig

# Remove strict-prototypes compiler flag
cfg_vars = sysconfig.get_config_vars()
for key, value in cfg_vars.items():
    if type(value) == str:
        cfg_vars[key] = value.replace('-Wstrict-prototypes', '')

cpp_args = ['-std=c++11']

ext_modules = [
    Extension(
        'seal',
        ['wrapper.cpp'],
        include_dirs=['/usr/include/python3.7', 'pybind11/include', '/SEAL/src'],
        language='c++',
        extra_compile_args = cpp_args,
        extra_objects=['/SEAL/lib/libseal-3.4.a'],
    ),
]

setup(
    name='seal',
    version='2.3',
    author='Todd Stavish, Shashwat Kishore', 
    author_email='toddstavish@gmail.com',
    description='Python wrapper for SEAL',
    ext_modules=ext_modules,
)
