# LambdaLegion UML Program (CWorld Version) V1.0
The UML Diagram (CLI Edition) is a command-line tool
designed to help users create, manage, and visualize
UML (Unified Modeling Language) diagrams directly from the terminal.
Primary functionalities include adding, renaming,
and deleting classes, relationships and attributes 
within a UML diagram.

## Features
* GUI: Program features a graphical user interface in additon to a CLI to interact with diagrams. 
* Class Management: Add, rename, and delete classes within your UML Diagram.
* Attribute Handling: Manage attributes for each class, including adding, renaming, and deletion.
* Relationship Management: Define and modify relationships between classes, such as association, inheritance, and composition.
* Save/Load Functionality: Save your current diagram state to a JSON file and load it back into the application for continued management.
* Export as Image: Export the diagram as a png image file.

# Setup and Installation

## Pre-Requisites
<B>Python 3.8 or higher. You can download Python [here](https://www.python.org/downloads/)</B>

# Download the Project

### In a Terminal
To download the project directly into a terminal:
'git clone https://github.com/mucsci-students/2024sp-420-PythonB/releases/tag/v3.0.0'

### In a Desktop Environment
Download the zip [here](https://github.com/mucsci-students/2024sp-420-PythonB/releases/tag/v3.0.0) and extract it.

# Build the Project

It is recommended you use a virtual environment when running this program. Instructions for this can be found [here](https://docs.python.org/3/library/venv.html).

**The command to execute a python program varies with operating system. On Mac: python3. On Linux: on Windows: py. Python will be used below, substitute the command appropriate for your operating system in its place.**

<ol>
<li> Open a terminal and navigate to the folder that the project was cloned to. 
<li> Navigate to the source directory of the project (its name should be 2024sp-420-PythonB)
<li> Enter your virtual environment (create one if you don't have one, instructions above)
<li> Type 'pip install -e .'.
<li> Type 'python main.py' to run the program in its default mode (Additional modes below).
</ol>

### Operation modes
- ``python main.py ``      - default operation mode, opens a GUI.
- ``python main.py cli``   - runs the program in CLI mode.

**If you are in the CLI mode, type 'help' for a the help menu.**
**In the gui, use the menu options available at the top of the screen and along the left side of the window.**
### Commands for CLI
`` help class `` - Prints a help menu for class. <br>
`` add class <class_name> `` - Adds a class. <br>
`` delete class <class_name> `` - Deletes a class. <br>
`` rename class <old_name> <new_name> ``- Renames a class from its old name to a new name.  <br>
`` list class <class_name> `` - Lists information about the given class. <br>
`` list classes `` - Lists all classes in the diagram. <br>

`` help relations `` - Prints a help menu for relations. <br>
`` add relation <source> <dest> <type> `` - Adds a relation between a source class and destination class of a specified type. <br>
`` delete relation <source> <dest> `` - Deletes the relation between source and dest  <br>
`` list relations `` - List all relations in diagram. <br>
`` list relation <class_name> `` - List all relations containing the given class. <br>

`` add field <class_name> <fld_name> `` - Adds a field to given class. <br>
`` delete field <class_name> <fld_name> `` - Deletes a field from class. <br>
`` rename field <class_name> <old_name> <new_name> `` - Renames a field  <br>

`` add method <class_name> <mthd_name> `` - Adds a method to a class. <br>
`` delete method <class_name> <mthd_name> `` - Deletes a method from a class. <br>
`` rename method <cls_name> <mth_name> <new_name> `` - Renames a method <br>

`` add param <cls_name> <mthd_name> <param> `` - Adds a param to a method within a class. <br>
`` delete param <cls_name> <mthd_name> <param> `` - Deletes a param from a method within a class. <br>
`` rename param <cls_name> <mthd_name> <param_name> <new_name> `` - Renames a methods parameter within a class. <br>

`` save <file_name> `` - Saves the diagram. <br>
`` load <file_name> `` - Loads a diagram.  <br>
`` export <file_name> `` - Export the diagram as a png image file.  <br>
`` undo `` - Undoes the last command.  <br>
`` redo `` - Undoes an undo.  <br>
`` quit `` - Quits the program. <br>

### Test the project
'pytest'  - from the source directory of the project, automatically finds and executes all test files.

### Design Patterns
- MVC       - MVC is used as an organizational structure for the program. It can be seen in the names of the folders that contain controllers, the model, and the different views.

- Singleton - The file uml_undo_redo.py contains a definition for a UML_States class; only one of these can ever exist in the program. The definition of ``__new__ `` only creates a new instance of the object if one is not already created.

- Visitor   - There are two examples of visitor in the program; uml_save_load.py and uml_list.py are both implementations of the uml_visitor.py interface, which in turn relies on accept methods defined in each other object in the model. This structure allows recursive descent through the diagram while storing extra location data (tab depth in the case of listing), which helps to keep listing and converting to json clean and maintainable.

- Memento   - The file uml_undo_redo.py contains a definition for a UML_States class; this class is an example of a memento for the diagram. Upon successful execution of a command, around line 38 of the file controller.py, the diagram is converted to JSON and stored as a state in that list. From there, undo and redo can be used to restore past or future diagram states. If a command or GUI action fails, the diagram will automatically revert to the last valid state (as can be seen around line 45 of the controller) if a valid state exists.

- Decorator - The file controller.py is a decorator for the cli_controller.py and gui_controller.py files. controller.py has a method beginning around line 49 titled __pick_controller that decides which controller needs to be instantiated for the current instance of the program. That controller is then decorated with the functionality of controller.py, enabling it to run the program.

- Factory - The GUI View has a factory for constructing all of the dialog boxes that the user interacts with, such as when adding a class to the diagram. The Diagram_Factory is towards the bottom of the GUI View under the Dialog Factory seperator.
## Authors
January 2024 to March 2024:
- Zhang Chen, Jillian Daggs, Katie Downlin, Patrick McCullough, Danish Zubari 

March 2024 to Present: 
- Ganga Acharya, Marshall Feng, Peter Freedman, Adam Glick-Lynch, Tim Moser