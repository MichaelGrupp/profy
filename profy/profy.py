#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: Michael Grupp (github.com/MichaelGrupp/profy)

import sys
import argparse
import subprocess as sp
from distutils.spawn import find_executable

# custom help string because argparse's automatic one is useless here
usage_str = "profy cmd [cmd_args]"
help_msg = usage_str + '''

quickly profile Python scripts or entry-scripts
source: github.com/MichaelGrupp/profy

profiles a Python script or entry-point executable with cProfile
and visualizes the results in a browser with snakeviz

cmd             Python script or entry-point executable
cmd_args        any (optional) command line arguments for cmd

Options:
--profy_help    show this help message and exit
--profy_out     path to save the .prof file (default: out.prof)
'''


def main():
    # don't include default -h / --help
    parser = argparse.ArgumentParser(
        description="quickly profile Python scripts or entry-scripts",
        usage=help_msg,
        add_help=False
        )
    parser.add_argument("--profy_out", default="out.prof")
    parser.add_argument("--profy_help", action="store_true")
    args, other_args = parser.parse_known_args()

    if args.profy_help:
        parser.print_usage()
        sys.exit(0)

    if len(other_args) == 0:
        print("please provide a command that should be profiled" 
              "\n(see profy --profy_help)")
        sys.exit(1)

    # entry-script?
    full_path = find_executable(other_args[0])
    if full_path is not None:
        other_args[0] = full_path

    try:
        sp.check_call(["python", "-m", "cProfile", "-o", args.profy_out] + other_args)
        sp.call(["snakeviz", args.profy_out])
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
