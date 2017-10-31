#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import subprocess as sp
from distutils.spawn import find_executable


def main():
    parser = argparse.ArgumentParser(description="quickly profile Python scripts or entry-scripts")
    parser.add_argument("-o", "--out", help="output file name", default="out.prof")
    args, other_args = parser.parse_known_args()

    if len(other_args) == 0:
        print("please provide a command that should be profiled")
        sys.exit(1)

    # entry-script?
    full_path = find_executable(other_args[0])
    if full_path is not None:
        other_args[0] = full_path

    sp.check_call(["python", "-m", "cProfile", "-o", args.out] + other_args)
    sp.check_call(["snakeviz", args.out])


if __name__ == "__main__":
    main()
