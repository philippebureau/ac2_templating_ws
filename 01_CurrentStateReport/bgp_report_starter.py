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


def main():

    # Step 1: Create Environment
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

    # Set template file (this file should be in the templates directory under 01_CurrentStateReport
    selected_template = "bgp_report_md.j2"

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



    # Define a filename
    drawing_filename = f"{utils.replace_special_chars(arguments.location)}_BGP_Diagram"
    outformat = "jpg"
    create_bgp_diagram(data, filename=drawing_filename, outformat=outformat)
    print(f"\nDiagram saved as {drawing_filename}.{outformat}")

    # Step 3  Render the template
    # Render the template with the BGP data
    # Tip: Look at the template and see what template variables its expecting you to send and see if you can
    # determine the type by looking at the logic

    rendered_config = bgp_rpt_template.render(





        drawing_filename=f"{drawing_filename}.{outformat}",
    )

    print("=============== RENDERED RESULT ===============")
    print(rendered_config)
    print("===============================================\n")

    # FINAL STEP: Save the file using a filename like XXXLocation_BGP_REPORT.md
    utils.save_file(
        f"{ }_BGP_REPORT.md",
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
