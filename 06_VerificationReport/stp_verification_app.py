#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: stp_verification_app.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "11/10/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"


import os
import sys
import pandas as pd
import streamlit as st


# This is necessary because I want to import functions in a file called utils.py and that file is one level up
# from here
# Get the absolute path of the top level main repository
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Append the parent directory to sys.path so python searches that directory for the utils file
sys.path.append(parent_dir)
# Import the utils module (python script) one level up
import utils


def generate_report(selected_switches, vlan_id):
    """Generate a markdown report based on selected switches and VLAN ID."""
    report = f"""
# Network Configuration Report

## VLAN Configuration
**VLAN ID:** {vlan_id}

## Selected Switches
"""
    for switch in selected_switches:
        report += f"- {switch}\n"

    report += "\n## Configuration Summary\n"
    if selected_switches:
        report += f"VLAN {vlan_id} should be configured on {len(selected_switches)} switch{'es' if len(selected_switches) > 1 else ''}."
    else:
        report += "No switches selected for configuration."

    report += f"""

VLAN {vlan_id} should be 
- configured on each switch, 
- should have a properly formatted name, 
- should be participating in Spanning Tree and 
- have a root interface

"""
    return report


def main():

    selected_switches = list()
    namespace_list = list()
    selected_ns = list()

    # Set page title
    st.set_page_config(page_title="Vlan Provisioning Verification Tool", layout="wide")

    # Add header
    st.title("Vlan Provisioning Verification Tool")

    # Initialize session state for inputs
    if 'namespace' not in st.session_state:
        st.session_state.namespace = ""
    if 'device_list' not in st.session_state:
        st.session_state.device_list = list()
    if 'vlan_id' not in st.session_state:
        st.session_state.vlan_id = 1

    # Create two columns for inputs
    col1, col2 = st.columns(2)

    with col1:

        # Get Namespaces
        namespace_list = utils.get_namespace_list()

        try:

            selected_ns = st.selectbox(
                "Select Location",
                namespace_list,
                help="Choose the location where you want to verify the VLAN configuration",
                placeholder="Choose a location",
                index=None,
                key="namespace",
            )
        except:
            st.write("Select Location")

        if selected_ns:
            # Sample list of switches (you can modify this list)
            available_switches = utils.get_device_list(selected_ns)

            # Create multi-select for switches
            selected_switches = st.multiselect(
                "Select Switches",
                available_switches,
                help="Choose the switches where you want to configure the VLAN",
                key="device_list",
            )

        # Create VLAN ID input
        vlan_id = st.number_input(
            "VLAN ID",
            min_value=1,
            max_value=4094,
            # value=1,
            help="Enter a VLAN ID between 2 and 4094",
            key="vlan_id",
        )

    with col2:
        st.write(st.session_state)

    # Add a separator
    st.divider()

    # Generate and display report

    selected_switches = st.session_state.device_list
    vlan_id = st.session_state.vlan_id

    if selected_switches and vlan_id != 1:

        # Add a generate button (for future functionality)
        if st.button("Verify Configuration"):

            st.header("Configuration Report")
            report = generate_report(selected_switches, vlan_id)
            st.markdown(report)

            vlan_configured_bool = True
            stp_root_bool = True

            sw_missing_vlan_list = list()
            stp_problem_list = list()

            for sw in selected_switches:
                # Check to see if the vlan is configured on each switch
                vlan_on_sw, vlan_resp = utils.find_vlan_on_switch(vlan_id, sw)
                if vlan_on_sw:
                    st.write(f"Vlan {vlan_id} Configured on Switch {sw}")
                else:
                    st.write(f"Vlan {vlan_id} NOT on Switch {sw}")
                    vlan_configured_bool = False
                    sw_missing_vlan_list.append(sw)

                # Check to see if the vlan is participating in spanning tree
                stp_root_on_sw_bool, stp_resp = utils.check_stp_switch(vlan_id, sw)
                df = pd.DataFrame(stp_resp.json())
                if stp_root_on_sw_bool:
                    st.write(f"Vlan {vlan_id} participating in STP and has root {sw}")
                else:
                    st.write(f"Vlan {vlan_id} STP has no root on {sw}")
                    stp_root_bool = False
                    stp_problem_list.append(sw)
                st.write(df)

            if vlan_configured_bool:
                st.success(f":thumbsup: Vlan {vlan_id} is configured on all switches!")
            else:
                st.error(f":thumbsdown: CONFIGURATION is INCOMPLETE.  {len(sw_missing_vlan_list)} switch(s) missing vlan {vlan_id}")
                for sw in sw_missing_vlan_list:
                    st.write(f"- {sw}")

            if stp_root_bool:
                st.success(f":thumbsup: Vlan {vlan_id} has root on all switches!")
            else:
                # TODO: Check to see if it IS the root!
                st.error(f":thumbsdown: STP ERROR.  {len(stp_problem_list)} switch(s) without STP root on vlan {vlan_id}")
                for sw in stp_problem_list:
                    st.write(f"- {sw}")

            # TODO: Check to see if the vlan name is per guideline (has the subnet)


if __name__ == "__main__":
    main()
