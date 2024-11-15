#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: gen_bgp_report
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
try:
    import utils
except:
    print(f"Move this script up a level to execute.")
    exit("Aborting run!")


def main():

    # Step 1: Create Environment
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

    selected_template = "bgp_report_md.j2"

    # ====  START Example of an interactive CLI to pick the template
    # What templates are available in this environment?
    # template_list = env.list_templates()

    # Print the list of templates available in the defined environment
    # which is looking at a relative path in the "templates" directory
    # for template in template_list:
    #     print(template)

    # selected_template = utils.get_template_selection(template_list)
    # print(f"You selected: {selected_template}")
    # ====  END Example of an interactive CLI to pick the template

    # Step 2: Load the template
    bgp_rpt_template = env.get_template(selected_template)

    # This is only needed to display the template in the Terminal
    bgp_rpt_template.source = open(bgp_rpt_template.filename).read()
    print(f"\n\n======= EXECUTING BGP Report Script=======")
    print(f"\nTemplate name: {bgp_rpt_template.name}")
    print(f"Template filename: {bgp_rpt_template.filename}")

    print(f"\nTemplate {selected_template} Source:")
    print(bgp_rpt_template.source)

    # Manipulate the data
    # In this case we have queried SuzieQ for a list of BGP sessions at the GDL_Campus
    # and saved the output to a JSON file for later use

    # Load the JSON file
    data = utils.load_json("GDL_bgp.json")

    # Boolean to see if all sessions are up
    all_peers_up = True
    ibgp_count = 0
    ebgp_count = 0
    for line in data:
        if "Down" in line["state"]:
            all_peers_up = False
        if line["asn"] == line["peerAsn"]:
            ibgp_count += 1
        else:
            ebgp_count += 1

    drawing_filename = f"{utils.replace_special_chars(arguments.location)}_BGP_Diagram"
    outformat = "jpg"
    utils.create_bgp_diagram(data, filename=drawing_filename, outformat=outformat)
    print(f"\nDiagram saved as {drawing_filename}.{outformat}")

    # Step 3  Render the template

    # Render the template with the BGP data
    rendered_config = bgp_rpt_template.render(
        location=arguments.location,
        bgp_list=data,
        all_peers_up=all_peers_up,
        ibgp_count=ibgp_count,
        ebgp_count=ebgp_count,
        drawing_filename=f"{drawing_filename}.{outformat}",
    )

    print("=============== RENDERED RESULT ===============")
    print(rendered_config)
    print("===============================================\n")

    filename = utils.replace_special_chars(arguments.location)
    utils.save_file(
        f"{filename}_BGP_REPORT.md",
        rendered_config,
    )


# Standard call to the main() function.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script Description",
        epilog="Usage: ' python gen_bgp_report.py' or python gen_bgp_report.py -l 'AMS Campus'",
    )

    parser.add_argument(
        "-t",
        "--title",
        help="Add Custom Title to report. Default: BGP_Report",
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
