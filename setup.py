#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup, Command

# monkey patch because setuptools entry_points are slow as fuck
# https://github.com/ninjaaron/fast-entry_points
import fastentrypoints


# Package meta-data.
NAME = 'profy'
DESCRIPTION = 'quickly profile Python scripts or entry-scripts with cProfile and snakeviz'
URL = 'https://github.com/MichaelGrupp/profy'
EMAIL = 'michael.grupp@tum.de'
AUTHOR = 'Michael Grupp'

# What packages are required for this module to be executed?
REQUIRED = [
    'snakeviz'
]

# Where the magic happens:
setup(
    name=NAME,
    version="0.1.2",
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=['profy'],
    entry_points={
         'console_scripts': ['profy=profy.profy:main'],
    },
    install_requires=REQUIRED,
)
