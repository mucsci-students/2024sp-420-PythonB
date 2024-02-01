class Diagram:
    def __init__(self):
        self
    # Katie Dowlin: Method to check if a name of an attribute is valid. Returns True if the name is valid, returns False if
    # the name is invalid.
    def attribute_name_checker(name):
        if not type(name) == str:
            print("Invalid Name")
            return False
        used_attribute_names = list()
        reserved_keywords = ["and", "as", "assert", "break", "continue", "class", "def", "del", "else", "finally",
                             "elif",
                             "except", "for", "from", "global", "if", "in", "is", "lambda", "import", "nonlocal",
                             "not",
                             "or", "pass", "print", "raise", "return", "try", "while", "with", "yield"]
        # Katie Dowlin: If the name the user entered is a reserved keyword in Python, then the name is invalid.
        if name in reserved_keywords:
            print("Invalid Name")
            return False
        # Katie Dowlin: If the name the user entered starts with a number, then the name is invalid.
        if name[0].isdigit():
            print("Invalid Name")
            return False
        # Katie Dowlin: If the name the user entered doesn't start with a letter, it has to start with an underscore
        # to be valid.
        if not name[0].isalpha():
            if not name.startswith("_"):
                print("Invalid Name")
                return False
        for x in name:
            # Katie Dowlin: If the name the user entered contains any special characters other than underscores, then
            # the name is invalid.
            if not x.isalnum() and not x == "_":
                print("Invalid Name")
                return False
        # Katie Dowlin: The name the user entered can't already be used for another attribute.
        if name in used_attribute_names:
            print("Attribute Already Exists")
            return False
        # Katie Dowlin: If the name the user entered isn't used, then the user can use that name for the attribute and
        # the name should be added to the list of used names.
        else:
            used_attribute_names.append(name)
            return True



    # Katie Dowlin: Method to check if a name of a class is valid. Returns True if the name is valid, returns False if
    # the name is invalid.
    def class_name_checker(name):
        if not type(name) == str:
            print("Invalid Name")
            return False
        # Katie Dowlin: Empty list to add to when we use a new name.
        used_class_names = list()
        reserved_keywords = ["and", "as", "assert", "break", "continue", "class", "def", "del", "else", "finally",
                             "elif",
                             "except", "for", "from", "global", "if", "in", "is", "lambda", "import", "nonlocal", "not",
                             "or", "pass", "print", "raise", "return", "try", "while", "with", "yield"]
        # Katie Dowlin: If the name the user entered is a reserved keyword in Python, then the name is invalid.
        if name in reserved_keywords:
            print("Invalid Name")
            return False
        # Katie Dowlin: If the name the user entered starts with a number, then the name is invalid.
        if name[0].isdigit():
            print("Invalid Name")
            return False
        # Katie Dowlin: If the name the user entered doesn't start with a letter, it has to start with an underscore
        # to be valid.
        if not name[0].isalpha():
            if not name.startswith("_"):
                print("Invalid Name")
                return False
        # Katie Dowlin: If the name the user entered doesn't start with a capital letter, then the name is invalid
        if not name[0].isupper():
            print("Invalid Name")
            return False
        for x in name:
            # Katie Dowlin: If the name the user entered contains any special characters other than underscores, then
            # the name is invalid.
            if not x.isalnum() and not x == "_":
                print("Invalid Name")
                return False
        # Katie Dowlin: The name the user entered can't already be used for another attribute.
        if name in used_class_names:
            print("Class Already Exists")
            return False
        # Katie Dowlin: If the name the user entered isn't used, then the user can use that name for the attribute and
        # the name should be added to the list of used names.
        else:
            used_class_names.append(name)
            return True
