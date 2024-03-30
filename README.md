# LambdaLegion UML Program (CWorld Version) V1.0
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

# Setup and Installation

## Pre-Requisites
<B>Python 3.8 or higher. You can download Python here: [this](https://www.python.org/downloads/)</B>

# Download the Project

### In a Terminal
To download the project directly into a terminal:
'git clone https://github.com/mucsci-students/2024sp-420-PythonB/releases/tag/v2.0.0'

### In a Desktop Environment
Download the zip [here](https://github.com/mucsci-students/2024sp-420-PythonB/releases/tag/v2.0.0) and extract it.

# Build the Project

It is recommended you use a virtual environment when running this program. Instructions for this can be found here: [this link](https://docs.python.org/3/library/venv.html).

**The command to execute a python program varies with operating system. On Mac: python3. On Linux and Windows: python. Python will be used below, substitute the command appropriate for your operating system in its place.**

<ol>
<li> Open a terminal and navigate to the folder that the project was cloned to. 
<li> Navigate to the source directory of the project (its name should be 2024sp-420-CWorld)
<li> Enter your virtual environment if you want to use one (link above)
<li> Type 'pip install -e .'.
<li> Type 'python main.py' to run the program in its default mode (Additional modes below).
</ol>

### Operation modes
- `'python main.py'       - default operation mode, opens a GUI.
- `'python main.py cli'   - runs the program in CLI mode.
- `'python main.py debug' - runs the program in CLI debug mode. This mode is similar to the CLI mode, supresses some error handling. Use at your own risk.

**If you are in the CLI mode, type 'help' for a list of commands.**
**In the gui, use the menu options available at the top of the screen.**

### Test the project
'pytest'  - from the source directory of the project, automatically finds and executes all test files.

### Design Structures
- MVC       - This is the main structure of the program. Each part is contained in its own folder.
- Singleton - Controller?
- Visitor   - Help Menu?

## Authors
January 2024 to March 2024:
- Zhang Chen, Jillian Daggs, Katie Downlin, Patrick McCullough, Danish Zubari 
March 2024 to Preset: 
- Ganga Acharya, Marshall Feng, Peter Freedman, Adam Glick-Lynch, Tim Moser