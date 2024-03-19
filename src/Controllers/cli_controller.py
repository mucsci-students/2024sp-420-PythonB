from Models.uml_diagram import UML_Diagram
from Models.error_handler import Error_Handler
from Models.uml_parser import parse
from Views.cli_view import CLI_View

class CLI_Controller:

    def __init__(self, diagram:UML_Diagram = UML_Diagram(), saved:bool = False):
        self._diagram = diagram
        self._tab_complete = CLI_View()
        self._should_quit = False
    
    @Error_Handler.handle_error
    def update(self, input:str):
        if len(input.strip()) > 0:
            data = parse(self._diagram, input)
            #if the first for chars are help or list, print instead of returning
            if not hasattr(CLI_View, str(input[:4])):
                return data[0](*data[1:])
            #print if it comes from cli view
            print(data)
            print(data[0](*data[1:]))

    

