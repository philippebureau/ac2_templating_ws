# Configuration Templates

## Monolithic

With the monolitic strategy templates are define in their entirely based on 

- function
- region
- hardware model
- location type

This has a simplicity that is very attractive and easy to grasp conceptually as well as in code.


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
These templats are for example only. They have not been tested andy may not work!