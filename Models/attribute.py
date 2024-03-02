from diagram import Diagram
from classadd import UMLClass


class Fields:
    def __init__(self, diagram_class):
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
        self.diagram_class = diagram_class

    def add_field(self, class_name, field_name):
        """
                Adds a new field to a class.

                Parameters:
                    class_name: The name of the class to add the field to.
                    field_name: The name of the field to add.

                Precondition:
                    class_name should be the name of a class that exists in the UML Diagram.
                    field_name should be a valid name for a field in Python.
                    There should be no field already called field_name in the class class_name.

                Postcondition:
                    If successful: Adds a new field with the given name to the given class.

                Returns:
                    None
        """
        # Katie Dowlin: Check if the class you want to add the field to exists.
        if class_name in self.diagram_class.classes.keys():
            # Katie Dowlin: Check if the field name is already used.
            if field_name not in self.diagram_class.classes[class_name]["Fields"]:
                self.diagram_class.classes[class_name]["Fields"].append(field_name)
                print(f"Field '{field_name}' added successfully.")
            else:
                raise ValueError(f"Add failed- field '{field_name}' already exists.")
        # Katie Dowlin: If the class you want to add the field to doesn't exist.
        else:
            raise ValueError(f"Add failed- class '{class_name}' doesn't exist.")

    def delete_field(self, class_name, field_name):
        """
                Deletes a field from a class.

                Parameters:
                    class_name: The name of the class to delete the field from.
                    field_name: The name of the field to delete.

                Precondition:
                    class_name should be the name of a class that exists in the UML Diagram.
                    field_name should be the name of a field that exists in the class class_name.

                Postcondition:
                    If successful: Renames the field old_name in the class class_name to new_name.

                Returns:
                    None
        """
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram_class.classes.keys():
            # Katie Dowlin: Check if a field with that name exists in that class.
            if field_name in self.diagram_class.classes[class_name]["Fields"]:
                self.diagram_class.classes[class_name]["Fields"].remove(field_name)
                print(f"Field '{field_name}' deleted successfully.")
            # Katie Dowlin: If there is no field with that name in that class.
            else:
                raise ValueError(f"Delete failed- field '{field_name}' doesn't exist.")
        # Katie Dowlin: If the class doesn't exist.
        else:
            raise ValueError(f"Delete failed- class '{class_name}' doesn't exist.")

    def rename_field(self, class_name, old_name, new_name):
        """
                Renames a field in a class.

                Parameters:
                    class_name: The name of the class to delete the field from.
                    old_name: The name of the field to rename.
                    new_name: The name the field should be renamed to.

                   Precondition:
                       class_name should be the name of a class that exists in the UML Diagram.
                       old_name should be the name of a field that exists in the class class_name.
                       new_name should be a valid name for a field in Python.
                       There should be no field already called new_name in the class class_name.

                   Postcondition:
                       If successful: Deletes the field field_name from the class class_name.

                   Returns:
                       None
        """
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram_class.classes.keys():
            # Katie Dowlin: Check if old name is a field in that class.
            if old_name in self.diagram_class.classes[class_name]["Fields"]:
                # Katie Dowlin: Check if new name is a field in that class.
                if new_name in self.diagram_class.classes[class_name]["Fields"]:
                    raise ValueError(f"Rename failed- field '{new_name}' already exists.")
                else:
                    self.diagram_class.classes[class_name]["Fields"].remove(old_name)
                    self.diagram_class.classes[class_name]["Fields"].append(new_name)
                    print(f"Field '{old_name}' has been renamed to '{new_name}'.")
            # Katie Dowlin: If the old name does not exist.
            else:
                raise ValueError(f"Rename failed- field '{old_name}' doesn't exist.")
        # Katie Dowlin: If the class doesn't exist.
        else:
            raise ValueError(f"Rename failed- class '{class_name}' doesn't exist.")


