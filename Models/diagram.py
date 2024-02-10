# Primary: Jill Daggs, Katie Dowlin
# Secondary: Danish Zubari, Patrick McCullough
# Last updated by Jill on February 9, 2024, at 5:35 PM.
from addclass import UMLClass
from relationship import Relationship

class Diagram:
    # used_attribute_names = list()
    def __init__(self):
        self.classes = {}
        
    #Jill: A list of surface level commands    
    def command_help(self):
        return ("Commands:"
                "help                                                       Displays this menu"
                "help class                                                 Displays commands related to classes"
                "help attribute                                             Displays commands related to attributes"
                "help relationship                                          Displays commands related to relationships"
                "save                                                       Saves your UML diagram as a JSON file"
                "load                                                       Loads a UML diagram from a JSON file"
                "exit                                                       Exits the program")      
    #Jill: Commands for classes      
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
    #Jill: Commands for relationships
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
        #Jill: closes loop when 'exit'
        while userinput != "exit":
            userinput = input("Enter Command, or type 'help' for a list of commands\n") 
            #Jill: Splits input into tokens           
            tokens = userinput.split()
            #Jill:All versions of help command
            if tokens[0] == "help" or tokens[0] == "Help" or tokens[0] == "h":
                #Jill: Checks that token list contains only one token
                if len(tokens) == 1:
                    print(self.command_help())
                elif tokens[1] == "class" or tokens[1] == "Class" or tokens[1] == "classes" or tokens[1] == "Classes":
                    print(self.class_help())
                elif tokens[1] == "attribute" or tokens[1] == "Attribute" or tokens[1] == "attributes" or tokens[1] == "Attributes":
                    print(self.attribute_help())
                elif tokens[1] == "relationship" or tokens[1] == "Relationship" or tokens[1] == "relationship" or tokens[1] == "Relationships":
                    print(self.relationship_help())
                else:
                    print("Command not recognized\n")
                    self.CLI()
                    
            #Jill: All versions of add command
            elif tokens[0] == "add" or tokens[0] =="Add":
                name = tokens[2] 
                #Jill: Calls namechecker
                if self.name_checker(name):
                    #Class
                    if tokens[1] == "class" or tokens[1] == "Class":
                        #Jill: checks for capitalization 
                        if name.istitle():
                            UMLClass.add_class(self,tokens[2])
                        else:
                            print("Class names must start with capital letters, try again\n")                           
                    #Attribute
                    elif tokens[1] == "attribute" or tokens[1] == "Attribute":
                        #TODO when attribute is done
                        print("TODO")
                    #Relationship
                    elif tokens[1] == "relationship" or tokens[1] == "Relationship":
                        Relationship.add_relationship(self,tokens[2],tokens[3],tokens[4])
                    else:
                        print("Command not recognized\n")
                        self.CLI()
                else:
                    print("Name not valid, try again\n")
                    
            #Jill: All versions of delete command
            elif tokens[0] == 'delete' or tokens[0]== "Delete":
                #Class
                if tokens[1] == "class" or tokens[1] == "Class":
                    UMLClass.delete_class(self, tokens[2])
                #Attribute
                elif tokens[1] == "attribute" or tokens[1] == "Attribute":
                    #TODO when attribute is done
                    print("TODO")
                #Relationship
                elif tokens[1] == "relationship" or tokens[1] == "Relationship":
                    Relationship.delete_relationship(self, tokens[2], tokens[3])
                else:
                    print("Command not recognized\n")
                    self.CLI() 
                    
            #Jill: All versions of rename command
            elif tokens[0] == "rename" or tokens[0] == "Rename":
                new_name = tokens[3]
                old_name = tokens[2] 
                #Jill: Calls namechecker                                   
                if self.name_checker(new_name):
                    #Class
                    if tokens[1] == "class" or tokens[1] == "Class":
                        #Jill: Checks capitalization
                        if new_name.istitle:
                            UMLClass.rename_class(self,old_name,new_name)
                    #Attribute
                    elif tokens[1] == "attribute" or tokens[1] == "Attribute":
                        #TODO when katie finishes 
                        print("TODO")                                 
                else:
                    print("Name not valid, try again")
                    self.CLI() 
            #Jill: All versions of list command       
            elif tokens[0] == "list" or tokens[0] =="List":
                if tokens[1] == "class" or tokens[1] == "lass":
                    UMLClass.list_class()
                
        print("Exiting, would you like to save?") 
    CLI()             