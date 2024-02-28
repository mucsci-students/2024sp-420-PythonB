from diagram import Diagram
from classadd import UMLClass
from errorHandler import ErrorHandler


class Fields:
    def __init__(self, diagram_class):
        self.diagram_class = diagram_class


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

    @ErrorHandler.handle_error
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

    @ErrorHandler.handle_error
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

    @ErrorHandler.handle_error
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
        self.method_class = method_class

    @ErrorHandler.handle_error
    def add_parameters(self, class_name, m_name, p_name):
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

    @ErrorHandler.handle_error
    def delete_parameters(self, class_name, m_name, p_name):
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

    @ErrorHandler.handle_error
    def rename_parameters(self, class_name, m_name, old_p_name, new_p_name):
        if class_name not in self.method_class.diagram_class.classes:
            raise ValueError(f"Class '{class_name}' does not exist")
        for method_dict in self.method_class.diagram_class.classes[class_name]['Methods']:
            if m_name in method_dict:
                if old_p_name in method_dict[m_name]['Parameters'] and new_p_name not in method_dict[m_name]['Parameters']:
                    method_dict[m_name]['Parameters'].remove(old_p_name)
                    method_dict[m_name]['Parameters'].append(new_p_name)
                    print(f"Parameters '{old_p_name}' has been renamed to '{new_p_name}.'")
                else:
                    raise ValueError(f"Rename failed- parameter")
            else:
                raise ValueError(f"Rename failed- method '{m_name}' doesn't exist.")


"""
# Zhang testing:
dia = Diagram()
some_class = UMLClass(dia)
some_class.add_class('Csci')

method1 = Methods(some_class)
method1.add_method('Csci', 'Software Development')
# method1.rename_method('Csci', 'Software Development', '420')
# method1.delete_method('Csci', '420')
Parameter1 = Parameters(method1)
Parameter1.add_parameters('Software Development', 'Exams')

print(some_class.list_class())
# help(Methods)
"""
dia = Diagram()
some_class = UMLClass(dia)
some_class.add_class('Csci')

method1 = Methods(some_class)
method1.add_method('Csci', 'Software')

print(some_class.list_class())
# Adding parameters to the method
method1.parameters.add_parameters('Csci', 'Software', 'SQL')
method1.parameters.add_parameters('Csci', 'Software', 'DL')
method1.parameters.add_parameters('Csci', 'Software', 'DL')
print(some_class.list_class())
method1.parameters.delete_parameters('Csci', 'Software', 'YYL')
# method1.parameters.delete_parameters('Csci', 'Software', 'SQL')
print(some_class.list_class())

method1.parameters.rename_parameters('Csci', 'Software', 'SQL', 'DL')

print(some_class.list_class())
