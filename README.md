# LambdaLegion UML Program (CLI Edition) V1.0
The UML Diagram (CLI Edition) is a command-line tool
designed to help users create, manage, and visualize
UML (Unified Modeling Language) diagrams directly from the terminal.
Primary functionalities include adding, renaming,
and deleting classes, relationships and attributes 
within a UML diagram.

## Features
* Class Management: Add, rename, and delete classes within your UML Diagram.
* Attribute Handling: Manage attributes for each class, including adding, renaming, and deletion.
* Relationship Management: Define and modify relationships between classes, such as association, inheritance, and composition.
* Visualization: Although the current version focuses on the management aspect, future updates aim to include visualization capabilities.
* Save/Load Functionality: Save your current diagram state to a JSON file and load it back into the application for continued management.

# Installation and Running the Program

## Pre-Requisites
* Have Python 3.6 or newer.
* Have Pytest 6.2 or newer. 
## Installation
* Clone the Repository: First, clone the project repository to your local machine using Git. Open a terminal and run the following command<br> `git clone https://github.com/mucsci-students/2024sp-420-LambdaLegion.git`
* Navigate to the project directory `cd 2024sp-420-LambdaLegion`
## Running
* For MacOS/Linux `python3 controller.py`
* For Windows `python -m poetry run uml.py`
## Testing
* For MacOS/Linux `FILL OUT`
* For Windows `python -m pytest`

## Usage
To interact with the UML Diagram CLI Manager, start the application and use the following commands:
* `help`: Display a list of available commands. 
* `help <class>`: Displays commands related to classes
* `help <attribute>`: Displays commands related to attributes
* `help <relationship>`: Displays commands related to relationships
* `add class <class_name>`: Adds a class named <class_name>
* `delete class <class_name`: Deletes class named <class_name> and all of its attributes/relationships
* `"rename class <current_name> <new_name>`: Renames class <current_name> to <new_name>
* `list class <class_name>`: Lists all attributes/relationships pertaining to <class_name>
* `list classes`: Lists all classes in the diagram.
* `add field <class_name> <field_name>` : Adds field named <field_name> 
* `add method <class_name> <method_name>`: Adds method named <method_name>  
* `add parameter <class_name> <method_name> <param_name>`: Adds param named <param_name> to method <method_name>            
* `delete method <class_name> <method_name>`: Deletes method named <method_name>
* `delete field <class_name> <field_name>`: Deletes field named <field_name>
* `delete parameter <class_name> <method_name> <param_name>`: Deletes param named <param_name> from <method_name>
* `rename field <class_name> <current_name> <new_name>`: Renames field <current_name> to <new_name>
* `rename method <class_name> <current_name> <new_name>`: Renames method <current_name> to <new_name>
* `rename parameter <class_name> <method_name> <current_name> <new_name>`: Renames param <current_name> in method <method_name> to <new_name>
* `add relationship <src_class> <destination_class> <relation_type>`: Adds a relationship between <src_class> and <des_class> of <relation_type> 
  * `Relationship types:` (Aggregation, Composition, Generalization, Inheritance)
* `delete relationship <src_class> <destination_class>`: Deletes the relationship between <src_class> <des_class>
* `list relationships`: Lists all relationships in UML
* `list relationship <class_name>`: Lists all relationships to <class_name>
* `save <file_name>`: Saves your UML Diagram as a JSON file.
* `load <filename>`: Loads a UML diagram from a JSON file.
* `exit` Exits the program.

## Updates
* Release 1.1 (March 10, 2024) **CURRENT**
  * + Expaned attributes to have fields and methods (which contain parameters)
  * + Added the ability to run tests using Pytest
  * + Added the ability to list all relationships pertaining to a class (CLI)
  * + Improved visualization of UML (CLI)
  * + Added a GUI
  * - Removed bug which allowed duplicate attributes to be added 
  * - Removed a bug which would allow users to attempt to save a file without editing it

* Release 1.0 (February 11, 2024) 
  * + Added basic functionality for classes
  * + Added basic functionality for attributes
  * + Added basic functionality for relationships
  * + Added basic functionality for Save/Load
  * + Added a CLI interface
  * - Removed Herobrine

## Members
* Danish Zubari 
* Katie Downlin
* Jillian Daggs
* Patrick McCullough
* Zhang Chen