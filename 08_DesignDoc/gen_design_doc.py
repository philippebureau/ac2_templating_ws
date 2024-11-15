#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: gen_design_doc.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "11/14/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"


import os
import sys
import argparse
# This is necessary because I want to import functions in a file called utils.py and that file is one level up
# from here
# Get the absolute path of the top level main repository
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Append the parent directory to sys.path so python searches that directory for the utils file
sys.path.append(parent_dir)
# Import the utils module (python script) one level up
import utils


def prompt():

    """
    This is just a summary of the activities that need to be done to complete this mini project.

    This should be removed from main() once the project is complete.

    :return:
    """


    prompt = """
    
    Extract the design available to you from the Devices, Subnets/Vlans, and Connectivity Matrix tables
    
    You have two options.  
    1. via REST calls to the SuzieQ Server
    
    # https://172.16.14.4:8443/api/v2/extdb/show?ext_table=newDevs&view=latest&namespace=DEN_Campus&columns=default&reverse=false&include_deleted=false&show_exceptions=false

    2. using the CSV files in the csv_outputs directory
    
    With an understanding of the design data available to you, manipulate the design data into an appropriate payload for the template.
    
    Update the template accordingly.
    
    STEPS 1,2 and 3
    If you have followed the pattern established in the other mini projects, you can use the utils function
    
    render_in_one
    
    providing you make the appropriate variable adjustments.
    
    Save the rendered file as Markdown and include the location in the filename.
    
    Craft text suitable for a Change Control ticket and save in a change_request_text.txt file.
    
    """

    return prompt


def main():
    """
    Create a LowLevel Design markdown template and use the DEN_Campus design data to render a LLD for that locaiton.

    REF:
    utils.extract_excel_to_csv("Design_Data_NewSite.xlsx")

    :return:
    """

    print(prompt())


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python gen_design_doc.py' ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    # parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',default=False)
    arguments = parser.parse_args()
    main()
