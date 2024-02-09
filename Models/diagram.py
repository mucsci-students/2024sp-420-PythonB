# Primary: Jillian Daggs, Katie Dowlin
# Secondary: Danish Zubari
# Last updated by Jillian on February 9, 2024, at 5:35 PM.
from Models.addclass import UMLClass
from Models.relationship import Relationship

class Diagram:
    # used_attribute_names = list()
    def __init__(self):
        self.classes = {}
        
    def command_help(self):
        return ("Commands:"
                "help                                                       Displays this menu"
                "help class                                                 Displays commands related to classes"
                "help attribute                                             Displays commands related to attributes"
                "help relationship                                          Displays commands related to relationships"
                "save                                                       Saves your UML diagram as a JSON file"
                "load                                                       Loads a UML diagram from a JSON file"
                "exit                                                       Exits the program")      
        
    def class_help(self):
        return ("Commands:"
                "help class                                                 Displays this menu"
                "add class <class_name>                                     Adds a class named <class_name>"
                "delete class <class_name>                                  Deletes class named <class_name> and all of its attributes/relationships"
                "rename class <current_name> <new_name>                     Renames class <current_name> to <new_name>"
                "list class <class_name>                                    Lists all atributes/relatioships pertaining to <class_name>"
                "list classes                                               Lists all classes in current UML")
    
    #TODO after katie finishes attributes
    def attribute_help(self):
        return ("Commands:"
                "help attribute                                             Displays this menu"
                "add attribute <attribute_name>                             Adds attribute named <attribute_name>"               
                "delete attribute <attribute_name>                          Deletes attribute named <attribute_name>"
                "rename attribute <current_name> <new_name>                 Renames attribute <current_name> to <new_name>"                 
                "list attribute                                             Lists all attributes in class")
    
    def relationship_help(self):
        return ("Commands:"
                "help relationships                                         Displays this menu"
                "add relationship <src_class> <des_class> <relation_type>   Adds a relationship between <src_class> and <des_class>"
                "delete relationship <src_class> <des_class>                Deletes the relationship between <src_class> <des_class>"
                "list relationship <class_name>                             Lists all relationships to <class_name>")

    def name_checker(self, name):
        if not isinstance(name, str):
            print("Invalid Name")
            return False
        if len(name) == 0:
            print("Error! Empty name")
            return False
        reserved_keywords = ["and", "as", "assert", "break", "continue", "class", "def", "del", "else", "finally",
                             "elif",
                             "except", "for", "from", "global", "if", "in", "is", "lambda", "import", "nonlocal",
                             "not",
                             "or", "pass", "print", "raise", "return", "try", "while", "with", "yield"]
        # Katie Dowlin: If the name the user entered is a reserved keyword in Python, then the name is invalid.
        if name in reserved_keywords:
            print("Invalid Name! You cannot use a word that is a reserved word. ")
            return False
        # Katie Dowlin: If the name the user entered starts with a number, then the name is invalid.
        if name[0].isdigit():
            print("Invalid Name! Name can not start with a number")
            return False
        # Katie Dowlin: If the name the user entered doesn't start with a letter, it has to start with an underscore
        # to be valid.
        if not name[0].isalpha():
            if not name.startswith("_"):
                print("Invalid Name! Name should start with a letter or underscore")
                return False
        # Katie Dowlin: If the name the user entered doesn't start with a capital letter, then the name is
        # not valid for a class.
        if not name[0].isupper():
            print("Invalid Name! Name should start with a Capital Letter")
            return False
        for x in name:
            # Katie Dowlin: If the name the user entered contains any special characters other than underscores, then
            # the name is invalid.
            if not x.isalnum() and not x == "_":
                print("Invalid Name! Special Characters not allowed")
                return False

            # Katie Dowlin: The name the user entered can't already be used for another class.
            if name in self.classes:
                print("Class Already Exists")
                return False
        # Katie Dowlin: If the name the user entered passed all checks and isn't used, then the user can
        # use that name for the attribute or class.
        else:
            return True
    # Katie Dowlin: Method to check if a name of a class or attribute is valid. Returns True if the
    # name is valid, returns False if the name is invalid.
    # Katie Dowlin: Method should be called before adding a new class or attribute or renaming a class
    # or attribute.



 #*************************************************************CLI*************************************************************************
    def CLI(self):
        userinput = 0
        while userinput != "exit":
            userinput = input("Enter Command, or type 'help' for a list of commands\n")            
            tokens = userinput.split()
            if tokens[0] == "help" or tokens[0] == "Help" or tokens[0] == "h":
                if tokens[1] == "":
                    self.command_help()
                elif tokens[1] == "class" or tokens[1] == "Class":
                    self.class_help()
                elif tokens[1] == "attribute" or tokens[1] == "Attribute" or tokens[1] == "attributes" or tokens[1] == "Attributes":
                    self.attribute_help()
                elif tokens[1] == "relationship" or tokens[1] == "Relationship":
                    self.relationship_help()
                else:
                    print("Command not recognized\n")
                    self.CLI()
            elif tokens[0] == "add" or tokens[0] =="Add":
                if tokens[1] == "class" or tokens[1] == "Class":
                    UMLClass.add_class(tokens[2])
                elif tokens[1] == "attribute" or tokens[1] == "Attribute":
                    #TODO when attribute is done
                    print("TODO")
                elif tokens[1] == "relationship" or tokens[1] == "Relationship":
                    Relationship.add_relationship(tokens[2],tokens[3],tokens[4])
                else:
                    print("Command not recognized\n")
                    self.CLI()
            elif tokens[1] == 
                    
                                                       