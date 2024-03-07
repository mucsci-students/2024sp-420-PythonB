import tkinter as tk
from tkinter import *
from tkinter import messagebox

# NOT INTEGRATED
class GUIController:
    def __init__(self, view):
        self.view = view  # Reference to the view

    """
    pydoc comment goes here
    """

    def new_file(self):
        """
        Creates a new file.

        Parameters:
            self -- The parent

        Returns:
            newFile -- The new file
        """
        # Placeholder for new file action
        messagebox.showinfo("Action", "Create a new file")

    def open_file(self):
        """
        Loads a file.

        Parameters:
            filename -- The name of the file to load

        Returns:
            theFile -- The opened file

        """
        messagebox.showinfo("Action", "Open an existing file")

    def save_file(self):
        """
        Saves a file.

        Parameters:
            filename -- The desired filename, or the name of the file to overwrite

        Returns:
            theFile -- The saved file
        """
        messagebox.showinfo("Action", "Save the current file")

    def undo_action(self):
        """
        Undoes the previous action.
        Parameters:
            None

        Returns:
            successBool -- True if the undo was successful, False otherwise
        """
        messagebox.showinfo("Action", "Undo the last action")

    def add_class(self):
        """
        Adds a class

        Parameters:
            self -- The parent
            className -- The name of the class to be created

        Returns:
            successBool -- True if the add class was successful, False otherwise
        """
        messagebox.showinfo("Action", "Add a new class")

    def delete_class(self):
        """
              Deletes a class

              Parameters:
                  self -- The parent
                  className -- The name of the class to be created

              Returns:
                  successBool -- True if the Delete class was successful, False otherwise
              """
        messagebox.showinfo("Action", "Delete Class")

    def rename_class(self):
        """
              Renames a class

              Parameters:
                  self -- The parent
                  className -- The name of the class to be renamed
                  newClassName -- the new name of the class

              Returns:
                  successBool -- True if the rename class was successful, False otherwise
              """
        messagebox.showinfo("Action", "Rename Class")

    def list_classes(self):
        """
        Lists all classes

        Parameters:
            self -- The parent

        Returns:
            none
        """
        messagebox.showinfo("Action", "List Classes")

    def list_attributes(self):
        """
        List all attributes of a given class

        Parameters:
            self -- the parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "List Attributes")

    def add_relationship(self):
        """
        Adds a relationship between two classes

        Parameters:
            self -- The parent

        Returns:
            None
        """
        # Placeholder for adding a relationship
        messagebox.showinfo("Action", "Add a new relationship")

    def delete_relationship(self):
        """
        Deletes a relationship between two classes
        Parameters:
            self -- The parent

        Returns:
             None
        """
        messagebox.showinfo("Action", "Delete Relationship")

    def list_relationship(self):
        """
        Lists all relationships of a class
        Parameters:
            self -- the parent

        Returns:
            none
        """
        messagebox.showinfo("Action", "List Relationships")

    def add_field(self):
        """
        Adds a field to a class
        Parameters:
            self -- The parent

        Returns:
            successBool -- True if the add field was successful, False otherwise
        """
        messagebox.showinfo("Action", "Add Field")

    def delete_field(self):
        """
        Deletes a field from a class

        Parameters:
            self -- the parent

        Returns:
             None
        """
        messagebox.showinfo("Action", "Delete Field")

    def rename_field(self):
        """
        Renames a field in a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Rename Field")

    def new_param(self):
        """
        Adds a new parameter to a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", " Add Parameter")

    def delete_param(self):
        """
        Deletes a parameter from a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Delete Parameter")

    def rename_param(self):
        """
        Renames a parameter in a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Rename Param")

    def new_method(self):
        """
        Adds a method to a class.

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "New Method")

    def delete_method(self):
        """
        Deletes a method from a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Delete Method")

    def rename_method(self):
        """
        Renames a parameter from a class.

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Rename Param")

    def helpClasses(self):
        """
        Displays the classes help page

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Help Classes")

    def helpRelationships(self):
        """
        Displays the relationships help page

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Help Relationships")

    def helpAttributes(self):
        """
        Displays the attributes help page

        Parameters:
            self -- The parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "Help Attributes")
