from Models import *
from Views.cli_view import CLI_View
import re

cli_view = CLI_View()

def parse(d:UML_Diagram, input:str) -> list | str:
    tokens = check_args(input.split())
    
    if len(tokens) < 3 or tokens[0] == 'list': 
        return short_command(d, tokens)
    else: 
        return instance_command(d, tokens)
    

def short_command(d:UML_Diagram, tokens:list[str]) -> list:
    """Parses all forms of the following commands, returning appropriate lists for each: 
        quit, save, load, undo, redo, list, help
    """
    cur_token = tokens.pop(0)
    match cur_token: 
        case 'quit':
            import src.Controllers.controller
            return [getattr(src.Controllers.controller,"quit")]
        case 'save' | 'load':
            return [getattr(uml_save_load, cur_token), d, tokens.pop(0)]
        case 'undo' | 'redo':
            #TODO: return [getattr(UML_States, cur_token)]
            pass
        case 'list':
            return __parse_list_cmd(d, tokens)
        case 'help':
            return __parse_help_cmd(tokens)
        case _:
            raise ValueError("Invalid command.")

def __parse_list_cmd(d:UML_Diagram, tokens:list[str]):
    """Parses a list command, returning it in a state ready to be called"""
    match len(tokens):
        case 0:
            return [getattr(cli_view, 'list'), d]
        case 1 | 2:
            return [getattr(cli_view, 'list_' + tokens.pop(0)), d] + tokens
        case _:
            raise ValueError("Invalid use of list.")

def __parse_help_cmd(tokens:list[str]):
    """Parses a help command, returning it in a form ready to be run"""
    if len(tokens) == 0:
                return [getattr(cli_view, 'help')]
    elif len(tokens) == 1:
        return [getattr(cli_view, 'help_' + tokens.pop(0))]
    else:
        raise ValueError("Invalid command.")

def check_args (args:list[str]) -> list[str]: 
    """Makes sure every string in args is valid
        Valid names match the following regex: ^[a-zA-Z][a-zA-Z0-9_]*$
    """
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
    for arg in args: 
        if not regex.match(arg):
            raise ValueError("Argument {0} is invalid.".format(arg))
    return args

def instance_command(d:UML_Diagram, tokens:list[str]) -> list:
    """Turns a command into an instance of a method being applied to an object
        and the args to that method
        
        Raises: ValueError if a command is invalid
                AttributeError if the target class does not have the requested method
        
        Returns: A list in the form [function object, arg1, arg2,...,argn]
    """
    cmd = tokens.pop(0)
    cmd_target_name = tokens.pop(0)
    
    if not cmd.islower() or not cmd_target_name.islower():
        raise ValueError("Commands should be lowercase.")
 
    object = None
    #if cmd target is relation or class, we can get it directly from the diagram
    if cmd_target_name == 'relation' or cmd_target_name == 'class':
        object = getattr(d, cmd + '_' + cmd_target_name)

    else:
        #if cmd target isn't in the diagram, we know it is in a class. Get that class.
        object = getattr(d, 'get_class')(tokens.pop(0))
        if cmd_target_name == 'method' or cmd_target_name == 'field':
            object = getattr(object, cmd + '_' + cmd_target_name)
        #if cmd target isn't in a class, the only other place for it to be is in a method. 
        elif cmd_target_name == 'param':
            object = getattr(object, 'get_method')(tokens.pop(0))
            object = getattr(object, cmd + '_' + cmd_target_name)
        else: 
            raise ValueError("Invalid Command.")
    
    return [object] + tokens

