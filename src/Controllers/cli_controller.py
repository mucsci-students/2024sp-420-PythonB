
from Models.uml_diagram import UML_Diagram

from prompt_toolkit import prompt
from Views.cli_view import CLI_View

class CLI_Controller:

    def __init__(self):
        self._view = CLI_View()
    
    def request_update(self):
         return prompt("Command: ", completer=self._view._completer).strip()

    def draw(self, diagram: UML_Diagram):
        pass

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