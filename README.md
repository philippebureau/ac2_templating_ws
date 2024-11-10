# NAF AutoCon2 Denver, CO USA
# WS:B4 - A day in the life of a Network Engineer using Jinja2 Templates
Proctor: Claudia de Luna, EIA

Teaching Assistants:
- Mike Lester (EIA)

- Lucas Boyd (Former EIA)


Description: Using templates to create network docs & configurations programmatically is key to any automation strategy; we will generate a wide range of artifacts using Jinja templates.
Level: Beginner, Intermediate
Agenda:
+ Everyone already has templates, Why are we here?
+ Background on templating languages
+ Revision Control
+ Template format
+ Jinja2 Fundamentals
+ Working Sessions

![Claudia - WS Promo2.png](images/Claudia_WSPromo2.png)

This workshop will present a number of "mini projects".  These mini projects are intended to showcase self contained templating solutions.

#### Data Woodchipper

The first mini-project is intended to illustrate the relationship between data structures, how they can be decomposed, and referenced in a Jinja2 template.

#### Current State Report

The Current State Report mini project illustrates how to turn a JSON payload of data into a "current state report".

Specifically, we take the JSON output of a SuzieQ bgp show command and process the data in order to:

- Understand the location of the report and develop an appropraite heading
- Note if all the sessions are up
- Note the number of BGP sessions configured
- Detail if the sessions are iBGP or eBGP (including count of each)
- Generate a diagram of the peering relationships with relevant attributes for each (name, vrf, ASN, state)

This project will also establish a patter that will be used throughout the class.  A repository with a templates folder where all the relevant Jinja2 templates can be found.
This project also illustrates how passing each variable can become too complex.  This sets the state for a more scalable way to pass payload information into the template in the **Procedure** mini-project.

#### Procedure

This mini-project will illustrate how to use a Jinja2 template to produce detailed work instructions or procedures for a specific task. 

In this project, we will use a local YAML file to store the design data required.  Based on the design data, the script will produce a specific Markdown document with all the details required for a "smart-hands" technician to perform the installation work.


---
#### Modules

Use the requirements.txt file to build your virtual environment
``` 
# Create a virtual environment
# If you do this within the top level of your repository you will see a new directory called ac2-venv which will hold your virtual environment
python -m venv ac2-venv

# Activate your virtual environment 
# Windows
ac2-venv\Source\Activate.bat (or .ps1)
#Mac/Linux
source ./ac2-venv/bin/activate

# Building the virtual environment
pip install -r requirements.txt

```


pip install jinja2

pip install solara

pip install black

pip install pyyaml

pip install pandas

pip install diagrams

pip install httpx

pip install python-dotenv

pip install streamlit

#### Uninstall all

``` pip uninstall -r requirements.txt -y ```