class Methods:
    def __init__(self, diagram_class):
        """
            Initializes the Methods instance with a reference to the diagram's class structure.

            Parameters:
                diagram_class (Diagram): An instance containing the UML diagram's class structure.

            Precondition:
                'diagram_class' should be an initialized instance of DiagramClass or a similar structure that contains
                 a 'classes' attribute.

            Postcondition:
                Initializes 'diagram_class' with the given DiagramClass instance.

            Returns:
                None
        """
        self.diagram_class = diagram_class
        self.parameters = Parameters(self)

    def add_method(self, class_name, method_name):
        """
            Adds a new method to a specified class if the method does not already exist.

            Parameters:
                class_name (str): The name of the class to which the method will be added.
                method_name (str): The name of the method to be added.

            Precondition:
                'class_name' must exist within 'diagram_class.classes'.
                'method_name' must not already exist within the methods of 'class_name'.

            Postcondition:
                Adds a new method to the specified class with no parameters.

            Returns:
                None
        """

        if class_name not in self.diagram_class.classes.keys():
            raise ValueError(f"Class '{class_name}' does not exist.")

        methods = self.diagram_class.classes[class_name]['Methods']
        for method in methods:
            if method_name in method:
                raise ValueError(f"Method '{method_name}' already exists in class '{class_name}'.")

        methods.append({method_name: {'Parameters': []}})
        print(f"Method '{method_name}' added to class '{class_name}' successfully.")

    def delete_method(self, class_name, method_name):
        """
            Deletes an existing method from a specified class.

            Parameters:
                class_name (str): The name of the class from which the method will be removed.
                method_name (str): The name of the method to be removed.

            Precondition:
                'class_name' must exist within 'diagram_class.classes'.
                'method_name' must exist within the methods of 'class_name'.

            Postcondition:
                Removes the specified method from the class.

            Returns:
                None
        """

        if class_name not in self.diagram_class.classes.keys():
            raise ValueError(f"Class '{class_name}' does not exist.")

        remove = False
        methods = self.diagram_class.classes[class_name]['Methods']
        for method in methods:
            if method_name in method:
                methods.remove(method)
                print(f"Method '{method_name}' removed from class '{class_name}' successfully.")
                remove = True
                break
        if not remove:
            raise ValueError(f"Method '{method_name}' not found in class '{class_name}'.")

    def rename_method(self, class_name, old_name, new_name):
        """
            Renames an existing method in a specified class.

            Parameters:
                class_name (str): The name of the class containing the method to be renamed.
                old_name (str): The current name of the method to be renamed.
                new_name (str): The new name for the method.

            Precondition:
                'class_name' must exist within 'diagram_class.classes'.
                'old_name' must exist within the methods of 'class_name'.
                'new_name' must not already exist within the methods of 'class_name'.

            Postcondition:
                Renames the specified method to 'new_name'.

            Returns:
                None
        """

        if class_name not in self.diagram_class.classes.keys():
            raise ValueError(f"Class '{class_name}' does not exist.")

        renamed = False
        methods = self.diagram_class.classes[class_name]['Methods']
        for method in methods:
            if old_name in method:
                method[new_name] = method.pop(old_name)
                print(f"Method '{old_name}' in class '{class_name}' renamed to '{new_name}' successfully.")
                renamed = True
                break
        if not renamed:
            raise ValueError(f"Method '{old_name}' not found in class '{class_name}'.")



