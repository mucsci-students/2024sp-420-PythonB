
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
## Installation
* Clone the Repository: First, clone the project repository to your local machine using Git. Open a terminal and run the following command<br> `git clone https://github.com/mucsci-students/2024sp-420-LambdaLegion.git`
* Navigate to the project directory `cd 2024sp-420-LambdaLegion`
## Running
* For MacOS/Linux `python3 controller.py`
* For Windows `python controller.py`

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
* `help attribute`: Displays this menu
* `add attribute <attribute_name> <class_name>`: Adds attribute named <attribute_name>
* `delete attribute <attribute_name> <class_name>`: Deletes attribute named <attribute_name>
* `rename attribute <current_name> <new_name> <class_name>`:  Renames attribute <current_name> to <new_name>
* `add relationship <src_class> <destination_class> <relation_type>`: Adds a relationship between <src_class> and <des_class> of <relation_type> 
  * `Relationship types:` (Aggregation, Composition, Generalization, Inheritance)
* `delete relationship <src_class> <destination_class>`: Deletes the relationship between <src_class> <des_class>
* `list relationship <class_name>`: Lists all relationships to <class_name>
* `save <file_name>`: Saves your UML Diagram as a JSON file.
* `load <filename>`: Loads a UML diagram from a JSON file.
* `exit` Exits the program.

## Updates
* Release 1.0 (February 11, 2024) **CURRENT**
  * Added basic functionality for classes
  * Added basic functionality for attributes
  * Added basic functionality for relationships
  * Added basic functionality for Save/Load
  * Added a CLI interface
  * Removed Herobrine

## Members
* Danish Zubari 
* Katie Downlin
* Jillian Daggs
* Patrick McCullough
* Zhang Chen
               