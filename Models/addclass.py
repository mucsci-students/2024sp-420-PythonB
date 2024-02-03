# Primary: Danish
# secondary : Zhang
from namechecker import *


class UMLClass:
    def __init__(self):
        # Danish: create an empty dictionary
        self.classes = {}
        # create object from diagram class
        self.diagram = Diagram()
    # Danish: I'm writing this function to add a class name

    def add_class(self, name):
        # Danish: If the class name doesn't exist it will print the "class name added successfully"
        if self.diagram.class_name_checker(name):
            self.classes[name] = []
            print(f"{name} added successfully")
            return name

    # Danish: I'm writing this function to delete a class name
    def delete_class(self, name):
        # Danish: if class is exist then it'll delete and display "class name deleted successfully
        if name in self.classes:
            del self.classes[name]
            print(f"{name} deleted successfully")
            return name
        # Danish: if class is not exist then it'll  display "class name not exist
        if name not in self.classes:
            print(f"{name} not exist")
            return name

    # Danish: I'm writing this function to rename a class
    def rename_class(self, name, newname):
        # Danish: If the class do not exist, it will display "Class name does not exist."
        if name not in self.classes:
            print(f"{name} does not exist")
            return name

        # Danish: If the class exists, it will be renamed to the new name,
        # and the message "Class name renamed to new_name successfully" will be displayed
        # Danish: If the class name exists, it will remove the old name and assign it a new name.
        if self.diagram.class_name_checker(newname):
            self.classes[newname] = self.classes.pop(name)
            print(f"{name} renamed to {newname} successfully")
            return newname
        else:
            print(f"{newname} already exist ")
            return name

    # print all the classes using list
    def list_class(self):
        return self.classes


# for my testing
"""
umlclass = UMLClass()
umlclass.add_class('Student')
umlclass.add_class('MID')
umlclass.add_class('')
umlclass.add_class('assert')
umlclass.add_class('class')
umlclass.add_class('Grades')
umlclass.add_class('Student')
umlclass.add_class('Student')
umlclass.add_class(' ')
print("all classes after adding ", umlclass.list_class())
umlclass.rename_class('MID','Student1')
umlclass.rename_class('Grades','Student1')
umlclass.rename_class('Ali','Danish')
print("all classes after rename ", umlclass.list_class())
umlclass.delete_class('Student')
print("all classes after delete ", umlclass.list_class())
"""