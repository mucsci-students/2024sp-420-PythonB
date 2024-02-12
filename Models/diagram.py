# Primary: Jill Daggs, Katie Dowlin
# Secondary: Danish Zubari, Patrick McCullough
# Last updated by Jill on February 9, 2024, at 5:35 PM.
class Diagram:
    # used_attribute_names = list()
    def __init__(self):
        self.classes = {}
        
    #Jill: A list of surface level commands    
    def command_help(self):
        return ("\nCommands:\n"
                "help                                                       Displays this menu\n"
                "help class                                                 Displays commands related to classes\n"
                "help attribute                                             Displays commands related to attributes\n"
                "help relationship                                          Displays commands related to relationships\n"
                "save <file_name>                                           Saves your UML diagram as a JSON file\n"
                "load <file_name>                                           Loads a UML diagram from a JSON file\n"
                "exit                                                       Exits the program\n")   
          
    #Jill: Commands for classes      
    def class_help(self):
        return ("\nClass Commands:\n"
                "help class                                                 Displays this menu\n"
                "add class <class_name>                                     Adds a class named <class_name>\n"
                "delete class <class_name>                                  Deletes class named <class_name> and all of its attributes/relationships\n"
                "rename class <current_name> <new_name>                     Renames class <current_name> to <new_name>\n"
                "list class <class_name>                                    Lists all atributes/relatioships pertaining to <class_name>\n"
                "list classes                                               Lists all classes in current UML\n")
    
    #Jill: Commands for attributes
    def attribute_help(self):
        return ("\nAttribute Commands:\n"
                "help attribute                                             Displays this menu\n"
                "add attribute <attribute_name> <class_name>                Adds attribute named <attribute_name>\n"               
                "delete attribute <attribute_name> <class_name>             Deletes attribute named <attribute_name>\n"
                "rename attribute <current_name> <new_name> <class_name>    Renames attribute <current_name> to <new_name>\n")
        
    #Jill: Commands for relationships
    def relationship_help(self):
        return ("\nRelationship Commands:\n"
                "help relationships                                         Displays this menu\n"
                "add relationship <src_class> <des_class> <relation_type>   Adds a relationship between <src_class> and <des_class> of <relation_type>: (Aggregation, Composition, Generalization, Inheritance)\n"
                "delete relationship <src_class> <des_class>                Deletes the relationship between <src_class> <des_class>\n"
                "list relationship <class_name>                             Lists all relationships to <class_name>\n")



    def name_checker(self, name):
        if not isinstance(name, str):
            print("Invalid name.")
            return False
        if len(name) == 0:
            print("Error! Empty name.")
            return False
        reserved_keywords = ["and", "as", "assert", "break", "continue", "class", "def", "del", "else", "finally",
                             "elif",
                             "except", "for", "from", "global", "if", "in", "is", "lambda", "import", "nonlocal",
                             "not",
                             "or", "pass", "print", "raise", "return", "try", "while", "with", "yield"]
        # Katie Dowlin: If the name the user entered is a reserved keyword in Python, then the name is invalid.
        if name in reserved_keywords:
            print("Invalid name! You cannot use a word that is a reserved word. ")
            return False
        # Katie Dowlin: If the name the user entered starts with a number, then the name is invalid.
        if name[0].isdigit():
            print("Invalid name! Name can not start with a number.")
            return False
        # Katie Dowlin: If the name the user entered doesn't start with a letter, it has to start with an underscore
        # to be valid.
        if not name[0].isalpha():
            if not name.startswith("_"):
                print("Invalid name. Name should start with a letter or underscore.")
                return False
        for x in name:
            # Katie Dowlin: If the name the user entered contains any special characters other than underscores, then
            # the name is invalid.
            if not x.isalnum() and not x == "_":
                print("Invalid name! Special characters are not allowed.")
                return False

            # Katie Dowlin: The name the user entered can't already be used for another class.
            if name in self.classes:
                print("Class already exists.")
                return False
        # Katie Dowlin: If the name the user entered passed all checks and isn't used, then the user can
        # use that name for the attribute or class.
        else:
            return True
    # Katie Dowlin: Method to check if a name of a class or attribute is valid. Returns True if the
    # name is valid, returns False if the name is invalid.
    # Katie Dowlin: Method should be called before adding a new class or attribute or renaming a class
    # or attribute.

