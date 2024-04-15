from Models.uml_diagram import UML_Diagram
from prompt_toolkit import prompt
from Views.cli_view import CLI_View
from prompt_toolkit.completion import NestedCompleter
from Views.relation_completer import RelationCompleter

class CLI_Controller:

    def __init__(self):
        self._view = CLI_View()
    
    def request_update(self):
         self.setup_autocomplete(self._diagram)
         return prompt("Command: ", completer=self._completer).strip()

    def draw(self, diagram: UML_Diagram):
        pass

    def get_diagram(self, diagram: UML_Diagram):
        self._diagram = diagram

#=========================CLI Specific Parseing=========================#  
    def parse_list_cmd(self, d:UML_Diagram, tokens:list[str]):
        """Parses a list command, returning it in a state ready to be called"""
        match len(tokens):
            case 0:
                return [getattr(self._view, 'list'), d]
            case 1 | 2:
                return [getattr(self._view, 'list_' + tokens.pop(0)), d] + tokens
            case _:
                raise ValueError("Invalid use of list.")

    def parse_help_cmd(self, tokens:list[str]):
        """Parses a help command, returning it in a form ready to be run"""
        if len(tokens) == 0:
            return [getattr(self._view, 'help')]
        elif len(tokens) == 1:
            return [getattr(self._view, 'help_' + tokens.pop(0))]
        else:
            raise ValueError("Invalid command.")
        

#========================= Autocomplete Functionality =========================#          
    def setup_autocomplete(self, dia: UML_Diagram):
        """
        Sets up autocomplete functionality using the NestedCompleter.

        Returns:
        NestedCompleter: An instance of NestedCompleter configured with a dictionary representing available commands
        and their respective subcommands or arguments.
        """
        classes = set(self._view.list_classes(self._diagram).split())

        # Add Relation dict
        class_2nd = {cls: {"Aggregation", "Composition", "Realization", "Inheritance"} for cls in classes}
        add_relation = {cls: class_2nd for cls in class_2nd}

        self._completer = NestedCompleter.from_nested_dict({
        'add': {
            'relation': add_relation,
            'class': None,
            'field': None,
            'method': None,
            'param': None
            
        },
        'delete': {
            'relation': None,
            'class': classes,
            'field': None,
            'method': None,
            'param': None
        },
        'rename':{
            'class': classes,
            'field': None,
            'method': None,
            'param': None
        },
        'list':{
            'class': classes,
            'classes': None,
            'relation': None,
            'relations': None
        },
        'help':{
            'class': None,
            'attribute': None,
            'relation': None
        },
        'save': None,
        'load': None,
        'undo': None,
        'redo': None,
        'quit': None
        })  