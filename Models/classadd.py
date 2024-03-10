# Primary: Danish
# secondary : Zhang
# updated_version Feb 25, 2024
from Models.diagram import Diagram
from Models.relationship import UMLRelationship
from Models.errorHandler import ErrorHandler


class UMLClass:
    def __init__(self, diagram):
        # create object from diagram class
        self.diagram = diagram
        self.classes = self.diagram.classes
        self.relationships = UMLRelationship(self)
        
    # Danish: I'm writing this function to add a class name
    def add_class(self, name):
        # Danish: If the class name doesn't exist it will print the "class name added successfully"

        if self.diagram.name_checker(name):
            if name in self.classes:
                raise ValueError("Class already exists.")
            elif name not in self.classes:
                self.classes[name] = {'Fields': [], 'Methods': {}}
                print(f"Class '{name}' added successfully.")

    # Danish: I'm writing this function to delete a class name
    def delete_class(self, name):
        # Danish: if class is exist then it'll delete and display "class name deleted successfully
        if name in self.classes:
            del self.classes[name]
            # Zhang: make a function call to the relationship class
            self.relationships.removed_class(name)
            print(f"Class '{name}' deleted successfully.")
            # return name
        # Danish: if class is not exist then it'll  display "class name not exist
        elif name not in self.classes:
            raise ValueError(f"Unable to delete! Class '{name}' does not exist.")
            # print(f"{name} not exist, so we can not delete the class")
            # return name

    # Danish: I'm writing this function to rename a class
    def rename_class(self, name, newname):
        # Danish: If the class do not exist, it will display "Class name does not exist."
        if name not in self.classes:
            raise ValueError(f"Unable to rename! Class '{name}' does not exist.")
            # return None
        # Danish: If the newName already exists, or it's a reserved word, then it will display an error.
        elif not self.diagram.name_checker(newname) or newname in self.classes:
            raise ValueError(f"Unable to rename to '{newname}'.")
            # return None
        self.relationships.renamed_class(name, newname)
        self.classes[newname] = self.classes.pop(name)
        print(f"Class '{name}' renamed to '{newname}' successfully.")
        # return newname

    # print all the classes using list
    def list_classes(self):
        return list(self.classes.keys())

    def list_class(self):
        return self.classes

