from Controllers.CLIcontroller import CLIController
from Views.cli import CLI
from Models.diagram import Diagram
from Models.classadd import UMLClass
import Models.attribute
from Models.saveload import SaveLoad

def main():
    # Create instances of the required classes
    diagram = Diagram()
    classes = UMLClass(diagram)
    fields = Models.attribute.Fields(classes)
    methods = Models.attribute.Methods(classes)
    parameters = Models.attribute.Parameters(methods)
    saveload = SaveLoad()

    # Create an instance of the controller
    CLIcontroller = CLIController(diagram, classes, fields, methods, parameters, saveload)
    
    choice = input("Type 'CLI' to run in CLI mode, otherwise hit enter to run GUI: ").strip().lower()

    if choice == "cli":
        # Create an instance of the CLI and pass the controller to it
        cli_view = CLI(CLIcontroller)

        # Start the CLI interaction
        cli_view.prompt()
    else:
        print("gui goes here")

if __name__ == "__main__":
    main()