from Models import *
from Views.cli_view import CLI
import re

classes = [UML_Diagram, UML_Class, UML_Relation, UML_Method, UML_Field, UML_Param, CLI()]

def parse(d:UML_Diagram, input:str) -> list:
    tokens = check_args(input.split())

    if len(tokens) < 3:
        #TODO: account for save, load, quit, help. 
        return [short_commands(tokens)].extend(tokens)
    else:
        return [get_instance(d, tokens)].extend(tokens)
    

def check_args (*args:str) -> list[str]:
    '''Makes sure every string in *args is valid'''
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
    for arg in [*args]: 
        if not regex.match(arg):
            raise ValueError("{0} is not valid, please try again.".format(arg))
    return [*args]

def short_commands(tokens:list[str]):
    '''Finds the class that the command being called should be executed in
        
        Params: 
            tokens: a line of input that has been split on spaces into tokens
        
        Returns an unbound function object.

        NOTE: This method modifies tokens, specifically it always removes the first item.
    '''
    func = None
    cmd = tokens.pop(0).lower()
    if len(tokens) == 0: 
        func = __find_class(cmd)
    else:
        if cmd == 'save' | cmd == 'load':
            func = __find_class(cmd)
    return func

def __find_class(d:UML_Diagram, cmd:str):
    return next((getattr(f, cmd) for f in classes if hasattr(f, cmd)), __error(cmd))

def get_instance(d:UML_Diagram, tokens:list[str]) -> list:
    cmd = tokens.pop(0).lower()
    cmd_target_name = tokens.pop(0).lower()
    object = None
    if cmd_target_name == 'relation' or cmd_target_name == 'class':
        object = getattr(d, cmd + '_' + object)
    else: 
        object = getattr(d, 'get_class')(tokens.pop(0))
        if cmd_target_name == 'method' or cmd_target_name == 'field':
            object = getattr(object, cmd + '_' + cmd_target_name)
        elif cmd_target_name == 'param':
            object = getattr(object, 'get_method')(tokens.pop(0))
            object = getattr(object, cmd + '_' + cmd_target_name)
    return object


def __error(value:str):
    raise ValueError("{0} is not a valid command.".format(value))