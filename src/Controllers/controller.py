import sys
from Controllers.cli_controller import CLI_Controller
from Controllers.gui_controller import GUI_Controller
from Views.cli_view import CLI_View
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
class UML_Controller:

    def __init__(self):
        self._controller:CLI_Controller | GUI_Controller = self.__pick_controller()
        self._autocompleter = self.setup_autocomplete()  
        
    
    def run(self):
        while not self._controller._should_quit:
            self._controller.update(input("Command: ").strip().lower())
    
    def __pick_controller(self, args:str = sys.argv) -> CLI_Controller | GUI_Controller: 
        if len(args) > 1 and str(args[1]).strip().lower() == 'cli':
            return CLI_Controller()
        return GUI_Controller()
    
    def setup_autocomplete(self):
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
    