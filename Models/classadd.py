# Primary: Danish
# secondary : Zhang
# updated_version Feb 25, 2024
from Models.diagram import Diagram
from Models.relationship import UMLRelationship
from Models.errorHandler import ErrorHandler


class UMLClass:
    def __init__(self, diagram):
        # Danish: create an empty dictionary
        # self.classes = {}
        # self.relationships = relationships

        # create object from diagram class
        self.diagram = diagram
        self.classes = self.diagram.classes
        self.relationships = UMLRelationship(self)
    # Danish: I'm writing this function to add a class name
    def add_class(self, name):
        # Danish: If the class name doesn't exist it will print the "class name added successfully"
        """if name in self.classes:
            print(f"{name} already exist")
            return name
            # Danish: If the class name doesn't exist it will print the "class name added successfully"
        if name not in self.classes:
            if len(name) == 0:
                print("invalid name")
                return name
            else:
                self.classes[name] = {}
                print(f"{name} added successfully")
                return name
        """
        if self.diagram.name_checker(name):
            if name in self.classes:
                raise ValueError("Class already exists.")
            elif name not in self.classes:
                self.classes[name] = {'Fields': [], 'Methods': []}
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

    # Danish: I'm writing this function to rename a clas
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



'''
Zhang: testing
dia = Diagram()
some_class = UMLClass(dia)
some_class.add_class('Csci')
some_class.add_class('MU')
some_relationship = some_class.relationships
some_class.relationships.add_relationship(src='Csci', des='MU', type_rel='Composition')
some_class.rename_class('Csci', 'CS')
print(some_class.relationships.list_relationships())
some_class.delete_class('CS')
print(some_relationship.list_relationships())
#some_relationship.delete_relationship('CS', 'MU')
#print(some_relationship.list_relationships())
'''
# for my testing
'''umlclass.add_class('Cla ss')
umlclass.add_class('Student')
umlclass.add_class('1hello')
umlclass.add_class('Dani')
umlclass.add_class('MID')
umlclass.add_class('')
umlclass.add_class('assert')
umlclass.add_class('class')
umlclass.add_class('Grades')
umlclass.add_class('Student')
umlclass.add_class('Student')

umlclass.add_class(' ')
print("all classes after adding ", umlclass.list_class())
umlclass.rename_class('MID', 'Student1')
umlclass.rename_class('Grades', 'Student1')
umlclass.rename_class('Grades', 'class')
umlclass.rename_class('Dani', 'Student1')
print("all classes after rename ", umlclass.list_class())
umlclass.delete_class('Student')
print("all classes after delete ", umlclass.list_class())'''

# umlclass = UMLClass()
# umlclass.add_class('Cla ss')
# umlclass.add_class('Student')
# umlclass.add_class('1hello')
# umlclass.add_class('Dani')
# umlclass.add_class('MID')
# umlclass.add_class('')
# umlclass.add_class('assert')
# umlclass.add_class('class')
# umlclass.add_class('Grades')
# umlclass.add_class('Student')
# umlclass.add_class('Student')

# umlclass.add_class(' ')
# print("all classes after adding ", umlclass.list_class())
# umlclass.rename_class('MID', 'Student1')
# umlclass.rename_class('Grades', 'Student1')
# umlclass.rename_class('Grades', 'class')
# umlclass.rename_class('Dani', 'Student1')
# print("all classes after rename ", umlclass.list_class())
# umlclass.delete_class('Student')
# print("all classes after delete ", umlclass.list_class())