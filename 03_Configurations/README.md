# Configuration Templates

This mini-project has a number of examples to showcase the different strategies.

- Monolithic
- Modular
  - Using Jinja2 Inheritance
  - Using Jinja2 Includes

## Monolithic

With the monolitic strategy, templates are define in their entirety based on 

- function
- region
- hardware model
- location type

This has a simplicity that is very attractive and easy to grasp conceptually as well as in code.
You have one master template for an access switch, a branch office switch, etc.  Some will have templates based on region, etc.

In the monolitic directory you will find a Python script which generates device configurations from the new_switch.csv file using the dance base sample template which can be found (as ususal) in the templates directory.

```python
├── cfg_output
├── monolithic_sw_cfg.py
├── new_switches.csv
└── templates
    └── dnac_baseconfig_sample_template.j2

```

This introduces another common strategy, which you saw to some degree in the 02_Procedure mini project.  Bring in payload (REST, JSON, YAML, XLSX, CSV etc.) and then add key/value pairs.

In this case, we want to timestamp each template so we know when it was generated, so we calculate a human readable timestamp and add that key/value pair to our payload dictionarly.

We bring in a temporary enable secret and add that to the payload.

We calculate the number of user interfaces based on the model number so we know how many interfaces to configure.

```python
% python monolithic_sw_cfg.py -h
usage: monolithic_sw_cfg.py [-h] [-p PAYLOAD_FILE] [-o OUTPUT_DIR] [-s SECRET_TEMP] [-t TIMEZONE]

Script Description

options:
  -h, --help            show this help message and exit
  -p PAYLOAD_FILE, --payload_file PAYLOAD_FILE
                        CSV Payload file to use Default is new_switches.csv
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        output directory for configuration files Default is cfg_output
  -s SECRET_TEMP, --secret_temp SECRET_TEMP
                        Temporary enable secret and login password
  -t TIMEZONE, --timezone TIMEZONE
                        Timezone defaults to America/Los_Angeles

Usage: ' python monolithic_sw_cfg.py # Assumes a CSV file new_switches.csv with new switch payload'
```






## Modular

The modular strategy gives you the a'la carte option.

You can break out your configurations as you like including
- base
- user interface
- uplinks (by model if you like)
- NAC servers
- TACACS servers
- tty configuration
- routing
- acls
- ....

Each one can now be updated individually without having to modify the one big template.

Jinja has two approaches to support this "modularity":

1. Inheritance (extends)
2. includes

### Inheritance (extends)

With inheritance you define a base template with {% block <name> %} and child templates 

base_switch_config.j2 (base)

- ​	user_interface_config.j2 # extends "base_switch_config.j2"
- ​	tacacs_server_config.j2 # extends "base_switch_config.j2"

The price for that is you need one (or more) overarching templates to put it all together.





```python

Main Switch Configuration Template

{# main_switch_config.j2 #}
{% include "base_switch_config_include.j2" %}

{% block user_interface %}
{% include "user_interface_config_include.j2" %}
{% endblock %}

{% block tacacs_config %}
{% include "tacacs_server_config_include.j2" %}
{% endblock %}

```

WARNING
These templates are for example only. They have not been tested andy may not work!


---
### Modules

- jinja2
