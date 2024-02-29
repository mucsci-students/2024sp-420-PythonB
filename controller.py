#Primary: Jillian Daggs
#Secondary: Patrick McCullough
#Last Updated: 2/11/24
import os

from Models.diagram import Diagram
from Models.classadd import UMLClass
#from Models.relationship import UMLRelationship
from Models.attribute import Attributes
from Models.saveload import SaveLoad


#Jill: initializes types of commands
class CLIController:
    def __init__(self, diagram, relationship, classes, attributes, save_load):
        self.classes = classes
        self.relationship = relationship
        self.attributes = attributes
        self.diagram = diagram
        self.save_load = save_load
        self.commands = {
            "help": self.help,
            "add" : self.add,
            "rename" : self.rename,
            "delete" : self.delete,
            "list" : self.list,
            "save" : self.save,
            "load" : self.load
        }

    #Jill: takes a class name as input, returns a dictionary from class name to dictionaries from 'Attribute' to a list of attributes and 'Relationship' to a list of relationships
    def class_breakdown(self, name):
        #Jill: a dict of all classes to their attributes
        all_classattributes = self.classes.list_class()
        #Jill: a list of all classes
        all_classes = self.classes.list_classes()
        #Jill: checks if 'name is a class
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

    def pretty_breakdown(self, name):
        #Jill: a dict of all classes to their attributes
        all_classattributes = self.classes.list_class()
        #Jill: a list of all classes
        all_classes = self.classes.list_classes()
        #Jill: checks if 'name is a class
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

            all_class_aspects = (f"\t{name}:\n"
                                 f"\tAttributes: {attributes}\n"
                                 f"\tRelationships: {class_relationships}\n")

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
            class_name = tokens[2]
            #Jill: adding a relationship does not call namechecker
            if type == "relationship":
                if len(tokens) >= 5:
                    dest = tokens[3]
                    r_type = tokens[4]
                    self.relationship.add_relationship(class_name,dest,r_type)
                else:
                    print("Missing arguments.")
            #Jill: Adding classes and attributes do
            elif self.diagram.name_checker(class_name):
                if type == "class":
                    #Jill: checks for capitalization

                    if class_name[0].isupper():
                        self.classes.add_class(class_name)

                    else:
                        print("Class names must start with capital letters.")
                if type == "attribute":
                    if len(tokens) >= 4:
                        attribute_name = tokens[3]
                        if self.diagram.name_checker(attribute_name):
                            self.attributes.add_attribute(class_name, attribute_name)
                    else:
                        print("Missing arguments.")

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
                    if newname[0].isupper():


                        self.classes.rename_class(oldname,newname)
                        # Zhang: will rename automatically now
                        #self.relationship.renamed_class(oldname,newname)
                    else:
                        print("Class names must start with capital letters.")
            elif type == "attribute":
                oldname = tokens[3]
                newname = tokens[4]
                    #Jill: Checks name
                if self.diagram.name_checker(newname):
                    if len(tokens) >= 5:
                        class_name = tokens[2]
                        self.attributes.rename_attribute(class_name, oldname, newname)
        else:
            print("Missing arguments.")


    #Jill: all varients of delete command
    def delete(self, tokens):
        if len(tokens) >= 3:
            type = tokens[1].lower()
            if type == "class":
                name = tokens[2]
                self.classes.delete_class(name)
                # Zhang: will remove automatically now
                #self.relationship.removed_class(name)
            elif len(tokens) >=4:
                if type == "attribute":
                    name = tokens[3]
                    classname = tokens[2]
                    self.attributes.delete_attribute(classname, name)
                elif type == "relationship":
                    name = tokens[2]
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
                all_classes = self.classes.list_classes()
                print("Classes:")
                for item in all_classes:
                    class_info = self.pretty_breakdown(item)
                    print(class_info)
            elif type == "class":
                if len(tokens) >= 3:
                    name = tokens[2]
                    print(self.class_breakdown(name))
                else:
                    print("Missing arguments.")
            elif type == "relationships" or type == "relationship":
                if len(tokens) >= 3:
                    name = tokens[2]
                    all_relationships = self.relationship.list_relationships()
                    class_relationships = []

                    for relation in all_relationships:
                        if name in relation:  # Check if name is in the list
                            class_relationships.append(relation)

                    print(class_relationships)
                else:
                    print(self.relationship.list_relationships())
        else:
            print("Missing arguments.")

    def save(self, tokens):
        if len(tokens) >= 2:
            name = tokens[1]

            all_classes = self.classes.list_classes()
            saveitem = {}
            for item in all_classes:
                # Jill: Update saveitem with each class's breakdown. Ensure updates don't overwrite each other.
                class_info = self.class_breakdown(item)
                saveitem.update(class_info)

            self.save_load.save(saveitem, name)


        elif len(tokens) <= 1:
            print("No filename provided.")
            # Protects against attempting to save a file without a filename. (2/15/24)


    def load(self, tokens):

        save_folder = 'save_folder'

        if len(tokens) >= 2:
            name = tokens[1]

            file_path = os.path.join(save_folder, name + ".json")

            if not os.path.exists(file_path):
                print("File does not exist.")
            # Protects against loading a file that does not exist. (2/15/24)

            else:
                saveitem = self.save_load.load(name)
                for classname, details in saveitem.items():  #Jill: iterating over items to get both key and value

                    if classname not in self.diagram.classes:
                        self.diagram.classes[classname] = {}
                    if "Attributes" in details:

                        self.diagram.classes[classname]["Attributes"] = details["Attributes"]
                    if "Relationships" in details:

                        self.relationship.relationships.extend(details["Relationships"])
        elif len(tokens) <= 1:
            print("No filename provided.")
            # Protects against attempting to loading a file without a filename. (2/15/24)


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
            user_input = input("Enter command or type 'help' for a list of commands: ").strip()
            if not self.execute_command(user_input):
                break


diagram = Diagram()
classes = UMLClass(diagram)
# Zhang: UMLClass will also initialize a relationship object by default
#relationship = UMLRelationship(classes)
relationship = classes.relationships
attributes = Attributes(classes)
saveload = SaveLoad()
diagram_cli = CLIController(diagram,relationship,classes, attributes, saveload)
diagram_cli.CLI()

