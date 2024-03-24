from Models.uml_diagram import UML_Diagram
from Models.error_handler import Error_Handler
from Models.uml_parser import parse
from Views.cli_view import CLI_View
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

class CLI_Controller:

    def __init__(self, diagram:UML_Diagram = UML_Diagram(), saved:bool = False):
        self._diagram = diagram
        self._should_quit = False
        self._completer = self.setup_autocomplete()  
    
    @Error_Handler.handle_error
    def update(self, input:str):
        if len(input.strip()) > 0:
            data = parse(self._diagram, input)
            r_val = data[0](*data[1:])
            if isinstance(r_val, str):
                print(r_val) 
               
    def setup_autocomplete(self):
        """
        Sets up autocomplete functionality using the NestedCompleter.

        Returns:
        NestedCompleter: An instance of NestedCompleter configured with a dictionary representing available commands
        and their respective subcommands or arguments.
        """
        return NestedCompleter.from_nested_dict({
        'add': {
            'class': None,
            'field': None,
            'method': None,
            'relationship': None
        },
        'delete': {
            'class': None,
            'field': None,
            'method': None,
            'relationship': None
        },
        'rename':{
            'class': None,
            'field': None,
            'method': None
        },
        'list':{
            'class': None,
            'classes': None,
            'relationship': None,
            'relationships': None
        },
        'save': None,
        'load': None,
        'exit': None
        })  
    


    

