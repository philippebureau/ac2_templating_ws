#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: gen_bgp_report_starter
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/4/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"

import argparse
import jinja2
import sys
import os


# Get the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Now you can import the module from the parent directory
import utils


def main():

    # Step 1: Create Environment
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

    # Set template file (this file should be in the templates directory under 01_CurrentStateReport
    selected_template = "bgp_report_starter_md.j2"

    # Step 2: Load the template int memory (Tip:  Slide 19) using the variable bgp_rpt_template

    # Manipulate the data
    # In this case we have queried SuzieQ for a list of BGP sessions at the GDL_Campus
    # and saved the output to a JSON file for later use

    # Load the JSON file GDL_bgp.json into a variable named data
    # Calculate a boolean all_peers_up (bool)
    # Calculate the number of iBGP sessions in ibgp_count (int)
    # Calculate the number of eBGP sessions in ebgp_count (int)
    # Tip: Take a look at the JSON file with the data and determine how you are going to process it to get the
    # values above

    data = ""

    # Define a filename
    drawing_filename = f"{utils.replace_special_chars(arguments.location)}_BGP_Diagram"
    outformat = "jpg"
    # If data is empty (the script has not been updated) don't generate an empty diagram
    if data:
        utils.create_bgp_diagram(data, filename=drawing_filename, outformat=outformat)
        print(f"\nDiagram saved as {drawing_filename}.{outformat}")

    # Step 3  Render the template
    # Render the template with the BGP data
    # Tip: Look at the template and see what template variables its expecting you to send and see if you can
    # determine the type by looking at the logic

    # Putting in try/except block so script can be run before it is complete
    try:
        rendered_config = bgp_rpt_template.render(
            drawing_filename=f"{drawing_filename}.{outformat}",
        )

        print("=============== RENDERED RESULT ===============")
        print(rendered_config)
        print("===============================================\n")

    except:
        rendered_config = ""
        print("Starter script needs to be updated!!")

    # FINAL STEP: Save the file using a filename like XXX_Location_bgp_report_starter.md
    # Tip: the utils module has a function to help removes spaces and special characters and one of the CLI
    # options is for the location
    filename = "location text with spaces removed"

    # if rendered_config is empty don't save an empty report
    if rendered_config:
        utils.save_file(
            f"{filename}_bgp_report_starter.md",
            rendered_config,
        )


# Standard call to the main() function.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script Description",
        epilog="Usage: ' python gen_bgp_report_starter.py' or python gen_bgp_report_starter.py -l 'AMS Campus'",
    )

    parser.add_argument(
        "-t",
        "--title",
        help="Add Custom Title to report. Default: bgp_report_starter",
        action="store",
        default="BGP Report",
    )
    parser.add_argument(
        "-l",
        "--location",
        help="Location Default: GDL Campus",
        action="store",
        default="GDL Campus",
    )
    arguments = parser.parse_args()
    main()
