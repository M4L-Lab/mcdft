#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
from glob import glob

import setuptools
from pybind11.setup_helpers import Pybind11Extension
from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext

cpp_part = Pybind11Extension(
    '_mcdft',
    glob('src/*.cpp'),
    include_dirs=[
        'src/ext/Catch2/',
        'src/ext/pybind11/'
    ],
    language='c++')


version = "1.0.0"
maintainer = "Rajib K. Musa"
email = "irajibdu@gmail.com"
description = "Data driven Monte Carlo simulation"
url = ""
license = "MIT"
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: {}'.format(license),
    'Topic :: Scientific/Engineering :: Physics']


if __name__ == '__main__':

    setup(
        name='mcdft',
        version=version,
        author='Rajib K. Musa',
        author_email=email,
        description=description,
        long_description="Faster alloy ground state search",
        ext_modules=[cpp_part],
        install_requires=['ase',
                          'numpy',
                          'scipy',
                          'numba',
                          'pandas>=0.23',
                          'spglib>1.12.0',
                          'trainstation>=0.2',
                          'icet==2.2'],
        packages=find_packages(),
        # cmdclass={'build_ext': BuildExt},
        zip_safe=False,
        classifiers=classifiers,
        license=license,
        url=url,
    )
