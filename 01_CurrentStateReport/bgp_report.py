#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: bgp_report
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
from diagrams import Diagram, Edge
from diagrams.generic.network import Router

# Get the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Now you can import the module from the parent directory
import utils


def create_bgp_diagram(bgp_sessions, filename="bgp_sessions", outformat="png"):
    """
    Given a list of dictionaries in bgp_sessions with local and peer information, draw a diagram which
    shows each peering session including state and ASN
    :param bgp_sessions:
    :param filename:
    :return: Nothing but the file is saved as "filename".
    """
    with Diagram(
        "BGP Sessions",
        show=False,
        filename=filename,
        direction="LR",
        outformat=outformat,
    ):
        # Initialize an empty dictionary which will have a key and Diagram object based on each element
        # (peering session dictionary) of the list
        routers = {}

        for session in bgp_sessions:
            # Create each local nodes
            local_key = f"{session['hostname']}_{session['asn']}"
            if local_key not in routers:
                routers[local_key] = Router(
                    f"{session['hostname']}\nAS {session['asn']}"
                )

            # Create peer nodes
            peer_key = f"{session['peerHostname']}_{session['peerAsn']}"
            if peer_key not in routers:
                routers[peer_key] = Router(
                    f"{session['peerHostname']}\nAS {session['peerAsn']}"
                )

            # Create edge with session details
            edge_label = f"State: {session['state']}\nVRF: {session['vrf']}"
            routers[local_key] - Edge(label=edge_label) - routers[peer_key]


def get_template_selection(options):
    """
    Example Only - Currently Not Used
    Function to enumerate templates in the templates directory for interactive user selection
    :param options:
    :return: selected template
    """
    # Display numbered options
    for index, item in enumerate(options, start=1):
        print(f"{index}. {item}")

    # Get user input and validate
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")



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

    # selected_template = get_template_selection(template_list)
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
    create_bgp_diagram(data, filename=drawing_filename, outformat=outformat)
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

    utils.save_file(
        f"{utils.replace_special_chars(arguments.location)}_BGP_REPORT.md",
        rendered_config,
    )


# Standard call to the main() function.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script Description",
        epilog="Usage: ' python bgp_report.py' or python bgp_report.py -l 'AMS Campus'",
    )

    parser.add_argument(
        "-t",
        "--title",
        help="Add Custom Title to report",
        action="store",
        default="BGP Report",
    )
    parser.add_argument(
        "-l",
        "--location",
        help="Update location",
        action="store",
        default="GDL Campus",
    )
    arguments = parser.parse_args()
    main()
