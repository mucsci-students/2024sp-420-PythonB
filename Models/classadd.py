# Primary: Danish
# secondary : Zhang
# updated_version Feb 10,2024
from diagram import Diagram
from relationship import UMLRelationship


class UMLClass:
    def __init__(self, diagram):
        # Danish: create an empty dictionary
        # self.classes = {}
        # self.relationships = relationships

        # create object from diagram class
        self.diagram = diagram
        self.classes = self.diagram.classes
        self.relationships = UMLRelationship(self.classes)
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
            print(f"Unable to delete! {name} Class does not exist")
            # print(f"{name} not exist, so we can not delete the class")
            return name

    # Danish: I'm writing this function to rename a class
    def rename_class(self, name, newname):
        # Danish: If the class do not exist, it will display "Class name does not exist."
        if name not in self.classes:
            print(f"Unable to rename! {name} Class does not exist")
            return None
        # Danish: If the newName already exists, or it's a reserved word, then it will display an error.
        if not self.diagram.name_checker(newname) or newname in self.classes:
            print(f"Unable to rename! {newname}")
            return None

        self.classes[newname] = self.classes.pop(name)
        print(f"{name} renamed to {newname} successfully")
        return newname

    # print all the classes using list
    def list_classes(self):
        return list(self.classes.keys())
    
    def list_class(self):
        return self.classes


# Zhang: testing
'''
umlclass = UMLClass()
umlrelation = UMLRelationship(umlclass)

umlclass.add_class('CS')
umlclass.add_class('BIO')
umlrelation.add_relationship('CS','BIO','Aggregation')

umlclass.add_class('Apple')
umlclass.add_class('Banana')
umlrelation.add_relationship('Apple','Banana','Aggregation')
print("===============================")
umlclass.rename_class('CS','CSCI')
umlrelation.renamed_class('CS','CSCI')

umlclass.delete_class('Banana')
umlrelation.removed_class('Banana')


print(umlrelation.list_relationships())
print(umlclass.list_class())

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
=======
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