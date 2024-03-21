from Models import *
from Views.cli_view import CLI_View
import re

cli_view = CLI_View()
def parse(d:UML_Diagram, input:str) -> list | str:
    tokens = check_args(input.split())
    
    if len(tokens) < 3 or tokens[0].lower() == 'list': 
        return short_command(d, tokens)
    else: 
        return get_instance(d, tokens)
    

def short_command(d:UML_Diagram, tokens:list[str]) -> list:
    """Parses all forms of the following commands, returning appropriate lists for each: 
        quit
        save
        load
        undo
        redo
        list
        help
    """
    cur_token = tokens.pop(0).lower()

    if cur_token == 'quit':
        import src.Controllers.controller
        return [getattr(src.Controllers.controller,"quit")]
    elif cur_token == 'save' or cur_token == 'load':
        return [getattr(uml_save_load, cur_token), d, tokens.pop(0)]
    elif cur_token == 'undo' or cur_token == 'redo':
        #TODO: return [getattr(UML_States, cur_token)]
        pass
    elif cur_token == 'list' or cur_token == 'help':
        #TODO: list needs to have the diagram in idx 1 to work right
            #TODO: TODO: to string methods need to be updated to work
        out = None
        if len(tokens) > 0:
            out = [getattr(cli_view, cur_token + '_' + tokens.pop(0).lower())] + tokens
        else:
            out = [getattr(cli_view, cur_token)]
        

def check_args (args:list[str]) -> list[str]: 
    """Makes sure every string in *args is valid"""
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
    for arg in args: 
        if not regex.match(arg):
            raise ValueError("Argument {0} is invalid.".format(arg))
    return args


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
    
    return [object] + tokens

#TODO: Length based parseing would probably be cleaner. EG:
#       1) take the first token. If it is quit, return it. If it is save or load, prep them and return 
#       2) take the second token and combine it with the first token. 
#       3) If the second token is relation, branch into an edge case for relations that just preps and returns
#       4) if there are only three tokens, call getattr on the diagram and append the third item to the list
#       5) if there are more than three tokens, call getattr on the result of 4 and call that result with the next item in the token list
#       6) if the second token is not param, repeat this process until len is 2.
#       7) if the second token is param, repeat this process until len is 1. 
#       NOTE: In cases 6 and 7, everything left on the list should be the params to the method call and there should now be an instance to call it on.

#NOTE: Group, I will likely do this over the weekend. I don't have time to do it now. This should also fix the list issues. 
    #There will be a few more branches than listed because list and help can both have either two or three tokens. 
        #also, help does not need the diagram and list does. 
