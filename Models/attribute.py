from Models.diagram import Diagram


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
            # Katie Dowlin: If the class you want to add the attribute to doesn't exist.
            else:
                print("Add Failed- " + class_name + " Doesn't Exist")
                return name
        # Katie Dowlin: If the name is invalid.
        else:
            print("Add Failed- " + name + " Is Invalid")
            return name

    def delete_attribute(self, name, class_name):
        # Katie Dowlin: Check if class exists.
        if class_name in diagram.classes.keys():
            # Katie Dowlin: Check if an attribute with that name exists in that class.
            if name in diagram.classes[class_name]:
                diagram.classes[class_name].remove(name)
                print(name + " Deleted Successfully")
            # Katie Dowlin: If there is no attribute with that name in that class.
            else:
                print("Delete Failed-" + name + " Doesn't Exist")
                return name
        # Katie Dowlin: If the class doesn't exist.
        else:
            print("Delete Failed- " + class_name + " Doesn't Exist")
            return name


    def rename_attribute(self, old_name, new_name, class_name):
        # Katie Dowlin: Check if class exists.
        if class_name in diagram.classes.keys():
            # Katie Dowlin: Check if old name is an attribute in that class.
            if old_name in diagram.classes[class_name]:
                # Katie Dowlin: Check if new name is valid.
                if diagram.name_checker(self, new_name):
                    diagram.classes[class_name].remove(old_name)
                    diagram.classes[class_name].append(new_name)
                    print(old_name + " Has Been Renamed To " + new_name)
                    return new_name
                # Katie Dowlin: If the new name is invalid.
                else:
                    print("Rename Failed- " + new_name + " Is Invalid")
                    return old_name
            # Katie Dowlin: If the old name does not exist.
            else:
                print("Rename Failed- " + old_name + "Doesn't Exist")
        # Katie Dowlin: If the class doesn't exist.
        else:
            print("Rename Failed- " + class_name + "Doesn't Exist")
            return old_name
