from Models import *
from Views.cli_view import CLI_View
import re

classes = [UML_Diagram, UML_Class, UML_Relation, UML_Method, UML_Field, UML_Param, uml_save_load]

def parse(d:UML_Diagram, input:str) -> list | str:
    tokens = check_args(input.split())
    
    if len(tokens) < 3:
        cmd = tokens[0].strip().lower()
        if cmd == 'quit':
            return cmd
        if cmd == 'save' or cmd == 'load':
          return [getattr(uml_save_load, cmd), d, tokens[1]]
        if cmd == 'help':
            return __handle_help(tokens)
    else:
        return [get_instance(d, tokens)] + tokens
    

def check_args (args:list[str]) -> list[str]: 
    """Makes sure every string in *args is valid"""
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
    for arg in args: 
        if not regex.match(arg):
            raise ValueError("Argument {0} is invalid.".format(arg))
    return args

def __handle_help(tokens:list[str]):
    if len(tokens) == 1: 
        return [getattr(CLI_View(), 'help')]
    if len(tokens) == 2: 
        return [getattr(CLI_View(), 'help_' + tokens[1])]
    raise ValueError("No help options available for {0}.".format(tokens[1]))

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
    if cmd_target_name == 'relation' or cmd_target_name == 'class':
        object = getattr(d, cmd + '_' + cmd_target_name)
    else: 
        object = getattr(d, 'get_class')(tokens.pop(0))
        if cmd_target_name == 'method' or cmd_target_name == 'field':
            object = getattr(object, cmd + '_' + cmd_target_name)
        elif cmd_target_name == 'param':
            object = getattr(object, 'get_method')(tokens.pop(0))
            object = getattr(object, cmd + '_' + cmd_target_name)
    return object