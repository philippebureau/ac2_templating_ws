#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: gen_procedure_starter
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "9/2/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"

import argparse
import sys
import os
import re
import datetime
import pprint


# This is necessary because I want to import functions in a file called utils.py and that file is one level up
# from here
# Get the absolute path of the top level main repository
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Append the parent directory to sys.path so python searches that directory for the utils file
sys.path.append(parent_dir)
# Import the utils module (python script) one level up
try:
    import utils
except:
    print(f"Move this script up a level to execute.")
    exit("Aborting run!")


def main():

    # File Friendly timestamp
    # Tip: Take a peek in utils
    file_timestamp = ""

    # Format as human-readable string
    # Tip: Take a peek in utils
    human_readable = ""

    # ----------------------------------------------------------------------------------------------------------
    # Load the installation details YAML file
    # Tip: .. yes, you guessed it! utils
    # This is an example of the type of dictionary you should have once you load the YAML file
    payload_dict = {
        "model": "",
        "mgmt_subnet": "",
    }
    print("YAML File Contents")
    pprint.pprint(payload_dict)
    # ----------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------------------
    # Select Image
    # Consider the logic needed to set the correct image file baed on the YAML file
    # Make sure that you provide an option if the right image can't be set!
    # The img variable should a relative file path string to the needed image file

    # For now the img is a Not found graphic
    img = os.path.join(".", "images", "istockphoto-519363862-612x612.jpeg")





    # Now we need to add our calculated image file to our payload dictionary using the key "diagram"
    # Add the appropriate diagram image to the payload dictionary


    # Update the payload dictionary we will send to the template with the human readable timestamp
    # using the key "dattim:


    # Calculate configuration parameters from subnet

    # Get Gateway
    # Calculate the Management Gateway of the appliance and add it to the payload dictionary
    # key: mgmt_gw
    # Tip...you guessed it


    # Get Mask in dotted notation
    # Calculate the management subnet mask in dotted notation and add it to the payload dictionary
    # key: mgmt_mask



    # Get Appliance IP (4th Valid in subnet)
    # Calculate the management IP of the appliance and add it to the payload dictionary
    # Tip:  By convention it is the 4th valid ip of the management subnet  ..and yes... the other thing
    # key: mgmt_ip


    # ----------------------------------------------------------------------------------------------------------
    # STEP 1: CREATE JINJA2 TEMPLATE ENVIRONMENT
    # Note: in the jenv_filesystem function the default line comment is #
    #       Because # is part of the Markdown syntax we need to use something else if we
    #       are rendering Markdown otherwise our # Titles will be interpreted by Jinja as comments!


    # How would you print out all the templates available in the environment?

    # ADD DEBUGGING Just In Case if needed
    # env_obj.add_extension("jinja2.ext.debug")

    # STEP 2: LOAD TEMPLATE


    # STEP 3: RENDER TEMPLATE
    # Look at the template and make sure you understand the script variable which maps to the template variable


    # Define Parent directory (in this example we are saving into the local directory)
    other_fp = os.path.join(os.getcwd())
    # Define the filename
    # Should be something like XXX_Location_ORDR_Appliance_Installation_<file timestamp>
    filename = ""


    # Create the full path to the new file
    # Tip: keep using the os module
    procedure_fp = ""

    # Save the rendered content to the file
    # There is a utils function called save_file which takes a filepath and rendered content

    print(f"\n\nSaved installation Markdown file to {procedure_fp}\n")


# Standard call to the main() function.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script Description",
        epilog="Usage: ' python gen_procedure_starter_starter.py <payload yaml>' Example payload yaml: 'Installation_details_S2000.yml'.  "
               "To use another payload file use the -p option.",
    )

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument(
        "payload_file",
        help="YAML Payload file to use. Default: Installation_details_S2000.yml"
    )
    arguments = parser.parse_args()
    main()
