#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: utils
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "8/31/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"


import re
import os
import csv
import yaml
import json
import jinja2
import argparse
import datetime
import ipaddress
import itertools

def is_user_intf(intf):
    """
    Cisco centric interface test to see if an interface is a user interface
    (typically like 1/0/21) vs an uplink (typically like 1/1/1)
    :param intf:
    :return: boolean: true if it looks like a user interface per the pattern, false otherwise
    """

    if re.search(r".+\d\/0\/\d{1,2}", intf):
        return True
    else:
        return False


def load_json(filename):

    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{filename}'. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    return None


def load_yaml(filename):
    """
    Load a YAML file safely
    :param filename:
    :return:
    """
    with open(filename, "r") as file:
        data = yaml.safe_load(file)

    return data


def load_csv(filename):
    """
    Given a path fo a file including filename, safely opens a CSV file and returns either None if it
    cannot open the file or returns the data in the file as a list (each element of the list is a row from
    the CSV file)
    :param filename: file to open
    :return: None or list
    """

    try:
        with open(filename, 'r', encoding='utf-8-sig', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


def save_file(fn, text):
    """

    :param fn:
    :param text:
    :return:
    """
    with open(fn, "w") as f:
        f.write(text)

    return fn


def check_and_create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        return True
    return False


def lists_to_dicts(data):
    """
    Takes in a CSV file with a header row as the first row and one ore more 'data' rows and builds and returns
    a list of dictionaries
    :param data:
    :return:
    """
    headers = data[0]
    return [dict(zip(headers, row)) for row in data[1:]]


def jenv_filesystem(search_dir="templates", line_comment="#"):
    """

    RECOMMENDED when getting started!
    This assumes that there is a directory called "templates" where all the Jinja Templates .j2 files are located.

    his will load templates from a directory in the file system (templates by default)

    env = jenv_filesystem()

    If, for example, you put your templates in a directory called jinja_temps you would call this function like so:

    env = jenv_filesystem(fp="jinja_temps")

    The path can be relative or absolute. Relative paths are relative to the current working directory.

    print(env)
    <jinja2.environment.Environment object at 0x105d730d0>

    dir(env)
    ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
    '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
    '__subclasshook__', '__weakref__', '_compile', '_filter_test_common', '_generate', '_load_template', '_parse',
    '_tokenize', 'add_extension', 'auto_reload', 'autoescape', 'block_end_string', 'block_start_string',
    'bytecode_cache', 'cache', 'call_filter', 'call_test', 'code_generator_class', 'comment_end_string',
    'comment_start_string', 'compile', 'compile_expression', 'compile_templates', 'concat', 'context_class',
    'extend', 'extensions', 'filters', 'finalize', 'from_string', 'get_or_select_template', 'get_template',
    'getattr', 'getitem', 'globals', 'handle_exception', 'is_async', 'iter_extensions', 'join_path',
    'keep_trailing_newline', 'lex', 'lexer', 'line_comment_prefix', 'line_statement_prefix', 'linked_to',
    'list_templates', 'loader', 'lstrip_blocks', 'make_globals', 'newline_sequence', 'optimized', 'overlay',
    'overlayed', 'parse', 'policies', 'preprocess', 'sandboxed', 'select_template', 'shared', 'template_class',
    'tests', 'trim_blocks', 'undefined', 'variable_end_string', 'variable_start_string']

    Enable Debugging
    # env = Environment(extensions=['jinja2.ext.debug'])

    ! Generally I leave this alone to default to {% %}  I like the unambiguity
    line_statement_prefix="",

    ! Error out if
    undefined=jinja2.runtime.StrictUndefined

    :param fp: the template directory path (relative or absolute)
    :return: the jinja2 environment object containing all the templates in the provided directory
    """

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(search_dir, encoding="utf-8"),
        line_comment_prefix=line_comment,
        keep_trailing_newline=False,  # Default is False
        trim_blocks=True,  # Removes lines
        lstrip_blocks=True,
        undefined=jinja2.runtime.Undefined,  # Default is Undefined - undefined variables render as empty string
    )

    return env


def load_jtemplate(jenv_obj, template_file_name):
    """
    This function takes two arguments:
    1. A Jinja2 Environment Object
    2. A Jinja2 Template Filename
    :param jenv_obj: Jinja2 Environment Object
    :param template_file_name: Jinja2 Template Filename
    :return: template_obj which will either be the requested template object or False
    """
    template_obj = False

    try:
        template_obj = jenv_obj.get_template(template_file_name)
    except jinja2.exceptions.TemplateNotFound as fn:
        print(f"ERROR: Template {template_file_name} not found!")
        print(f"Available Templates in the Environment are:")
        for line in jenv_obj.list_templates():
            print(f"\t- {line}")
    except Exception as e:
        print(f"ERROR: {e}")

    return template_obj


def render_in_one(
    template_file_name, payload_dict, search_dir="templates", line_comment="#"
):
    """
    Inspired by:
    https://daniel.feldroy.com/posts/jinja2-quick-load-function

    This is the all-in-one version of the Jinja2 process
    1. Create environment (using the jenv_filesystem function)
    2. Load template (using the load_jtemplate function)
    3. Render template with data

    :return: rendered text as a string (class 'str')
    """

    jenv = jenv_filesystem(search_dir="templates", line_comment="#")

    jtemplate = load_jtemplate(jenv, template_file_name=template_file_name)

    # The templates must use a variable called "payload_dict"
    return jtemplate.render(cfg=payload_dict)


def get_mask_from_cidr(cidr):
    network = ipaddress.IPv4Network(cidr, strict=False)
    return str(network.netmask)


def get_first_ip(cidr):
    network = ipaddress.IPv4Network(cidr, strict=False)
    first_ip = network.network_address + 1
    return str(first_ip)


def get_fourth_ip(cidr):
    network = ipaddress.IPv4Network(cidr, strict=False)
    fourth_ip = next(itertools.islice(network.hosts(), 3, 4), None)
    return str(fourth_ip) if fourth_ip else None


def add_business_days(start_date, business_days):
    """
    This helper function takes a start date and the number of business days to add. It iterates through the calendar,
    skipping weekends, until it has counted the specified number of business days.

    :param start_date:
    :param business_days:
    :return:
    """
    end_date = start_date
    while business_days > 0:
        end_date += datetime.timedelta(days=1)
        if end_date.weekday() < 5:  # Monday to Friday are 0 to 4
            business_days -= 1
    return end_date


def calculate_future_business_date(business_days):
    """
    This is the main function that uses today's date as the starting point and calls add_business_days
    to calculate the future date.

    To use this function, simply call calculate_future_business_date with the number of business days
    you want to add to today's date. For example:

    ** perplexity
    :param business_days:
    :return:
    """
    today = datetime.date.today()
    return add_business_days(today, business_days)


def main():
    pass


# Standard call to the main() function.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script Description", epilog="Usage: ' python utils' "
    )

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    # parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',default=False)
    arguments = parser.parse_args()
    main()
