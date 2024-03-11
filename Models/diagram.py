# Primary: Jill Daggs, Katie Dowlin
# Secondary: Danish Zubari, Patrick McCullough
# Last updated by Jill on February 9, 2024, at 5:35 PM.
import keyword

class Diagram:
    def __init__(self):
        self.classes = {}

    # Katie Dowlin: Method to check if a name of a class, field, method, or parameter is valid.
    # Returns True if the name is valid, returns False if the name is invalid.
    # Katie Dowlin: Method should be called before adding a new class, field, method, or parameter
    # or renaming a class, field, method, or parameter.
    def name_checker(self, name):
        if not isinstance(name, str):
            raise ValueError("Invalid name.")
        if len(name) == 0:
            raise ValueError("Error! Empty name.")
        # Katie Dowlin: If the name the user entered is a reserved keyword in Python, then the name is invalid.
        if keyword.iskeyword(name):
            raise ValueError("Invalid name! You cannot use a word that is a reserved word. ")
        # Katie Dowlin: If the name the user entered starts with a number, then the name is invalid.
        if name[0].isdigit():
            raise ValueError("Invalid name! Name can not start with a number.")
        # Katie Dowlin: If the name the user entered doesn't start with a letter, it has to start with an underscore
        # to be valid.
        if not name[0].isalpha():
            if not name.startswith("_"):
                raise ValueError("Invalid name. Name should start with a letter or underscore.")
        for x in name:
            # Katie Dowlin: If the name the user entered contains any special characters other than underscores, then
            # the name is invalid.
            if not x.isalnum() and not x == "_":
                raise ValueError("Invalid name! Special characters are not allowed.")
        # Katie Dowlin: If the name the user entered passed all checks and isn't used, then the user can
        # use that name for the attribute or class.
        else:
            return True

