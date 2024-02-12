from Models.diagram import Diagram


class Attributes:
    def __init__(self, diagram):
        self.diagram = diagram
        
    def add_attribute(self, name, class_name):
        # Katie Dowlin: Check if the class you want to add the attribute to exists.
        if class_name in self.diagram.classes.keys():
            self.diagram.classes[class_name].append(name)
            print(f"Attribute '{name}' added successfully.")
            return True
        # Katie Dowlin: If the class you want to add the attribute to doesn't exist.
        else:
            print(f"Add failed- class '{class_name}' doesn't exist.")
            return False

    def delete_attribute(self, name, class_name):
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram.classes.keys():
            # Katie Dowlin: Check if an attribute with that name exists in that class.
            if name in self.diagram.classes[class_name]:
                self.diagram.classes[class_name].remove(name)
                print(f"Attribute '{name}' deleted successfully.")
                return True
            # Katie Dowlin: If there is no attribute with that name in that class.
            else:
                print(f"Delete failed- attribute '{name}' doesn't exist.")
                return False
        # Katie Dowlin: If the class doesn't exist.
        else:
            print(f"Delete failed- class '{class_name}' doesn't exist.")
            return False

    def rename_attribute(self, old_name, new_name, class_name):
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram.classes.keys():
            # Katie Dowlin: Check if old name is an attribute in that class.
            if old_name in self.diagram.classes[class_name]:
                self.diagram.classes[class_name].remove(old_name)
                self.diagram.classes[class_name].append(new_name)
                print(f"Attribute '{old_name}' has been renamed to '{new_name}.'")
                return True
            # Katie Dowlin: If the old name does not exist.
            else:
                print(f"Rename failed- attribute '{old_name}' doesn't exist.")
                return False
        # Katie Dowlin: If the class doesn't exist.
        else:
            print(f"Rename failed- class '{class_name}' doesn't exist.")
            return False