class Parameters:
        def __init__(self, method_class):
            """
                   Initializes the Methods instance .

                   Parameters:
                       'method_class' (Method): An instance containing the Method's class structure.

                   Precondition:
                       'method_class' should be an initialized instance of Method class.

                   Postcondition:
                       Initializes 'method_class' with the given Method class instance.

                   Returns:
                       None
                   """
            self.method_class = method_class


        def add_parameters(self, class_name, m_name, p_name):
            """
                    Add a new Parameter to a specified method if the parameter does not already exist.

                    Parameters:
                        class_name (str): The name of the class to which the method will check that exist or not.
                        m_name (str): The name of the method to be added.

                    Precondition:
                        'class_name' must exist within 'diagram_class.classes'.
                        'method_name' must not already exist within the methods of 'class_name'.

                    Postcondition:
                        Adds a new Parameter to the specified Method.

                    Returns:
                        None
                    """
            if class_name not in self.method_class.diagram_class.classes:
                raise ValueError(f"Class '{class_name}' does not exist")
            for method_dict in self.method_class.diagram_class.classes[class_name]['Methods']:
                if m_name in method_dict:
                    if p_name not in method_dict[m_name]['Parameters']:
                        method_dict[m_name]['Parameters'].append(p_name)
                        print(f"Parameter '{p_name}' added to method '{m_name}' in class '{class_name}'.")
                    else:
                        raise ValueError(f"Parameter '{p_name}' already exists in method '{m_name}'.")
                else:
                    raise ValueError(f"Method '{m_name}' not found in class '{class_name}'.")


        def delete_parameters(self, class_name, m_name, p_name):
            """
                   Deletes an existing Parameter from a specified method.

                   Parameters:
                       class_name (str): The name of the class.
                       m_name (str): The name of the method containing the Parameter to be removed.

                   Precondition:
                       'class_name' must exist within 'diagram_class.classes'.
                       'm_name' must exist within the methods of 'class_name'.
                       p_name (str): must exist within method.

                   Postcondition:
                       Removes the specified Parameter from the method.

                   Returns:
                       None
                   """
            if class_name not in self.method_class.diagram_class.classes:
                raise ValueError(f"Class '{class_name}' does not exist")
            for method_dict in self.method_class.diagram_class.classes[class_name]['Methods']:
                if m_name in method_dict:
                    if p_name in method_dict[m_name]['Parameters']:
                        method_dict[m_name]['Parameters'].remove(p_name)
                        print(f"parameters '{p_name}' removed successfully.")

                    else:
                        raise ValueError(f"parameters '{p_name}'does not exist")

                else:
                    raise ValueError(f"Method '{m_name}' does not exist")



        def delete_all_parameters(self, class_name, m_name):
            """
                   Deletes an existing Parameter from a specified method.

                   Parameters:
                       class_name (str): The name of the class.
                       m_name (str): The name of the method containing the Parameter to be removed.

                   Precondition:
                       'class_name' must exist within 'diagram_class.classes'.
                       'm_name' must exist within the methods of 'class_name'.
                       p_name (str): must exist within method.

                   Postcondition:
                       Removes all the Parameters from the method.

                   Returns:
                       None
                   """
            if class_name not in self.method_class.diagram_class.classes:
                raise ValueError(f"Class '{class_name}' does not exist")
            for method_dict in self.method_class.diagram_class.classes[class_name]['Methods']:
                if m_name in method_dict:
                    method_dict[m_name]['Parameters'].clear()
                    print(f"All parameters removed successfully.")


                else:
                    raise ValueError(f"Method '{m_name}' does not exist")


        def change_parameters(self, class_name, m_name, old_p_name, new_p_name):
            """
                    Renames an existing Parameter in a specified method.

                    Parameters:
                        class_name (str): The name of the class containing the method.
                        m_name (str): The name of the method containing the Parameter to be renamed.
                        old_p_name (str): The current name of the Parameter to be renamed.
                        new_p_name (str): The new name for the Parameter.

                    Precondition:
                        'class_name' must exist within 'diagram_class.classes'.
                        'old_p_name' must exist within the Parameters of 'm_class'.
                        'new_p_name' must not already exist within the Parameters of 'm_name'.

                    Postcondition:
                        Renames the specified Parameter to 'new_p_name'.

                    Returns:
                        None
                    """
            if class_name not in self.method_class.diagram_class.classes:
                raise ValueError(f"Class '{class_name}' does not exist")
            for method_dict in self.method_class.diagram_class.classes[class_name]['Methods']:
                if m_name in method_dict:
                    if old_p_name in method_dict[m_name]['Parameters'] and new_p_name not in method_dict[m_name]['Parameters']:
                        method_dict[m_name]['Parameters'].remove(old_p_name)
                        method_dict[m_name]['Parameters'].append(new_p_name)
                        print(f"Parameters '{old_p_name}' has been changed to '{new_p_name}.'")
                    else:
                        raise ValueError(f"Changed failed- parameter")
                else:
                    raise ValueError(f"Changed failed- method '{m_name}' doesn't exist.")
