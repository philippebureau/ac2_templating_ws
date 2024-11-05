# Procedure/Work Instructions Mini Project

This mini project illustrates how to use a template to develop specific installation procedures for a particular location.

### Usage

```python
% python gen_procedure.py -h                              
usage: gen_procedure.py [-h] [-p PAYLOAD_FILE]

Script Description

options:
  -h, --help            show this help message and exit
  -p PAYLOAD_FILE, --payload_file PAYLOAD_FILE
                        YAML Payload file to use

Usage: 'python gen_procedure.py' The default payload is 'Installation_details.yml'. To use another payload file use the -p option.


```

The project has two YAML files with installation payload.  One for a model S600 and the other for a model S2000 appliance.

```python
% python gen_procedure.py -p Installation_details_S600.yml
```

This mini project will show how to send a dictionary to the template and explode out by key/value pairs.
This is another "lesson learned" and we will use this for all the remaining mini projects.

This mini project establishes the typical processing pattern:

- manipulate the data 
  - Calculate the IP, Gateway, and Mask in dotted decimal.

- put it in a payload dictionary
- send the payload to the template via the render call
- break out in the template

We also continue using utils module.

The following functions in the utils module are used:

- `get_first_ip` to calculate the gateway for the applicance configuraiton
- `get_mask_from_cidr` to calculate the mask in dotted decimal notation for the appliance configuration
- `get_fourth_ip` to calculate the IP (4th in subnet by convention) for the appliance configuration
- Step1: `jenv_filesystem` to safely establish the template file system including single line comments and white space control
- Step2: `load_jtemplate` to safely load the required report template
- Step 3 is done in-line in the script
- `save_file` to save the resulting procedure Markdown file

### Passing the payload

```python
YAML File Contents
{
 'appliance_location': 'Floor 1 MDF',
 'due_date': datetime.date(2024, 12, 4),
 'l3_dev': 'den-core01',
 'loc_type': 'branch',
 'location': 'DEN Office',
 'mgmt_int': 'GigabitEthernet1/0/47',
 'mgmt_subnet': '192.168.7.0/29',
 'mgmt_sw': 'den-as01',
 'mgmt_vlan': 60,
 'model': 'S600',
 'name': 'den-sec-app01.uwaco.net',
 'notes': 'Shelf may be a tight fit an may use up an extra RU',
 'photos': 'TBD',
 'power_plug': 'NEMA 5-15',
 'rack': 1,
 'rspan_range': '7XX',
 'ru': 12,
 'sh_email': 'ed@king-of-comedy.net',
 'sh_mobile': '555-666-5677',
 'smart_hands': 'Ed Herlihy',
 'span_int': 'TenGigabitEthernet1/1/21'
}

```



In the Current Sate Report mini project we saw how sending individual variables to the template could become "messy".  That would certainly be the case with these 20 variables.  Here we introduce the idea of sending a more complex data structure, a dictionary or a list of dictionaries.

In this mini project we will establish the pattern of sending our payload in dictionary.

Example:

payload_dict = {
  "ip_address": "192.168.0.1"
}


```
  rendered = template_obj.render(cfg=payload_dict)
```

We send our payload_dict to our template in the variable cfg (something short so we dont have to type so much!)

Now we can get the IP address by using the key of "ip_address" in the cfg dictionary.

Jinja2 Template using cfg variable:

```
IP Address is {{ cfg['ip_address'] }}
```

We could send `payload=payload_dict` and then get the ip via `payload['ip_address']`.

Jinja2 Template using payload variable:

```
IP Address is {{ payload['ip_address'] }}
```

Another option is to send the payload directly. 

```
  rendered = template_obj.render(payload_dict)
```

This probably seems very attractive.  Jinja2 will "unpack" the variable (**) so you can use the "key" directly in your template like below.

```
IP Address is {{ 'ip_address' }}
```

While attractive, this makes troubleshooting more difficult.  If you don't know all the keys (of course you can list them in your script) or what to look at what is getting passed to your template, this method does not directly support that.

For this reason, I always recommend passing a named variable like `cfg`. 

Worst case, you can have a template with:

```
Payload {{ cfg }}
```

which will output your data structure once rendered.





---
### Modules

- jinja2

