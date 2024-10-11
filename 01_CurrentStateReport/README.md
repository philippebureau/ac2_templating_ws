# Current State Report Mini Project

This Python script uses the Diagrams module and JSON output from SuzieQ 
to generate a state report on the BGP Sessions for a particular location.

The report is generated in Markdown using the bgp_report_md.j2 Jinja2 template 
which can be found in the templates subdirectory of the 01_CurrentStateReport directory.

The script will take the BGP state output found in `GDL_bgp.json` and process the data in order to answer some 
key questions and generate a diagram of the sessions.

The Current State Report mini project illustrates how to turn a JSON payload of data into a "current state report".

Specifically, we take the JSON output of a SuzieQ bgp show command and process the data in order to:

- Understand the location of the report and develop an appropraite heading
- Note if all the sessions are up
- Note the number of BGP sessions configured
- Detail if the sessions are iBGP or eBGP (including count of each)
- Generate a diagram of the peering relationships with relevant attributes for each (name, vrf, ASN, state)

This project will also establish a pattern that will be used throughout the class.  A repository with a templates folder where all the relevant Jinja2 templates can be found.
This project also illustrates how passing each variable can become too complex.

Putting all your templates in a ***templates*** directory is a good practice and all the other mini projects 
will follow this strategy.


---
### Modules

- jinja2
- diagrams