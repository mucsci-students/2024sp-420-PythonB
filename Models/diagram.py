class Diagram:
    # used_attribute_names = list()
    def __init__(self):
        self.classes = {}

    # used_class_names = list()

    def name_checker(self, name):
        if not isinstance(name, str):
            print("Invalid Name")
            return False
        if len(name) == 0:
            print("Invalid Name")
            return False
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
        # Katie Dowlin: If the name the user entered doesn't start with a capital letter, then the name is
        # not valid for a class.
        if not name[0].isupper():
            print("Invalid Name")
            return False
        for x in name:
            # Katie Dowlin: If the name the user entered contains any special characters other than underscores, then
            # the name is invalid.
            if not x.isalnum() and not x == "_":
                print("Invalid Name")
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

