from Models.uml_diagram import UML_Diagram
from Models.error_handler import Error_Handler
from Models.uml_parser import parse
from Views.cli_view import CLI_View

class CLI_Controller:

    def __init__(self, diagram:UML_Diagram = UML_Diagram(), saved:bool = False):
        self._diagram = diagram
        self._should_quit = False
        self._view = CLI_View()
    
    def update(self, input:str):
        if len(input.strip()) > 0:
            data = parse(self._diagram, input)
            if input[0] == 'save':
                self._saved = True
            else:
                self._saved = False
            return data[0](data[1:])
        
    def quit(self):
        self._should_quit = True
        if not self._saved: 
            if input("Would you like to save? ").strip().lower() in ['y','yes']:
                to_write = diagram_to_json(self._diagram)

            pass

    

