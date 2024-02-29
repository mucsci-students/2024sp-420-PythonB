from Models.diagram import Diagram
from Models.classadd import UMLClass


class Fields:
    """
        Initializes a Field instance.

        Parameters:
            diagram_class: A UMLClass instance.

        Precondition:
            'diagram_class' should be a class that exists in the UML Diagram.

        Postcondition:
            Initializes a field in the given class.

        Returns:
            None
    """
    def __init__(self, diagram_class):
        self.diagram_class = diagram_class


    """
        Adds a new field to a class.

        Parameters:
            class_name: The name of the class to add the field to.
            field_name: The name of the field to add.

        Precondition:
            class_name should be the name of a class that exists in the UML Diagram.
            field_name should be a valid name for a field in Python.

        Postcondition:
            If successful: Adds a new field with the given name to the given class.

        Returns:
            None
    """
    def add_field(self, class_name, field_name):
        # Katie Dowlin: Check if the class you want to add the field to exists.
        if class_name in self.diagram_class.diagram.classes.keys():
            # Katie Dowlin: Check if the field name is already used.
            if field_name not in self.diagram_class.classes[class_name]["Fields"]:
                self.diagram_class.diagram.classes[class_name]["Fields"].append(field_name)
                print(f"Field '{field_name}' added successfully.")
            else:
                raise ValueError(f"Add failed- field '{field_name}' already exists.")
        # Katie Dowlin: If the class you want to add the attribute to doesn't exist.
        else:
            raise ValueError(f"Add failed- class '{class_name}' doesn't exist.")

    """
        Deletes a field from a class.

        Parameters:
            class_name: The name of the class to delete the field from.
            field_name: The name of the field to delete.

        Precondition:
            class_name should be the name of a class that exists in the UML Diagram.
            field_name should be the name of a field that exists in the class class_name.

        Postcondition:
            If successful: Deletes the field field_name from the class class_name.

        Returns:
            None
    """
    def delete_field(self, class_name, field_name):
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram_class.diagram.classes.keys():
            # Katie Dowlin: Check if a field with that name exists in that class.
            if field_name in self.diagram_class.diagram.classes[class_name]["Fields"]:
                self.diagram_class.diagram.classes[class_name]["Fields"].remove(field_name)
                print(f"Field '{field_name}' deleted successfully.")
            # Katie Dowlin: If there is no attribute with that name in that class.
            else:
                raise ValueError(f"Delete failed- field '{field_name}' doesn't exist.")
        # Katie Dowlin: If the class doesn't exist.
        else:
            raise ValueError(f"Delete failed- class '{class_name}' doesn't exist.")

    def rename_field(self, class_name, old_name, new_name):
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram_class.diagram.classes.keys():
            # Katie Dowlin: Check if old name is an attribute in that class.
            if old_name in self.diagram_class.diagram.classes[class_name]["Fields"]:
                self.diagram_class.diagram.classes[class_name]["Fields"].remove(old_name)
                self.diagram_class.diagram.classes[class_name]["Fields"].append(new_name)
                print(f"Field '{old_name}' has been renamed to '{new_name}'.")
            # Katie Dowlin: If the old name does not exist.
            else:
                raise ValueError(f"Rename failed- field '{old_name}' doesn't exist.")
        # Katie Dowlin: If the class doesn't exist.
        else:
            raise ValueError(f"Rename failed- class '{class_name}' doesn't exist.")

dia = Diagram()
some_class = UMLClass(dia)
some_class.add_class("Students")
fields = Fields(some_class)
fields.add_field("Students", "Field")
fields.rename_field("Students", "Field", "Field2")
some_class.list_class()


class Methods:
    def __init__(self, diagram_class):
        self.diagram_class = diagram_class


class Parameters:
    def __init__(self, method):
        self.method = method
