#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: gen_new_vlan_cr.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/11/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"

import argparse
import os
import sys

# This is necessary because I want to import functions in a file called utils.py and that file is one level up
# from here
# Get the absolute path of the top level main repository
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Append the parent directory to sys.path so python searches that directory for the utils file
sys.path.append(parent_dir)
# Import the utils module (python script) one level up
import utils

def some_function():
    pass


def main():

    payload_data = utils.load_csv(arguments.payload_file)

    # Turn payload data into a list of dictionaries
    payload_lod = utils.lists_to_dicts(payload_data)

    # This works for one or more vlans to be defined
    for details_dict in payload_lod:

        # Assumption:  You are doing one vlan per CR
        # Is a better assumption one CR for n Vlans??  That's a business process decision.

        # Start data manipulation
        # assuming SLA is 3 days, calculate due date from day of submittal (assuming submitted today)
        requested_by_date = utils.calculate_future_business_date(3)

        # create the vlan name based on standard types (user, server, building_automation
        # is this the safest way to test for type???
        if details_dict["type"] == "user":
            vlan_name = f"USER_{details_dict['subnet_cidr']}"
        elif details_dict["type"] == "server":
            vlan_name = f"SRV_{details_dict['subnet_cidr']}"
        elif details_dict["type"] == "building_automation":
            vlan_name = f"BLDAUTO_{details_dict['subnet_cidr']}"
        else:
            print("Vlan name cannot be set. Aborting execution!")
            sys.exit()

        # Update the payload dictionary (details_dict here) for this
        details_dict.update({
            "requested_by_date": requested_by_date,
            "vlan_name": vlan_name,
            "svi_ip": utils.get_first_ip(details_dict['subnet_cidr'])
        })

        # We will use our "render in one" function to
        # - create the environment
        # - load the template
        # - render the template with our payload
        rendered_string = utils.render_in_one("new_vlan_cr_template.j2", details_dict)

        # Lets save our rendered output
        # Crafting a somewhat meaningful filename
        filename = f"{details_dict['location']}_NewVlan{details_dict['new_vlan']}_SNOW_STDCR.txt"

        # creating a full path
        cfg_file_fullpath = os.path.join(os.getcwd(), filename)

        # Saving the output to a text file
        utils.save_file(cfg_file_fullpath, rendered_string)

        print(f"Saved resulting CR file in current direcotry to {filename}")


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python gen_new_vlan_cr.py' ")

    parser.add_argument('-p', '--payload_file', help='Change details payload file', action='store', default="payload.csv")
    parser.add_argument('-c', '--create_cr', help='Create Change Request in SNOW', action='store_true', default=False)
    arguments = parser.parse_args()
    main()
