#Primary: Jillian Daggs
#Secondary: Patrick McCullough
#Last Updated: 2/11/24


from diagram import Diagram
from classadd import UMLClass
from relationship import UMLRelationship


#Jill: initializes types of commands
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
        
    #Jill: takes a class name as input, returns a dictionary from class name to dictionaries from 'Attribute' to a list of attributes and 'Relationship' to a list of relationships
    def class_breakdown(self, name):
        #Jill: a dict of all classes to their attributes
        all_classattributes = self.classes.list_class()
        #Jill: a list of all classes
        all_classes = self.classes.list_classes()
        #Jill: checks if 'name' is a class
        if name in all_classes:
            #Jill: uses 'name' as a key to access attributes
            attributes = all_classattributes[name]
            all_relationships = self.relationship.list_relationships()
            #an empty list to fill with relationships containing 'name'
            class_relationships = []
            
            #loops over realtionships to find any/all relationships 'name' is a part of
            for relation in all_relationships:
                for item in relation:
                    if item == name:
                        class_relationships.append(relation)

            all_class_aspects = {name : {'Attributes' : attributes, 'Relationships' : class_relationships } }
            return all_class_aspects
        else:
            print (f"No class named {name}")
            
        
    #Jill: All varients of the help command 
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
                

    #Jill: All Varients of add command
    def add (self, tokens):
        if len(tokens) >= 3:
            type = tokens[1].lower()
            name = tokens[2]
            #Jill: adding a relationship does not call namechecker
            if type == "relationship":
                if len(tokens) >= 5:
                    dest = tokens[3]
                    r_type = tokens[4]
                    self.relationship.add_relationship(name,dest,r_type)
                else:
                    print("Missing arguments.")
            #Jill: Adding classes and attributes do
            elif self.diagram.name_checker(name):
                if type == "class":
                    #Jill: checks for capitalization
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
            
    
    #Jill: All varients of rename command
    def rename(self, tokens):
        if len(tokens) >= 4:
            type = tokens[1].lower()
            oldname = tokens[2]
            newname = tokens[3]
            #Jill: Checks name
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
               
                
    #Jill: all varients of delete command                       
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
            
            
    #Jill: all varients of list command
    def list(self,tokens):
        if len(tokens) >= 2:
            type = tokens[1]
            if type == "classes":
                print(self.classes.list_classes())
            elif type == "class":
                if len(tokens) >= 3:
                    name = tokens[2] 
                    print(self.class_breakdown(name))
                else:
                    print("Missing arguments.")
            elif type == "relationship" or type == "relationships":
                print(self.relationship.list_relationships())
        else:
            print("Missing arguments.")
            
    #Jill: checks commands against given list of commands, also handles exit                 
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
     
    #Jill: what the user interacts with
    def CLI(self):
        while True:
            user_input = input("Enter command, or type 'help' for a list of commands: ").strip()
            if not self.execute_command(user_input):
                break
            
            
classes = UMLClass()
relationship = UMLRelationship(classes)
diagram = Diagram()
diagram_cli = CLIController(diagram,relationship,classes)
diagram_cli.CLI()
