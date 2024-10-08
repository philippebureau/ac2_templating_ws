# Data Structure Woodchipper

The goal of this mini project is to look at different data structures and how they can be 
- passed into a template, and
- decomposed 

within a Jinja2 Template.

The solara module is uses to present the information via a web interface which can be run locally 
on the student's laptop.

In the examples, all payload is loaded into a variable named `loaded_data`.
This variable in the pyhon script can be a 
- string variable
- a list
- a dictionary
- a complex data structure

The data_woodchipper.py App illustrates data structures and their display in corresponding Jinja2 templates.

### Starting the App
Change into the 00_DataStructureChipper directory.
```bash
solara run data_woodchipper.py
```

When the web page comes up, a list of available files comes up.  These files contain various types of data structures.

Click on one to select it and the right side of the center pane will show the data itself and its type.
The left side of the center pane will show the corresponding template derived from the data type.
The bottom part of the center pane will show the rendered template.

---

#### Modules 
- jinja2
- solara