import sys
import re
import os
from pathlib import Path

from Controllers.cli_controller import CLI_Controller
from Controllers.gui_controller import GUI_Controller
from Models.uml_diagram import UML_Diagram
from Models.uml_undo_redo import UML_States
from Models.uml_save_load import json_to_diagram, diagram_to_json


class UML_Controller:

    def __init__(self):
        """
        Initializes the instance with either a CLI_Controller or GUI_Controller based on user choice
        """
        self._controller:CLI_Controller | GUI_Controller = self.__pick_controller()
        self._diagram = UML_Diagram()
        self._states = UML_States(self._diagram)
        self._should_quit = False

    def run(self):
        """Executes the main loop of the program"""
        while not self._should_quit:
            try: 
                data = self.parse(self._controller.request_update())
                ret = data[0](*data[1:])
                if isinstance(ret, str) and isinstance(self._controller, CLI_Controller):
                    print(ret) 
                # For now this is only for undo/redo
                if isinstance(ret, UML_Diagram):
                    self._diagram = ret
                # For now this will ensure the state is not saved
                #     when doing list commands(commands that starts with 'list' prefix)
                elif not data[0].__name__.startswith('list'):
                    self._states.save_state(self._diagram)
            except KeyboardInterrupt:
                self.quit()
            except EOFError:
                self.quit()
            except Exception as e:
                print(str(e))
                self._states.undo()   
                continue
            self._controller.draw(self._diagram)

    def __pick_controller(self, args:str = sys.argv) -> CLI_Controller | GUI_Controller: 
        if len(args) > 1 and str(args[1]).strip().lower() == 'cli':
            return CLI_Controller()
        return GUI_Controller()
    
    def quit(self):
        #TODO: Make an actual quit routine
        self._should_quit = True

    def save(self, filename:str):
        """ Saves this controller's diagram to the provided filename 
            NOTE: Overwrites an existing file with the same name
        """
        jsoned = diagram_to_json(self._diagram)
        path = os.path.join(os.path.dirname(__file__), '../', '../', 'saves')
        if not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(path, filename + '.json')
        file = open(path, "w")
        file.write(jsoned)
        file.close()

    def load(self, filename:str):
        path = os.path.join(os.path.dirname(__file__), '../', '../', 'saves')
        if not os.path.exists(path):
            raise ValueError("No file named {0}.json exists in the save folder.".format(filename))
        path = os.path.join(path, filename + '.json')
        self._diagram.replace_content(json_to_diagram(Path(path).read_text()))

#=========================Parseing=========================#  
    def parse(self, input:str) -> list | str:
        tokens = self.check_args(input.split())
        
        if len(tokens) < 3 or tokens[0] == 'list': 
            return self.short_command(tokens)
        else: 
            return self.instance_command(tokens)
        
    def short_command(self, tokens:list[str]) -> list:
        """Parses all forms of the following commands, returning appropriate lists for each: 
            quit, save, load, undo, redo, list, help
        """
        cur_token = tokens.pop(0)
        match cur_token: 
            case 'quit':
                return [self.quit]
            case 'save' | 'load':
                return [getattr(self, cur_token), tokens.pop(0)]
            case 'undo' | 'redo':
                return [getattr(self._states, cur_token)]
            case 'list':
                return self._controller.parse_list_cmd(self._diagram, tokens)
            case 'help':
                return self._controller.parse_help_cmd(tokens)
            case _:
                raise ValueError("Invalid command.")

    def check_args (self, args:list[str]) -> list[str]: 
        """Makes sure every string in args is valid
            Valid names match the following regex: ^[a-zA-Z][a-zA-Z0-9_]*$
        """
        regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
        for arg in args: 
            if not regex.match(arg):
                raise ValueError("Argument {0} is invalid.".format(arg))
        return args

    def instance_command(self, tokens:list[str]) -> list:
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
        
        if cmd == 'rename':
            return self.__handle_rename([cmd_target_name] + tokens)

        object = None
        #if cmd target is relation or class, we can get it directly from the diagram
        if cmd_target_name == 'relation' or cmd_target_name == 'class':
            object = getattr(self._diagram, cmd + '_' + cmd_target_name)

        elif cmd_target_name == 'method' or cmd_target_name == 'field' or cmd_target_name == 'param':
            #if cmd target isn't in the diagram, we know it is in a class. Get that class.
            object = self._diagram.get_class(tokens.pop(0))
            if cmd_target_name == 'method' or cmd_target_name == 'field':
                object = getattr(object, cmd + '_' + cmd_target_name)
            #if cmd target isn't in a class, the only other place for it to be is in a method. 
            elif cmd_target_name == 'param':
                object = object.get_method(tokens.pop(0))
                object = getattr(object, cmd + '_' + cmd_target_name)
            else: 
                raise ValueError("Invalid Command.")
        else:
            raise ValueError("Invalid Command.")
        return [object] + tokens
    
    def __handle_rename(self, tokens:list[str]):
        """Rename has different logic from the rest of the methods, handle it separately.
        
            Raises:
            ValueError - attempt to rename an item that doesn't support renaming
            ValueError - provided too many or too few arguments

            Returns: 
            A list in the form [function object, arg1, ..., argn]
        """
        #this is the name of the object being renamed
        cmd_target_name = tokens.pop(0)
        match cmd_target_name: 
            case 'class':
                old_name = tokens.pop(0)
                self.__check_duplicate_item(tokens[0], self._diagram.get_all_classes())
                cl = self._diagram.get_class(old_name)
                return [cl.set_name, tokens[0]]
            case 'method' | 'field':
                cl = self._diagram.get_class(tokens.pop(0))
                obj = getattr(cl, 'get_' + cmd_target_name)(tokens.pop(0))
                obj_list = getattr(cl, 'get_' + cmd_target_name + 's')()
                self.__check_duplicate_item(tokens[0], obj_list)
                return [obj.set_name, tokens.pop(0)]     
            case 'param':
                 cl = self._diagram.get_class(tokens.pop(0))
                 mthd = cl.get_method(tokens.pop(0))
                 param = mthd.get_param(tokens.pop(0))
                 self.__check_duplicate_item(tokens[0], mthd.get_params())
                 return [param.set_name, tokens.pop(0)]
            case _: 
                raise ValueError ("Invalid target for rename.")
                
    def __check_duplicate_item (self, i_name:str, search_loc:list):
        """Makes sure that no class with name c_name exists in the diagram
        
            Raises: 
            ValueError - an item with name i_name exists in search_loc already
        """
        cl = next((item for item in search_loc if item.get_name() == i_name), None)
        if cl is not None:
            raise ValueError("{0} already exists.".format(i_name))


    

    