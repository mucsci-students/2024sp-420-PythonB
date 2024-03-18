from Models import *
from Views.cli_view import CLI
import re

classes = [UML_Diagram, UML_Class, UML_Relation, UML_Method, UML_Field, UML_Param, CLI()]

def parse(d:UML_Diagram, input:str) -> list:
    tokens = check_args(input.split())

    unbound_func = lookup_func(tokens) 
    
    #Steps: 
        #flookup
        #list creation
        #return
    

def check_args (*args:str) -> list[str]:
    '''Makes sure every string in *args is valid'''
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
    for arg in [*args]: 
        if not regex.match(arg):
            raise ValueError("{0} is not valid, please try again.".format(arg))
    return [*args]

def lookup_func(d:UML_Diagram, tokens:list[str]) -> function | None:
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
        else:
            suffix = tokens[0].lower()
            func = __find_class(cmd + '_' + suffix)
    return func

def __find_class(d:UML_Diagram, item:str):
    return next((getattr(f, item) for f in classes if hasattr(f, item)), __error(item))

def __find_instance(cmd:str, tokens:list[str]):
    pass


def __error(value:str):
    raise ValueError("{0} is not a valid command.".format(value))