
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


from setuptools import setup, Extension

core_module = Extension(
    'strkernels.core',
    sources=[
        'strkernels/core/fixed_degree_sk.c',
        'strkernels/core/locality_improved_sk.c',
        'strkernels/core/normalizer.c',
        'strkernels/core/sqrt_diag_normalizer.c',
        'strkernels/core/str_kernel.c',
        'strkernels/core/str_kernel_matrix.c',
        'strkernels/core/subsequence_sk.c',
    ],
    include_dirs=['strkernels/core']
)

setup(
    name='strkernels',
    version='0.0.1',
    description='A Python package that implements string kernels.',
    author='Denilson Fagundes Barbosa',
    author_email='denilsonfbar@gmail.com',
    url='https://github.com/denilsonfbar/strkernels',
    ext_modules=[core_module],
    packages=['strkernels'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
