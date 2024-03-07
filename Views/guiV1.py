import tkinter as tk
from tkinter import *
from tkinter import messagebox


class UMLDiagramEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LambdaLegion UML Program (GUI Edition) V1.0")
        self.geometry("800x600")

        self.create_menu()
        self.create_sidebar()
        self.create_canvas()

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
        classes_menu.add_command(label="List Attributes", command=self.list_attributes)
        classes_menu.add_command(label="List Classes", command=self.list_classes)
        menu_bar.add_cascade(label="Classes", menu=classes_menu)

        # Relationships
        relationships_menu = Menu(menu_bar, tearoff=0)
        relationships_menu.add_command(label="Add", command=self.add_relationship)
        relationships_menu.add_command(label="Delete", command=self.delete_relationship)
        relationships_menu.add_command(label="List", command=self.list_relationship)
        menu_bar.add_cascade(label="Relationships", menu=relationships_menu)

        # Attributes
        attributes_menu = Menu(menu_bar, tearoff=0)
        attributes_menu.add_command(label="New Field", command=self.add_field)
        attributes_menu.add_command(label="Delete Field", command=self.delete_field)
        attributes_menu.add_command(label="Rename Field", command=self.rename_field)
        attributes_menu.add_separator()
        attributes_menu.add_command(label="New Parameter", command=self.new_param)
        attributes_menu.add_command(label="Delete Parameter", command=self.delete_param)
        attributes_menu.add_command(label="Rename Parameter", command=self.rename_param)
        attributes_menu.add_separator()
        attributes_menu.add_command(label="New Method", command=self.new_method)
        attributes_menu.add_command(label="Delete Method", command=self.delete_method)
        attributes_menu.add_command(label="Rename Method", command=self.rename_method)
        menu_bar.add_cascade(label="Attributes", menu=attributes_menu)

        # Help
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Classes", command=self.helpClasses)
        help_menu.add_command(label="Relationships", command=self.helpRelationships)
        help_menu.add_command(label="Attributes", command=self.helpAttributes)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def create_canvas(self):
        self.canvas = tk.Canvas(self, width=600, height=400)
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def create_sidebar(self):
        self.sidebar = tk.Frame(self, width=200, bg='gray')
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



        # Add more buttons for other categories as needed

    def class_options_menu(self):
        # Create a menu that will appear at the current mouse position
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Add Class", command=self.add_class)
        menu.add_command(label="Delete Class", command=self.delete_class)
        menu.add_command(label="Rename Class", command=self.rename_class)
        menu.add_separator()
        menu.add_command(label="List Classes", command=self.list_classes)

        try:
            # Display the menu at the current mouse position
            menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            menu.grab_release()

    def attributes_options_menu(self):
        menu = Menu(self, tearoff=0)
        menu.add_command(label="New Field", command=self.add_field)
        menu.add_command(label="Delete Field", command=self.delete_field)
        menu.add_command(label="Rename Field", command=self.rename_field)
        menu.add_separator()
        menu.add_command(label="New Parameter", command=self.new_param)
        menu.add_command(label="Delete Parameter", command=self.delete_param)
        menu.add_command(label="Rename Parameter", command=self.rename_param)
        menu.add_separator()
        menu.add_command(label="New Method", command=self.new_method)
        menu.add_command(label="Delete Method", command=self.delete_method)
        menu.add_command(label="Rename Method", command=self.rename_method)

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
        menu.add_command(label="List", command=self.list_relationship)

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
        help_menu.add_command(label="Classes", command=self.helpClasses)
        help_menu.add_command(label="Relationships", command=self.helpRelationships)
        help_menu.add_command(label="Attributes", command=self.helpAttributes)

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
        help_window = tk.Toplevel(self)
        help_window.title("Help - Class Commands")
        help_window.geometry("400x300")

        text = tk.Text(help_window, wrap="word")
        text.insert("end", "help class                                                     Displays this menu\n"
                           "add class <class_name>                                         Adds a class named <class_name>\n"
                           "delete class <class_name>                                      Deletes class named <class_name> and all of its attributes/relationships\n"
                           "rename class <current_name> <new_name>                         Renames class <current_name> to <new_name>\n"
                           "list class <class_name>                                        Lists all attributes/relationships pertaining to <class_name>\n"
                           "list classes                                                   Lists all classes in current UML\n")
        text.config(state="disabled")  # Make it read-only
        text.pack(expand=True, fill="both")

        # Add a scrollbar
        scrollbar = tk.Scrollbar(help_window, command=text.yview)
        scrollbar.pack(side="right", fill="y")
        text.config(yscrollcommand=scrollbar.set)


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


if __name__ == "__main__":
    app = UMLDiagramEditor()
    app.mainloop()