from Models import *
from Views.cli_view import CLI_View
import re

cli_view = CLI_View()
def parse(d:UML_Diagram, input:str) -> list | str:
    tokens = check_args(input.split())
    
    if len(tokens) < 3:
        cmd = tokens[0].strip().lower()
        if cmd == 'quit':
            return cmd
        elif cmd == 'save' or cmd == 'load':
          return [getattr(uml_save_load, cmd), d, tokens[1]]
        #this handles lsit and help.
        else:
            if cmd == 'help':
                return __list_help_logic(tokens)
            if cmd == 'list':
                return __list_help_logic(tokens) + [d]

    return [get_instance(d, tokens)] + tokens
    

def check_args (args:list[str]) -> list[str]: 
    """Makes sure every string in *args is valid"""
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
    for arg in args: 
        if not regex.match(arg):
            raise ValueError("Argument {0} is invalid.".format(arg))
    return args

def __list_help_logic(tokens:list[str]):
    """Parses list and help commands specifically"""
    cmd = tokens[0].lower()
    if len(tokens) == 1: 
        return [getattr(cli_view, cmd)]
    elif len(tokens) == 2: 
        return [getattr(cli_view, cmd + '_' + tokens[1])]
    raise ValueError("No {0} options available for {1}.".format(cmd, tokens[1]))


def get_instance(d:UML_Diagram, tokens:list[str]) -> list:
    """Turns a command into an instance of a method being applied to an object
        and the args to that method
        
        Raises: ValueError if a command is invalid
                AttributeError if the target class does not have the requested method
        
        Returns: A list in the form [function object, arg1, arg2,...,argn]
    """
    cmd = tokens.pop(0).lower()
    cmd_target_name = tokens.pop(0).lower()
    print (cmd_target_name)
    object = None
    #if cmd target is relation or class, we can get it directly from the diagram
    if cmd_target_name == 'relation' or cmd_target_name == 'class':
        object = getattr(d, cmd + '_' + cmd_target_name)

    else:
        #if cmd target isn't in the diagram, we know it is at least in a class. Get that class.
        object = getattr(d, 'get_class')(tokens.pop(0))
        if cmd_target_name == 'method' or cmd_target_name == 'field':
            object = getattr(object, cmd + '_' + cmd_target_name)
        #if cmd target isn't in a class, the only other place for it to be is in a method. 
        elif cmd_target_name == 'param':
            object = getattr(object, 'get_method')(tokens.pop(0))
            object = getattr(object, cmd + '_' + cmd_target_name)
    
    return object