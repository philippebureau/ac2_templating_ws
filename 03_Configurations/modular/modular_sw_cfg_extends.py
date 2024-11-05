#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: modular_sw_cfg
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/9/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"


import argparse
import jinja2


def main():
    """
    MODULAR Inheritance
    Block and Extends
    :return:
    """
    # Set up the Jinja2 environment
    # template_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = "templates"
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

    # Load the templates
    base_template = env.get_template('base_switch_config_block_extends.j2')
    user_interface_template = env.get_template('user_interface_config_extends.j2')
    tacacs_server_template = env.get_template('tacacs_server_config_extends.j2')

    # Sample data
    switch_data = {
        'hostname': 'SW-ACCESS-01',
        'user_vlan': 100,
        'user_interface': 'GigabitEthernet1/0/1',
        'tacacs_server_ip': '192.168.1.100',
        'tacacs_key': 'SecretKey123'
    }

    # Render the templates
    base_config = base_template.render(switch_data)
    user_interface_config = user_interface_template.render(switch_data)
    tacacs_server_config = tacacs_server_template.render(switch_data)

    # Print the rendered configurations
    print("Base Configuration:")
    print(base_config)
    print("\nUser Interface Configuration:")
    print(user_interface_config)
    print("\nTACACS Server Configuration:")
    print(tacacs_server_config)

    # Optionally, save the configurations to files
    with open('mod_extend_base_config.txt', 'w') as f:
        f.write(base_config)

    with open('mod_extend_user_interface_config.txt', 'w') as f:
        f.write(user_interface_config)

    with open('mod_extend_tacacs_server_config.txt', 'w') as f:
        f.write(tacacs_server_config)

    with open('mod_extend_combined_config.txt', 'a') as f:
        f.write(base_config)
        f.write(user_interface_config)
        f.write(tacacs_server_config)

    print("\nConfigurations using the Modular Inheritance/Extends strategy have been saved to text files.")


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python sample_modular.py' ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    # parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',default=False)
    arguments = parser.parse_args()
    main()



# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python modular_sw_cfg.py' ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument(
        "-p",
        "--payload_file",
        help="CSV Payload file to use",
        action="store",
        default="new_switches.csv",
    )
    arguments = parser.parse_args()
    main()
