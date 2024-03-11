import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import json
from Models.diagram import Diagram
from Models.classadd import UMLClass
import Models.attribute
from Models.saveload import SaveLoad


# NOT INTEGRATED
class GUIController:
    def __init__(self):
        self.diagram = Diagram()
        self.classes = UMLClass(self.diagram)
        self.relationship = self.classes.relationships
        self.fields = Models.attribute.Fields(self.classes)
        self.methods = Models.attribute.Methods(self.classes)
        self.parameters = Models.attribute.Parameters(self.methods)
        self.save_load = SaveLoad()


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

    def open_file(self, name):
        
        save_folder = 'save_folder'
        
        file_path = os.path.join(save_folder, name + ".json")

        if not os.path.exists(file_path):
            raise ValueError(f"File, '{file_path}' does not exist.")
            # Protects against loading a file that does not exist. (2/15/24)

        else:
            save_item = self.save_load.load(name)
            for class_item in save_item["classes"]:
                class_name = class_item["name"]
                self.add_class(class_name)
                for field in class_item["fields"]:
                    self.add_attribute(class_name, field["name"], "field")
                for method in class_item["methods"]:
                    self.add_attribute(class_name, method["name"], "method")
                    for param in method["params"]:
                        self.add_param(class_name, method["name"], param["name"])
        for relation in save_item["relationships"]:
            src = relation["source"]
            dest = relation["destination"]
            type = relation["type"]
            self.add_relationship(src, dest, type)
            
        messagebox.showinfo("Action", "Open an existing file")

        return save_item

    def save_file(self):
        """
        Saves a file.

        Parameters:
            filename -- The desired filename, or the name of the file to overwrite

        Returns:
            theFile -- The saved file
        """
        messagebox.showinfo("Action", "Save the current file")

    def add_class(self, name):
        
        """
        Adds a class

        Parameters:
            self -- The parent
            className -- The name of the class to be created

        Returns:
            successBool -- True if the add class was successful, False otherwise
        """
        if self.diagram.name_checker(name):
            if name[0].isupper():
                self.classes.add_class(name)

    def delete_class(self, name):
        """
              Deletes a class

              Parameters:
                  self -- The parent
                  className -- The name of the class to be created

              Returns:
                  successBool -- True if the Delete class was successful, False otherwise
              """
        self.classes.delete_class(name)

    def rename_class(self, old_name, new_name):
        """
              Renames a class

              Parameters:
                  self -- The parent
                  className -- The name of the class to be renamed
                  newClassName -- the new name of the class

              Returns:
                  successBool -- True if the rename class was successful, False otherwise
              """
        if self.diagram.name_checker(new_name):
            if new_name[0].isupper():
                 self.classes.rename_class(old_name, new_name)      

    def add_relationship(self, src, dst, rel_type):
        """
        Adds a relationship between two classes

        Parameters:
            self -- The parent

        Returns:
            None
        """
        self.relationship.add_relationship(src, dst, rel_type) 

    def delete_relationship(self, src, dst):
        """
        Deletes a relationship between two classes
        Parameters:
            self -- The parent

        Returns:
             None
        """
        self.relationship.delete_relationship(src,dst)

    def add_attribute(self, class_name, attribute_name, att_type):
        """
        Adds a field to a class
        Parameters:
            self -- The parent

        Returns:
            successBool -- True if the add field was successful, False otherwise
        """
        if self.diagram.name_checker(attribute_name):
            if att_type == "field":
                self.fields.add_field(class_name, attribute_name)
            else:
                self.methods.add_method(class_name, attribute_name)

    def delete_attribute(self, class_name, attribute_name, att_type):
        """
        Deletes a field from a class

        Parameters:
            self -- the parent

        Returns:
             None
        """
        if att_type == "field":
            self.fields.delete_field(class_name, attribute_name)
        else:
            self.methods.delete_method(class_name, attribute_name)
    
    def rename_attribute(self, class_name, attribute_name, new_name, att_type):
        """
        Renames a field in a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        if self.diagram.name_checker(attribute_name):
            if att_type == "field":
                self.fields.rename_field(class_name, attribute_name, new_name)
            else:
                self.methods.rename_method(class_name, attribute_name, new_name)
            
    def add_param(self, class_name, method_name, param_name):
        """
        Adds a new parameter to a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        if self.diagram.name_checker(param_name):
            self.parameters.add_parameter(class_name, method_name, param_name)

    def delete_param(self, class_name, method_name, param_name):
        """
        Deletes a parameter from a class

        Parameters:
            self -- The parent

        Returns:
            None
            """
        self.parameters.delete_parameter(class_name, method_name, param_name)

    def rename_param(self, class_name, method_name, param_name, new_name):
        """
        Renames a parameter in a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        if self.diagram.name_checker(new_name):
            self.parameters.rename_parameter(class_name, method_name, param_name, new_name)


