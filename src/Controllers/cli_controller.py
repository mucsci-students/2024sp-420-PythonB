
from Models.uml_diagram import UML_Diagram

from prompt_toolkit import prompt
from Views.cli_view import CLI_View



class CLI_Controller:

    def __init__(self):
        self._view = CLI_View()
    
    
    def update(self, parsed_input:list):
        r_val = parsed_input[0](*parsed_input[1:])
        if isinstance(r_val, str):
            print(r_val) 
        # return the Diagram if the function called returns a Diagram
        if isinstance(r_val, UML_Diagram):
            return r_val
    
    def request_update(self):
         return prompt("Command: ", completer=self._view._completer).strip()


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