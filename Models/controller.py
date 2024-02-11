from diagram import Diagram
from classadd import UMLClass
from relationship import UMLRelationship

class CLIController:
    def __init__(self, diagram, relationship, classes):
        self.classes = classes
        self.relationship = relationship
        self.diagram = diagram
        self.commands = {
            "help": self.help,
            "add" : self.add,
            "rename" : self.rename,
            "delete" : self.delete,
            "list" : self.list,
            # "save" : self.save,
            # "load" : self.load
            
        }
    
    def help (self, tokens):
        
        if len(tokens) == 1:
            print(self.diagram.command_help())
        else:
            type = tokens[1].lower()
            if type == "class" or type == "classes":
                print(self.diagram.class_help())
            elif type == "attribute" or type == "attributes":
                print(self.diagram.attribute_help())
            elif type == "relationship" or type == "relationships":
                print(self.diagram.relationship_help())


    def add (self, tokens):
        if len(tokens) >= 3:
            type = tokens[1].lower()
            name = tokens[2]
            if type == "relationship":
                if len(tokens) >= 5:
                    dest = tokens[3]
                    r_type = tokens[4]
                    self.relationship.add_relationship(name,dest,r_type)
                else:
                    print("Missing arguments.")
            elif self.diagram.name_checker(name):
                if type == "class":
                    if name.istitle():
                        self.classes.add_class(name)
                    else:
                        print("Class names must start with capital letters.")
                if type == "attribute":
                    #TODO 
                    print("TODO")
            else:
                print("Not a valid name.")
        else:
            print("Missing arguments.")
    

    def rename(self, tokens):
        if len(tokens) >= 4:
            type = tokens[1].lower()
            oldname = tokens[2]
            newname = tokens[3]
            if self.diagram.name_checker(newname):
                if type == "class":
                    if newname.istitle():
                        self.classes.rename_class(oldname,newname)
                    else:
                        print("Class names must start with capital letters.")
                elif type == "attribute":
                    #TODO
                    print("TODO")         
            else:
                print("Not a valid name.")
        else:
            print("Missing arguments.")    
                
                            
    def delete(self, tokens):
        if len(tokens) >= 3:
            type = tokens[1].lower()
            name = tokens[2]
            if type == "class":
                self.classes.delete_class(name) 
            elif type == "attribute":
                #TODO
                print("TODO")
            elif type == "relationship":
                if len(tokens) >=4:
                    dest = tokens[3]
                    self.relationship.delete_relationship(name,dest)
                else:
                    print("Missing arguments.")
        else:
            print("Missing arguments")

    def list(self,tokens):
        if len(tokens) >= 2:
            type = tokens[1]
            if type == "class":
                print(self.classes.list_class())
            elif type == "classes":
                #TODO
                print("TODO")
            elif type == "relationship" or type == "relationships":
                print(self.relationship.list_relationships())
        else:
            print("Missing arguments.")
            
                     
    def execute_command(self, user_input):
        tokens = user_input.split()
        if tokens:
            command = tokens[0].lower()
            if command in self.commands:
                self.commands[command](tokens)
            elif command == "exit":
                return False  # Signal to exit CLI
            else:
                print("Command not recognized.")
        return True  # Continue running CLI   
     
        
    def CLI(self):
        while True:
            user_input = input("Enter Command, or type 'help' for a list of commands: ").strip()
            if not self.execute_command(user_input):
                break
            
            
classes = UMLClass()
relationship = UMLRelationship(classes)
diagram = Diagram()
diagram_cli = CLIController(diagram,relationship,classes)
diagram_cli.CLI()
