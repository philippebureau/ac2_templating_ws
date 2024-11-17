#!/usr/bin/python -tt
# Project: ac2_templating_workshop
# Filename: move_access_intf.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "11/2/24"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"


import jinja2
import utils


def main():

    # Step 1 - Define the environment containing the templates you want to use
    # Here all the templates will be in a directory called "templates" relative to the current directory
    env_obj = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates", encoding="utf-8")
    )

    env_obj2 = utils.jenv_filesystem(line_comment="", ktn=True, lsb=True, tb=True)

    # Step 2 - Load the specific template to be used
    template_obj = env_obj.get_template("move_intf.j2")

    template_obj2 = env_obj2.get_template("move_intf_w_macro.j2")

    # Template Payload
    cfg_dict = {
        "GigabitEthernet1/0/27": 300,
    }

    cfg_dict2 = dict()
    for idx in range(1, 6):
        cfg_dict2.update({f"GigE1/0/{idx}": 300})

    print(cfg_dict2)

    # Step 3 - Render the template with specific payload
    # The template is expecting a dictionary named "cfg"
    desc = ""
    rendered = template_obj.render(cfg=cfg_dict2, desc="Digital Signage")

    rendered2 = template_obj2.render(cfg=cfg_dict2, desc=desc)

    print(rendered)

    print("==== With white space settings set in env ====")
    print(rendered2)


# Standard call to the main() function.
if __name__ == "__main__":
    main()
