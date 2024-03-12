# Danish
# Zhang
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
        
    # I'm writing this function to add a class name
    def add_class(self, name):

        if self.diagram.name_checker(name):
            if name in self.classes:
                raise ValueError("Class already exists.")
            elif name not in self.classes:
                self.classes[name] = {'Fields': [], 'Methods': {}}
                return (f"Class '{name}' added successfully.")
                

    # I'm writing this function to delete a class name
    def delete_class(self, name):
        # if class is exist then it'll delete and display "class name deleted successfully
        if name in self.classes:
            del self.classes[name]
            # make a function call to the relationship class
            self.relationships.removed_class(name)
            return(f"Class '{name}' deleted successfully.")
            # return name
        # if class is not exist then it'll  display "class name not exist
        elif name not in self.classes:
            raise ValueError(f"Unable to delete! Class '{name}' does not exist.")
     

    # I'm writing this function to rename a class
    def rename_class(self, name, newname):
        # If the class do not exist, it will display "Class name does not exist."
        if name not in self.classes:
            raise ValueError(f"Unable to rename! Class '{name}' does not exist.")
            # return None
        # If the newName already exists, or it's a reserved word, then it will display an error.
        elif not self.diagram.name_checker(newname) or newname in self.classes:
            raise ValueError(f"Unable to rename to '{newname}'.")
            # return None
        self.relationships.renamed_class(name, newname)
        self.classes[newname] = self.classes.pop(name)
        return(f"Class '{name}' renamed to '{newname}' successfully.")
        # return newname

    # print all the classes using list
    def list_classes(self):
        return list(self.classes.keys())

    def list_class(self):
        return self.classes

