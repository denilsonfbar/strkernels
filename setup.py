import sys
from setuptools import setup, Extension

extra_compile_args = []
extra_link_args = []

if sys.platform == 'win32':
    extra_compile_args = ['/openmp']
else:
    extra_compile_args = ['-fopenmp']
    extra_link_args = ['-fopenmp']

core_module = Extension(
    'strkernels.libcore',
    sources=[
        'strkernels/core/fixed_degree_sk.c',
        'strkernels/core/locality_improved_sk.c',
        'strkernels/core/normalizer.c',
        'strkernels/core/sqrt_diag_normalizer.c',
        'strkernels/core/str_kernel.c',
        'strkernels/core/str_kernel_matrix.c',
        'strkernels/core/subsequence_sk.c',
    ],
    include_dirs=['strkernels/core'],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args
)

setup(
    ext_modules=[core_module]
)
