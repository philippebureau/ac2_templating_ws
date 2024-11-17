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

The repository was developed on Mac OS-X using Python 3.10.15 and has also been tested on:

- Windows 10/11 natively and Windows Subsystem for Linux (WSLv2)

Use the requirements.txt file to build your virtual environment
``` 
# Create a virtual environment
# If you do this within the top level of your repository you will see a new directory called ac2-venv which will hold your virtual environment
python -m venv ac2wsb4-venv

# Activate your virtual environment 
# Windows
ac2wsb4-venv\Source\Activate.bat (or .ps1)
#Mac/Linux
source ./ac2wsb4-venv/bin/activate

# Building the virtual environment
pip install -r requirements.txt

```

- pip install pytz
- pip install black
- pip install jinja2
- pip install solara
- pip install pyyaml
- pip install pandas
- pip install diagrams
- pip install requests
- pip install openpyxl
- pip install streamlit
- pip install python-dotenv


##### Installed but unused

- pip install httpx
- pip install notebook
- pip install jupyterlab


Note:  diagrams requires the installation of the Graphviz application

[Diagrams Getting Started > Installation](https://diagrams.mingrammer.com/docs/getting-started/installation)

Native installation for Windows Users without a package manager
https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224

[Installation instructions for MacOSX, Windows10/11, and Linux](https://www.perplexity.ai/page/installing-graphviz-on-windows-fzF5FhQASHqTyyOYDD6ODQ)


#### Uninstall all

``` pip uninstall -r requirements.txt -y ```

### Troubleshooting

1. Modules not found when using Python < 3.10.15

   Plan A:  Install pyenv (which is always a good idea)

   If you do not want to upgrade your Python version, we recommend installing pyenv.
   [Complete `pyenv` installation instructions](https://www.perplexity.ai/page/pyenv-installation-and-usage-g-0nRNLEaiSiqrvuzjsFaXrQ)

   Plan B: Install the modules listed above manually in a virtual environment using python 3.9 or greater
   
2. Im new to virtual environments, got any tips?
   This is a great and short introduction that tells you what you need to know and winds up being a great reference.  Thanks Lucas!

   https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/


## All Local

| Mini Project                 | Notes on running local only                                  | Requires External Access                                     |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 00_DataStructure_Woodchipper | All local.  All payload files are in the sample_data_structures directory. | No                                                           |
| 01_CurrentStateReport        | All local.  GDL_bgp.json file is in the directory.           | No                                                           |
| 02_Procedure                 | All local.  All required files are in the directory          | No                                                           |
| 03_Configurations            | All local.                                                   | No                                                           |
| 04_ChangeRequest             | By default all local using the payload.csv file in the directory.  <br />Option -c, --create_cr allows for the creation of the ticket in service now.<br />`python gen_new_vlan_cr.py -c -s "snow FQDN" -u "username" -p "password" | No<br />Optional Personal Developers Instance of Sevice Now  |
| 05_ClabTopology              | By default, expects to extract topology payload from the SuzieQ server.<br />There is a local topology file but the script needs to be updated to use it.<br /><br />There is command line option -g, --graph which generates Mermaid payload and sends it to the Mermaid Live server. | Yes. <br />CloudMyLab SuzieQ Server<br />Optional Mermaid Live Editor Diagram |
| 06_VerificationReportApp     | By default, expects to extract STP payload from SuzieQ server. No local option at this time.<br />Note: This is a Streamlit App. | Yes. <br />CloudMyLab SuzieQ Server                          |
| 07_SoW                       | By default, expects to extract design payload from SuzieQ server.  There is a local Excel file of design payload but the script does not support it currently. | Yes. <br />CloudMyLab SuzieQ Server                          |
| 08_DesignDoc                 | By default, the assignment involves accessing design data on the SuzieQ Server and optionally creating a ticket in a SNOW PDI.<br /><br />The directory does contain an Excel file of the design data (Design_Data_NewSite.xlsx). | Yes. <br />CloudMyLab SuzieQ Server                          |

