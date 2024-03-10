import json
import tkinter as tk
import webbrowser
from Models.classadd import UMLClass as Classes
from Models.attribute import Fields as Fields
from Models.attribute import Methods as Methods
from Models.attribute import Parameters as Parameters
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

from Models.diagram import Diagram


class UMLDiagramEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LambdaLegion UML Program (GUI Edition) V1.0")
        self.geometry("800x600")
        self.create_menu()
        self.create_sidebar()
        self.create_diagram_space()
        self.class_boxes = []

        

    def create_menu(self):
        """
        Creates the main menu bar for the application window.

        This method initializes and configures the menu bar with several cascading menus including File, Edit, Classes,
        Relationships, Attributes, and Help.
        Parameters:
            self - The parent

        Returns:
            None
        """
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        # File
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Classes
        classes_menu = Menu(menu_bar, tearoff=0)
        classes_menu.add_command(label="New", command=self.add_class)
        classes_menu.add_command(label="Delete", command=self.delete_class)
        classes_menu.add_command(label="Rename", command=self.rename_class)
        menu_bar.add_cascade(label="Classes", menu=classes_menu)

        # Relationships
        relationships_menu = Menu(menu_bar, tearoff=0)
        relationships_menu.add_command(label="Add", command=self.add_relationship)
        relationships_menu.add_command(label="Delete", command=self.delete_relationship)
        relationships_menu.add_command(label="List", command=self.list_relationship)
        menu_bar.add_cascade(label="Relationships", menu=relationships_menu)

        # Attributes
        attributes_menu = Menu(menu_bar, tearoff=0)
        attributes_menu.add_command(label="New Field", command=self.add_attribute_to_class)
        attributes_menu.add_command(label="Delete Field", command=self.add_attribute)
        attributes_menu.add_command(label="Rename Field", command=self.add_attribute)
        attributes_menu.add_separator()
        attributes_menu.add_command(label="New Parameter", command=self.new_param)
        attributes_menu.add_command(label="Delete Parameter", command=self.delete_param)
        attributes_menu.add_command(label="Rename Parameter", command=self.rename_param)
        attributes_menu.add_separator()
        attributes_menu.add_command(label="New Method", command=self.add_attribute_to_class)
        attributes_menu.add_command(label="Delete Method", command=self.add_attribute)
        attributes_menu.add_command(label="Rename Method", command=self.add_attribute)
        menu_bar.add_cascade(label="Attributes", menu=attributes_menu)

        # Help
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Read Me", command=self.help)
        
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def create_canvas(self):
        self.canvas = tk.Canvas(self, bg='LightBlue', width=600, height=400)
        self.canvas.pack(expand=True, fill=tk.BOTH)


    def create_sidebar(self):
        self.sidebar = tk.Frame(self, width=200, bg='lightgray')
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.btn_class = tk.Button(self.sidebar, text="File", command=self.file_options_menu)
        self.btn_class.pack(fill=tk.X, pady=(5, 5))

        self.btn_class = tk.Button(self.sidebar, text="Edit", command=self.edit_options_menu)
        self.btn_class.pack(fill=tk.X, pady=(5, 5))

        # Example button with dropdown for "Add Class"
        self.btn_class = tk.Button(self.sidebar, text="Classes", command=self.class_options_menu)
        self.btn_class.pack(fill=tk.X, pady=(5, 5))

        self.btn_relationships = tk.Button(self.sidebar, text="Relationships", command=self.relationship_options_menu)
        self.btn_relationships.pack(fill=tk.X, pady=(5, 5))

        self.btn_methods = tk.Button(self.sidebar, text="Attributes", command=self.attributes_options_menu)
        self.btn_methods.pack(fill=tk.X, pady=(5, 5))

        self.btn_class = tk.Button(self.sidebar, text="Help", command=self.help_options_menu)
        self.btn_class.pack(fill=tk.X, pady=(5, 5))

    def create_diagram_space(self):
        
        self.diagram_canvas = tk.Canvas(self, bg='white')
        
        # Pack the canvas to fill the remaining space after the sidebar
        self.diagram_canvas.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    def class_options_menu(self):
        # Create a menu that will appear at the current mouse position
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Add Class", command=self.add_class)
        menu.add_command(label="Delete Class", command=self.delete_class)
        menu.add_command(label="Rename Class", command=self.rename_class)
        menu.add_separator()

        try:
            # Display the menu at the current mouse position
            menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            menu.grab_release()

    def attributes_options_menu(self):
        menu = Menu(self, tearoff=0)
        menu.add_command(label="New Field", command=self.add_attribute_to_class)
        menu.add_command(label="Delete Field", command=self.delete_attribute)
        menu.add_command(label="Rename Field", command=self.rename_attribute)
        menu.add_separator()
        menu.add_command(label="New Parameter", command=self.new_param)
        menu.add_command(label="Delete Parameter", command=self.delete_param)
        menu.add_command(label="Rename Parameter", command=self.rename_param)
        menu.add_separator()
        menu.add_command(label="New Method", command=self.add_attribute_to_class)
        menu.add_command(label="Delete Method", command=self.delete_attribute)
        menu.add_command(label="Rename Method", command=self.rename_attribute)

        try:
            # Display the menu at the current mouse position
            menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            menu.grab_release()

    def relationship_options_menu(self):
        menu = Menu(self, tearoff=0)
        menu = Menu(self, tearoff=0)
        menu.add_command(label="Add", command=self.add_relationship)
        menu.add_command(label="Delete", command=self.delete_relationship)

        try:
            # Display the menu at the current mouse position
            menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            menu.grab_release()

    def file_options_menu(self):
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        try:
            # Display the menu at the current mouse position
            file_menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            file_menu.grab_release()

    def edit_options_menu(self):
        edit_menu = Menu(self, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo_action)

        try:
            # Display the menu at the current mouse position
            edit_menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            edit_menu.grab_release()

    def help_options_menu(self):
        help_menu = Menu(self, tearoff=0)
        help_menu.add_command(label="Read Me", command=self.help)

        try:
            # Display the menu at the current mouse position
            help_menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            help_menu.grab_release()

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
        class_name = simpledialog.askstring("Input", "Enter a Class Name:", parent=self)
        if not class_name:
            print("No name added!")

        fields = []
        methods = []
        
        next_x, next_y = self.get_next_position()
        
        self.class_boxes.append({'class_name': class_name, 'fields': fields, 'methods': methods, 'x': next_x, 'y': next_y})

        self.create_class_box(self.diagram_canvas, class_name, fields, methods, next_x,next_y)

        # Classes.add_class(class_name)

    def get_next_position(self):
        # For simplicity, let's just arrange them in a horizontal line for now
        spacing = 10  # Spacing between class boxes
        box_width = 150  # Assume a fixed width for now
        x, y = 50, 50  # Starting position for the first class box

        if self.class_boxes:
            # Get the position of the last class box
            last_box = self.class_boxes[-1]
            x, y = last_box['x'], last_box['y']

            # Move to the next position to the right
            x += box_width + spacing

        return x, y

    def create_class_box(self, canvas, class_name, fields, methods, x, y):
        box_width = 150
        text_spacing = 20
        box_height = text_spacing * (2 + len(fields) + len(methods))

        canvas.create_rectangle(x, y, x + box_width, y + box_height, fill='lightgray', outline='black')

        canvas.create_text(x+box_width / 2, y + text_spacing, text=class_name, font = ('TkDefaultFont', 10, 'bold'))

        current_y = y + text_spacing * 2
        for field in fields:
            canvas.create_text(x+10,current_y, text=field, anchor="w")
            current_y += text_spacing

        for method in methods:
            canvas.create_text(x+10, current_y, text=method, anchor="w")
            current_y += text_spacing
        
    def delete_class(self):
        """
        Deletes a class

        Parameters:
            self -- The parent
            className -- The name of the class to be created

        Returns:
            successBool -- True if the Delete class was successful, False otherwise
        """
        class_name = simpledialog.askstring("Delete Class", "Enter a class to delete:", parent=self)
        if class_name is None:
            return

        class_found = False
        for i, class_box in enumerate(self.class_boxes):
            if class_box['class_name'] == class_name:
                del self.class_boxes[i]
                class_found = True
                break  # Correctly placed to break out of the loop when a class is found and deleted

        self.redraw_canvas()  # Call redraw_canvas outside the loop to refresh the canvas once after any deletion

        if not class_found:
            messagebox.showinfo("Delete Class", "Class not found!")
        messagebox.showinfo("Delete Class", f"'{class_name}' has been removed.")

    def redraw_canvas(self):
        self.diagram_canvas.delete("all")  # Clears the canvas

    # Re-draw each class box
        for class_box in self.class_boxes:
            self.create_class_box(self.diagram_canvas, class_box['class_name'], class_box.get('fields', []), class_box.get('methods', []), class_box['x'], class_box['y'])

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
        old_name = simpledialog.askstring("Rename Class", "Enter the name of the class you would like to rename:", parent = self)
        if not old_name:
            messagebox.showinfo("Rename Class","No class name provided.")
            return
        
        new_name = simpledialog.askstring("Rename Class", "Enter a new class name:")
        if not new_name:
            messagebox.showinfo("Rename Class", "No new class name provided.")
            return
        
        for class_box in self.class_boxes:
            if class_box['class_name'] == old_name:
                class_box['class_name'] = new_name
                self.redraw_canvas()
                messagebox.showinfo("Rename Class",f"'{old_name}' has been renamed to '{new_name}'.")
                return
            
        messagebox.showinfo("Rename Class", f"'{old_name}' not found." )



        """
        List all attributes of a given class

        Parameters:
            self -- the parent

        Returns:
            None
        """
        messagebox.showinfo("Action", "List Attributes")

    def add_attribute_to_class(self):
        class_name = simpledialog.askstring("Add Attribute", "Enter the name of the class to add an attribute to:", parent=self)
        if not class_name:
            return

        AddAttributeDialog(self, title="Add Attribute", class_name=class_name)

    def add_attribute(self, class_name, attribute_name, attribute_type):
        if not attribute_name or not class_name or attribute_type not in ['field', 'method']:
            messagebox.showinfo("Error", "Invalid input provided.")
            return

    # Find the class box with the given class_name
        for class_box in self.class_boxes:
            if class_box['class_name'] == class_name:
            # Depending on the attribute_type, append the attribute_name to the appropriate list
                if attribute_type == 'field':
                    class_box.setdefault('fields', []).append(attribute_name)
                else:  # attribute_type == 'method'
                    class_box.setdefault('methods', []).append(attribute_name)

                self.redraw_canvas()  # Refresh the canvas to show the updated class box
                messagebox.showinfo("Success", f"{attribute_type.capitalize()} '{attribute_name}' added to class '{class_name}'.")
                return

    # If the class wasn't found, show an error message
        messagebox.showinfo("Error", f"Class '{class_name}' not found.")

    def delete_relationship(self):

        """
        Deletes a relationship between two classes
        Parameters:
            self -- The parent

        Returns:
             None
        """
        messagebox.showinfo("Action", "Delete Relationship")

    def add_relationship(self):
        """
        Lists all relationships of a class
        Parameters:
            self -- the parent

        Returns:
            none
        """
        messagebox.showinfo("Action", "List Relationships")

    def list_relationship(self):
        """
        Lists all relationships of a class
        Parameters:
            self -- the parent

        Returns:
            none
        """
        messagebox.showinfo("Action", "List Relationships")

    def delete_attribute(self):
    # Ask for the class name from which to delete an attribute
        class_name = simpledialog.askstring("Delete Attribute", "Enter the name of the class:", parent=self)
        if not class_name:
            messagebox.showinfo("Delete Attribute", "Class name not provided.")
            return

        # Ask for the attribute type (field or method)
        attribute_type = simpledialog.askstring("Delete Attribute", "Enter the attribute type (field/method):", parent=self).lower()
        if attribute_type not in ['field', 'method']:
            messagebox.showinfo("Delete Attribute", "Invalid attribute type. Please enter 'field' or 'method'.")
            return

        # Ask for the attribute name to delete
        attribute_name = simpledialog.askstring("Delete Attribute", "Enter the name of the attribute to delete:", parent=self)
        if not attribute_name:
            messagebox.showinfo("Delete Attribute", "Attribute name not provided.")
            return

        # Search for the class and attribute to delete
        for class_box in self.class_boxes:
            if class_box['class_name'] == class_name:
                if attribute_type == 'field' and 'fields' in class_box:
                    if attribute_name in class_box['fields']:
                        class_box['fields'].remove(attribute_name)
                        messagebox.showinfo("Delete Attribute", f"Field '{attribute_name}' deleted from class '{class_name}'.")
                    else:
                        messagebox.showinfo("Delete Attribute", f"Field '{attribute_name}' not found in class '{class_name}'.")
                elif attribute_type == 'method' and 'methods' in class_box:
                    if attribute_name in class_box['methods']:
                        class_box['methods'].remove(attribute_name)
                        messagebox.showinfo("Delete Attribute", f"Method '{attribute_name}' deleted from class '{class_name}'.")
                    else:
                        messagebox.showinfo("Delete Attribute", f"Method '{attribute_name}' not found in class '{class_name}'.")
                self.redraw_canvas()
                return

        messagebox.showinfo("Delete Attribute", f"Class '{class_name}' not found.")

    def rename_attribute(self):
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

    def help(self):
        
        """
        Displays the classes help page

        Parameters:
            self -- The parent

        Returns:
            None
        """
        url = "https://github.com/mucsci-students/2024sp-420-LambdaLegion?tab=readme-ov-file#readme"
        new = 1
        webbrowser.open(url, new = new )

class AddAttributeDialog(simpledialog.Dialog):

    def __init__(self, parent, title=None, class_name=""):
        self.class_name = class_name
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Attribute Name:").grid(row=0)
        self.entry_attribute_name = tk.Entry(master)
        self.entry_attribute_name.grid(row=0, column=1)

        self.attribute_type = tk.StringVar(value="field")
        tk.Radiobutton(master, text="Field", variable=self.attribute_type, value="field").grid(row=1, column=0)
        tk.Radiobutton(master, text="Method", variable=self.attribute_type, value="method").grid(row=1, column=1)

        return self.entry_attribute_name

    def apply(self):
        attribute_name = self.entry_attribute_name.get()
        attribute_type = self.attribute_type.get()
        # Now, we can call the main method to add the attribute with all required information
        self.parent.add_attribute(self.class_name, attribute_name, attribute_type)
   
if __name__ == "__main__":
    app = UMLDiagramEditor()
    app.mainloop()
