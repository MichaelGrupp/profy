#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'pyprof'
DESCRIPTION = 'quickly profile Python scripts or entry-scripts with cProfile and snakeviz'
URL = 'https://github.com/me/myproject'
EMAIL = 'me@example.com'
AUTHOR = 'Awesome Soul'

# What packages are required for this module to be executed?
REQUIRED = [
    'snakeviz'
]

# Where the magic happens:
setup(
    name=NAME,
    version=0.1,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=['pyprof'],
    entry_points={
         'console_scripts': ['pyprof=pyprof.pyprof:main'],
    },
    install_requires=REQUIRED,
)