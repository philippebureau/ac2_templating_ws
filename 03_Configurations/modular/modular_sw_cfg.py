#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: modular_sw_cfg
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/9/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"

import argparse

import utils


def some_function():
    pass


def main():
    payload_data = utils.read_csv_file(arguments.payload_file)

    if payload_data:
        print(payload_data)

# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python modular_sw_cfg.py' ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument(
        "-p",
        "--payload_file",
        help="CSV Payload file to use",
        action="store",
        default="new_switches.csv",
    )
    arguments = parser.parse_args()
    main()
