"""
Primary: Danish Zubari
secondary : Zhang
"""


class UMLClass:
    def __init__(self):
        # Danish: create an empty dictionary
        self.classes = {}

    # Danish: I'm writing this function to add a class name
    def addclass(self, name):
        # Danish: If the class name already exist it will print the "class name already exist"
        if name in self.classes:
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
    def rename(self, name, newname):
        # Danish: If the class does not exists, it will display "Class name does not exist."
        if name not in self.classes:
            print(f"{name} does not exist")
            return name

        # Danish: If the class exists, it will be renamed to the new name,
        # and the message "Class name renamed to new_name successfully" will be displayed
        if name in self.classes and newname not in self.classes:
            # Danish: If the class name exists, it will remove the old name and assign it a new name.
            self.classes[newname] = self.classes.pop(name)
            print(f"{name} renamed to {newname} successfully")
            return newname
        else:
            print(f"{newname} already exist ")
            return name

    # print all the classes using disctionary
    def listclass(self):
        return self.classes


# for my testing
"""
umlclass = UMLClass()
umlclass.addclass('Student')
umlclass.addclass('MID')
umlclass.addclass('')
umlclass.addclass('Grades')
umlclass.addclass('Student')
umlclass.rename('MID','Student1')
umlclass.rename('Grades','Student1')
umlclass.listclass()
print("all classes ", umlclass.listclass())
"""