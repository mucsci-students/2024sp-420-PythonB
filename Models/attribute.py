from Models.diagram import Diagram
from Models.classadd import UMLClass
from Models.errorHandler import ErrorHandler


class Fields:
    def __init__(self, diagram_class):
        self.diagram_class = diagram_class


class Methods:
    def __init__(self, diagram_class):
        """
        Initializes the Methods instance with a reference to the diagram's class structure.

        Parameters:
            diagram_class (DiagramClass): An instance containing the UML diagram's class structure.

        Precondition:
            `diagram_class` should be an initialized instance of DiagramClass or a similar structure that contains
             a 'classes' attribute.

        Postcondition:
            Initializes `diagram_class` with the given DiagramClass instance.

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
            `class_name` must exist within `diagram_class.classes`.
            `method_name` must not already exist within the methods of `class_name`.

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
            `class_name` must exist within `diagram_class.classes`.
            `method_name` must exist within the methods of `class_name`.

        Postcondition:
            Removes the specified method from the class.

        Returns:
            None
        """

        if class_name not in self.diagram_class.classes:
            raise ValueError(f"Class '{class_name}' does not exist.")

        methods = self.diagram_class.classes[class_name]['Methods']
        for method in methods:
            if method_name in method:
                methods.remove(method)
                print(f"Method '{method_name}' removed from class '{class_name}' successfully.")
                break

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
            `class_name` must exist within `diagram_class.classes`.
            `old_name` must exist within the methods of `class_name`.
            `new_name` must not already exist within the methods of `class_name`.

        Postcondition:
            Renames the specified method to `new_name`.

        Returns:
            None
        """

        if class_name not in self.diagram_class.classes:
            raise ValueError(f"Class '{class_name}' does not exist.")

        methods = self.diagram_class.classes[class_name]['Methods']
        for method in methods:
            if old_name in method:
                method[new_name] = method.pop(old_name)
                print(f"Method '{old_name}' in class '{class_name}' renamed to '{new_name}' successfully.")
                break

        raise ValueError(f"Method '{old_name}' not found in class '{class_name}'.")


class Parameters:
    def __init__(self, method):
        self.method = method


# Zhang testing:
dia = Diagram()
some_class = UMLClass(dia)
some_class.add_class('Csci')

method1 = Methods(some_class)
method1.add_method('Csci', 'Software Development')
#method1.add_method('Csci', 'Software Development')
# method1.delete_method('Csci', 'Software Development')

print(some_class.list_class())

