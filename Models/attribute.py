from diagram import *


class Attributes:
    def __init__(self):
        self.diagram = Diagram()

    def add_attribute(self, name, class_name):
        # Katie Dowlin: Check if the name is valid.
        if diagram.name_checker(self, name):
            # Katie Dowlin: Check if the class you want to add the attribute to exists.
            if class_name in diagram.classes.keys():
                diagram.classes[class_name].append(name)
                print(name + " Added Successfully")
                return name
            else:
                print("Add Failed- " + class_name + " Doesn't Exist")
                return name

        else:
            print("Add Failed- " + name + " Is Invalid")
            return name

    def delete_attribute(self, name, class_name):
        if class_name in diagram.classes.keys():
            if name in diagram.classes[class_name]:
                diagram.classes[class_name].remove(name)
                print(name + " Deleted Successfully")
            else:
                print("Delete Failed-" + name + " Doesn't Exist")
                return name
        else:
            print("Delete Failed- " + class_name + " Doesn't Exist")
            return name

    def rename_attribute(self, old_name, new_name, class_name):
        if class_name in diagram.classes.keys():
            if old_name in diagram.classes[class_name]:
                if diagram.name_checker(self, new_name):
                    diagram.classes[class_name].remove(old_name)
                    diagram.classes[class_name].append(new_name)
                    print(old_name + " Has Been Renamed To " + new_name)
                    return new_name
                else:
                    print("Rename Failed- " + new_name + " Is Invalid")
                    return old_name
            else:
                print("Rename Failed- " + old_name + "Doesn't Exist")
        else:
            print("Rename Failed- " + class_name + "Doesn't Exist")
            return old_name
