from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

class CLI:
    
    def __init__(self, controller):
        self.controller = controller
        self.setup_autocomplete()
        self.commands = {
            "help": self.help,
            "add" : self.controller.add,
            "rename" : self.controller.rename,
            "delete" : self.controller.delete,
            "list" : self.list,
            "save" : self.controller.save,
            "load" : self.controller.load
        }   

    def setup_autocomplete(self):
        self._completer = NestedCompleter.from_nested_dict({
        'add': {
            'class': None,
            'field': None,
            'method': None,
            'relationship': None
        },
        'delete': {
            'class': None,
            'field': None,
            'method': None,
            'relationship': None
        },
        'rename':{
            'class': None,
            'field': None,
            'method': None
        },
        'list':{
            'class': None,
            'classes': None,
            'relationship': None,
            'relationships': None
        },
        'save': None,
        'load': None,
        'exit': None
        })  
             
    #A list of surface level commands    
    def command_help(self):
        return ("\nCommands:\n"
                "help                                                           Displays this menu\n"
                "help class                                                     Displays commands related to classes\n"
                "help attribute                                                 Displays commands related to attributes\n"
                "help relationship                                              Displays commands related to relationships\n"
                "save <file_name>                                               Saves your UML diagram as a JSON file\n"
                "load <file_name>                                               Loads a UML diagram from a JSON file\n"
                "exit                                                           Exits the program\n")   
          
    #Commands for classes      
    def class_help(self):
        return ("\nClass Commands:\n"
                "help class                                                     Displays this menu\n"
                "add class <class_name>                                         Adds a class named <class_name>\n"
                "delete class <class_name>                                      Deletes class named <class_name> and all of its attributes/relationships\n"
                "rename class <current_name> <new_name>                         Renames class <current_name> to <new_name>\n"
                "list class <class_name>                                        Lists all attributes/relationships pertaining to <class_name>\n"
                "list classes                                                   Lists all classes in current UML\n")
    
    #Commands for attributes
    def attribute_help(self):
        return ("\nAttribute Commands:\n"
                "help attribute                                                 Displays this menu\n"
                "add field <class_name> <field_name>                            Adds field named <field_name>\n" 
                "add method <class_name> <method_name>                          Adds method named <method_name>\n"  
                "add parameter <class_name> <method_name> <param_name>          Adds param named <param_name> to method <method_name>\n"              
                "delete method <class_name> <method_name>                       Deletes method named <method_name>\n"
                "delete field <class_name> <field_name>                         Deletes field named <field_name>\n"
                "delete parameter <class_name> <method_name> <param_name>       Deletes param named <param_name> from <method_name>\n"
                "rename field <class_name> <current_name> <new_name>            Renames field <current_name> to <new_name>\n"
                "rename method <class_name> <current_name> <new_name>           Renames method <current_name> to <new_name>\n"
                "rename parameter <class_name> <method_name> <current_name> <new_name>          Renames param <current_name> in method\n"
                "   <method_name> to <new_name>\n")
        
    #Commands for relationships
    def relationship_help(self):
        return ("\nRelationship Commands:\n"
                "help relationships                                         Displays this menu\n"
                "add relationship <src_class> <des_class> <relation_type>   Adds a relationship between <src_class> and <des_class> of\n"
                "   <relation_type>: (Aggregation, Composition, Generalization, Inheritance)\n"
                "delete relationship <src_class> <des_class>                Deletes the relationship between <src_class> <des_class>\n"
                "list relationships                                         Lists all relationships\n"
                "list relationships <class_name>                            Lists all relationships to <class_name>\n")
        
        # All varients of the help command
    def help (self, tokens):

        if len(tokens) == 1:
            print(self.command_help())
        else:
            type = tokens[1].lower()
            if type == "class" or type == "classes":
                print(self.class_help())
            elif type == "attribute" or type == "attributes":
                print(self.attribute_help())
            elif type == "relationship" or type == "relationships":
                print(self.relationship_help())
            
        
    def list (self,tokens):
        print(self.controller.list(tokens))
        
        
    # checks commands against given list of commands, also handles exit
    def execute_command(self, user_input):
        tokens = user_input.split()
        if tokens:
            command = tokens[0].lower()
            if command in self.commands:
                self.commands[command](tokens)
            #Exits
            elif command == "exit":
                return False  # Signal to exit CL
            else:
                print("Command not recognized.")
        return True  # Continue running CLI

        
    # what the user interacts with
    def get_input(self):
        while True:
            user_input = prompt("Enter command or type 'help' for a list of commands: ", completer=self._completer).strip()
            if not self.execute_command(user_input):
                break
    