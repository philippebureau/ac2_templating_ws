#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: gen_clab_topo.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/14/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"


import os
import re
import sys
import json
import zlib
import dotenv
import base64
import argparse
import webbrowser


# This is necessary because I want to import functions in a file called utils.py and that file is one level up
# from here
# Get the absolute path of the top level main repository
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Append the parent directory to sys.path so python searches that directory for the utils file
sys.path.append(parent_dir)
# Import the utils module (python script) one level up
import utils


def generate_topology(links):
    nodes = {}
    unique_links = set()

    for link in links:
        if not re.search("Management", link["ifname"]):
            for node in [link["hostname"], link["peerHostname"]]:
                if node not in nodes:
                    nodes[node] = {"kind": "ceos", "image": "ceos:latest"}
            unique_links.add(tuple(sorted([link["hostname"], link["peerHostname"]])))

    processed_links = []
    for i, (node1, node2) in enumerate(unique_links):
        processed_links.append(
            {"endpoints": [f"{node1}:eth{i + 1}", f"{node2}:eth{i + 1}"]}
        )

    return {"name": links[0]["namespace"], "nodes": nodes, "links": processed_links}


def yaml_to_mermaid(yaml_data, dir="TD"):
    mermaid_text = f"graph {dir};\n"

    # Define a custom sorting key function
    def sort_key(item):
        name = (
            item[0] if isinstance(item, tuple) else item["endpoints"][0].split(":")[0]
        )
        if "core" in name:
            return 0
        elif "dist" in name:
            return 1
        elif "acc" in name:
            return 2
        else:
            return 3

    # Sort nodes
    sorted_nodes = sorted(yaml_data["nodes"].items(), key=sort_key)

    # Add sorted nodes to the mermaid text
    for node, data in sorted_nodes:
        mermaid_text += f"    {node};\n"

    # Sort links
    sorted_links = sorted(yaml_data["links"], key=sort_key)

    # Add sorted links to the mermaid text
    for link in sorted_links:
        endpoints = link["endpoints"]
        e1 = endpoints[0].split(":")
        e2 = endpoints[1].split(":")
        mermaid_text += f"    {e1[0]} -->|{e1[1]} To {e2[1]}| {e2[0]};\n"

    return mermaid_text


def view_mermaid_diagram(mermaid_code: str) -> None:
    """
    Takes a Mermaid diagram code as input, pushes it to the Mermaid Live Editor API,
    and opens it in the default web browser.

    Args:
        mermaid_code (str): The Mermaid diagram code/payload

    Example:
        mermaid_code = '''
        graph TD
            A[Start] --> B[Process]
            B --> C[End]
        '''
        view_mermaid_diagram(mermaid_code)
    """
    # Create the JSON state object
    state = {
        "code": mermaid_code,
        "mermaid": {"theme": "default"},
        "updateEditor": True,
        "autoSync": True,
        "updateDiagram": True,
    }

    # Convert the state to JSON and encode it
    json_state = json.dumps(state)
    json_bytes = json_state.encode("utf-8")

    # Compress the JSON using zlib
    compressed = zlib.compress(json_bytes)

    # Encode the compressed data to base64
    base64_encoded = base64.urlsafe_b64encode(compressed).decode("utf-8")

    # Create the Mermaid Live Editor URL
    base_url = "https://mermaid.live/edit"
    full_url = f"{base_url}#pako:{base64_encoded}"

    # Open the URL in the default web browser
    webbrowser.open(full_url)


def main():
    """
    Generate a Containerlab topology from a SuzieQ LLDP output
    :return:
    """

    # Initialize payload dictionary of payload to send to template
    pld = dict()

    # One option could be to have the user pick from a valid list of namespaces
    namespaces, full_response = utils.get_namespace_list()

    response = utils.get_topology(arguments.namespace)
    if response.ok:
        # Saving the response so we hae a local copy of the data, just in case
        if response.json():
            utils.save_json_payload(response.json(), f"topology_response_from_suzieq_{utils.file_timestamp()}.json")
    else:
        print(response)
        exit(
            f"\n\nAborting Run! Cannot access SuzieQ API! Status Code: "
            f"{response.status_code} Reason: {response.reason} "
            f"\nPlease make sure you have an .env file at the top level of your repository and a valdi token in "
            f"the environment variable SQ_API_TOKEN. \nRename .env_sample to .env\n\n"
        )

    pld.update({"name": f"{arguments.namespace}_clab_topology"})
    pld.update({"kind": "ceos"})
    pld.update({"image": "ceos:latest"})

    # Generate the topology data
    topology_data = generate_topology(response.json())

    # Render the Jinja2 template
    clab_topology = utils.render_in_one("lldp_topology_template.j2", topology_data, search_dir=".")

    # Optionally, save the YAML topology to a file
    filename = f"{topology_data['name']}.clab.yml"
    with open(filename, "w") as f:
        f.write(clab_topology)

    print(
        f"\nContainerlab Topology file saved to {filename} in current working directory.\n"
    )

    # Optional action to generate a Mermaid Graph of the topology
    if arguments.graph:

        print("\nGenerating Mermaid Diagram! Your default browser should launch into the Mermaid Live Editor.")
        print("Tip: If the diagram does not appear, click the FULL SCREEN button.\n")

        # Generate Mermaid text from the updated YAML
        mermaid_code = yaml_to_mermaid(topology_data, dir="RL")

        # Generate the mermaid payload and open in local browser
        view_mermaid_diagram(mermaid_code)


# Standard call to the main() function.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script Description", epilog="Usage: ' python gen_clab_topo.py' "
    )

    parser.add_argument(
        "-g",
        "--graph",
        help="Graph the topology in Mermaid Live Editor. Default: False (do not graph)",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-n",
        "--namespace",
        help="Defines the namespace from which to pull topology data from SuzieQ. Default: 'GDL_Campus'",
        action="store",
        default="GDL_Campus",
    )

    arguments = parser.parse_args()
    main()
