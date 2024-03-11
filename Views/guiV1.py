from Models.attribute import Fields, Methods, Parameters
from Models.classadd import UMLClass
from Models.diagram import Diagram
from Models.errorHandler import ErrorHandler
from Models.relationship import UMLRelationship
from Models.saveload import SaveLoad
import json
import tkinter as tk
from tkinter import filedialog
import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

from Models.diagram import Diagram


class UMLDiagramEditor(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("LambdaLegion UML Program (GUI Edition) V1.0")
        self.geometry("800x600")
        self.create_menu()
        self.create_sidebar()
        self.create_diagram_space()
        self.class_boxes = []
        self.relationshipsList = []
        self.update_relationship_tracker()
        
        self.diagram = Diagram()
        self.classes = self.diagram.classes
        self.errorHandler = ErrorHandler()
        self.fields = Fields(self.classes)
        self.methods = Methods(self.classes)
        self.parameters = Parameters(self.methods)
        self.relationships = UMLRelationship(self.classes)
        self.saveload = SaveLoad()
        self.diagram_class = Diagram()
        self.controller = controller

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
        menu_bar.add_cascade(label="Relationships", menu=relationships_menu)

        # Attributes
        attributes_menu = Menu(menu_bar, tearoff=0)
        attributes_menu.add_command(label="Add Attribute", command=self.add_attribute_to_class)
        attributes_menu.add_command(label="Delete Attribute", command=self.add_attribute)
        attributes_menu.add_command(label="Rename Attribute", command=self.add_attribute)
        attributes_menu.add_separator()
        attributes_menu.add_command(label="New Parameter", command=self.new_param)
        attributes_menu.add_command(label="Delete Parameter", command=self.delete_param)
        attributes_menu.add_command(label="Rename Parameter", command=self.rename_param)
        menu_bar.add_cascade(label="Attributes", menu=attributes_menu)

        # Help
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Read Me", command=self.help)
        help_menu.add_command(label="Redraw Diagram", command = self.redraw_canvas)
        
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

        tk.Label(self.sidebar, text="Relationships Tracker", bg='lightgray', font=('TkDefaultFont', 10, 'bold')).pack(pady=(10, 0))

        # Relationship Tracker Listbox
        self.relationship_tracker = tk.Listbox(self.sidebar, height=10)
        self.relationship_tracker.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def update_relationship_tracker(self):
        self.relationship_tracker.delete(0, tk.END)  # Clear existing entries
        for relationship in self.relationshipsList:
            # Assuming your relationship structure is a dictionary with 'source', 'destination', and 'type'
            relationship_str = f"{relationship['source']} - {relationship['type']} - {relationship['destination']}"
            self.relationship_tracker.insert(tk.END, relationship_str)

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
        menu.add_command(label="Add Attribute", command=self.add_attribute_to_class)
        menu.add_command(label="Delete Attribute", command=self.delete_attribute)
        menu.add_command(label="Rename Rename", command=self.rename_attribute)
        menu.add_separator()
        menu.add_command(label="Add Parameter", command=self.new_param)
        menu.add_command(label="Delete Parameter", command=self.delete_param)
        menu.add_command(label="Rename Parameter", command=self.rename_param)

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

        try:
            # Display the menu at the current mouse position
            edit_menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            edit_menu.grab_release()

    def help_options_menu(self):
        help_menu = Menu(self, tearoff=0)
        help_menu.add_command(label="Read Me", command=self.help)
        help_menu.add_command(label="Redraw Diagram", command = self.redraw_canvas)

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
        # Ask the user to select a file

        filename = simpledialog.askstring("Open a file", "Enter an existing filename:")

        if not filename:
            return
        
        

        data = self.controller.open_file(filename)
        
        # Clear current state (optional, depends on your requirements)
        self.class_boxes.clear()
        self.relationshipsList.clear()

        # Load classes
        for class_data in data['classes']:
            for class_info in class_data:
                next_x, next_y = self.get_next_position()  # Calculate next position
                self.class_boxes.append({
                    'class_name': class_info['name'],
                    'fields': class_info['fields'],
                    'methods': class_info['methods'],
                    'x': next_x,
                    'y': next_y
                })

        # Load relationships
        for rel in data['relationships']:
            self.relationshipsList.append({
                'source': rel['source'],
                'destination': rel['destination'],
                'type': rel['type']
            })
        
        # Refresh GUI to reflect the loaded diagram
        self.update_relationship_tracker()
        self.redraw_canvas()

    def save_file(self):
        """
        Saves a file.

        Parameters:
            filename -- The desired filename, or the name of the file to overwrite

        Returns:
            theFile -- The saved file
        """
        
        filename = simpledialog.askstring("Save File", "Enter a valid filename:")
        
        if not filename:
            return  # User cancelled, exit the method

        # Prepare the data for serialization
        data = {
            "classes": [[{"name": box['class_name'], "fields": box['fields'], "methods": box['methods']} for box in self.class_boxes]],
            "relationships": self.relationshipsList
        }

        # Serialize data to JSON and write it to the file
        SaveLoad.save(self, data, filename)

        # Optionally, show a message to the user
        messagebox.showinfo("Save Diagram", f"Diagram saved successfully to {filename}.")

        return filename
   
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
        
        fields = []
        methods = []

        self.controller.add_class(class_name)     

        next_x, next_y = self.get_next_position()
                
        self.class_boxes.append({'class_name': class_name, 'fields': fields, 'methods': methods, 'x': next_x, 'y': next_y})

        self.create_class_box(self.diagram_canvas, class_name, fields, methods, next_x,next_y)

        return class_name
    
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
        indent_spacing = 10  # Indentation for sub-items like parameters
        bullet = "\u2022"  # Unicode character for a bullet point

        # Calculate box height dynamically based on contents
        num_text_lines = 2 + len(fields) + sum(len(method['parameters']) + 1 for method in methods) + (2 if fields else 0) + (2 if methods else 0)
        box_height = text_spacing * num_text_lines

        canvas.create_rectangle(x, y, x + box_width, y + box_height, fill='lightgray', outline='black')
        canvas.create_text(x + box_width / 2, y + text_spacing, text=class_name, font=('TkDefaultFont', 10, 'bold'))

        current_y = y + text_spacing * 2
        if fields:
            # Add "Fields:" label
            canvas.create_text(x + 10, current_y, text="Fields:", anchor="w", font=('TkDefaultFont', 10, 'underline'))
            current_y += text_spacing

        for field in fields:
            canvas.create_text(x + 10, current_y, text=field, anchor="w")
            current_y += text_spacing

        if methods:
            # Add some space before "Methods:" label if there are fields
            if fields:
                current_y += text_spacing / 2

            # Add "Methods:" label
            canvas.create_text(x + 10, current_y, text="Methods:", anchor="w", font=('TkDefaultFont', 10, 'underline'))
            current_y += text_spacing

        for method in methods:
            canvas.create_text(x + 10, current_y, text=method['name'], anchor="w")
            current_y += text_spacing
            for param in method['parameters']:
                # Indent and bullet each parameter
                canvas.create_text(x + 10 + indent_spacing, current_y, text=f"{bullet} {param}", anchor="w")
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
        
        self.controller.delete_class(class_name)

        class_found = False
        for i, class_box in enumerate(self.class_boxes):
            if class_box['class_name'] == class_name:
                del self.class_boxes[i]
                class_found = True
                break  # Correctly placed to break out of the loop when a class is found and deleted
            
        if class_found:
            self.relationshipsList[:] = [rel for rel in self.relationshipsList if rel['source'] != class_name and rel['destination']!= class_name]
        self.redraw_canvas()  # Call redraw_canvas outside the loop to refresh the canvas once after any deletion
        self.update_relationship_tracker()

        

        if not class_found:
            messagebox.showinfo("Delete Class", "Class not found!")
            return
        
        messagebox.showinfo("Delete Class", f"'{class_name}' has been removed.")

        return class_name
 
    def redraw_canvas(self):
        self.diagram_canvas.delete("all")  # Clears the canvas
        # Draw relationships
        for relationship in self.relationshipsList:
            source = next((box for box in self.class_boxes if box['class_name'] == relationship["source"]), None)
            destination = next((box for box in self.class_boxes if box['class_name'] == relationship["destination"]), None)

            if source and destination:
                # Calculate center points of source and destination boxes
                source_center = (source['x'] + 75, source['y'] + (20 * (2 + len(source.get('fields', [])) + len(source.get('methods', []))) / 2))
                destination_center = (destination['x'] + 75, destination['y'] + (20 * (2 + len(destination.get('fields', [])) + len(destination.get('methods', []))) / 2))

                # Draw a line between them
                self.diagram_canvas.create_line(source_center, destination_center, arrow=tk.LAST)

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
        dialog = RenameClassDialog(self,"Rename Class")
        if dialog.result:
            old_name, new_name = dialog.result

            self.controller.rename_class(old_name,new_name)

            for class_box in self.class_boxes:
                if class_box['class_name'] == old_name:
                    class_box['class_name'] = new_name
                    break
            #TODO
            for relationship in self.relationshipsList:
                if relationship['source'] == old_name:
                    relationship['source'] = new_name
                elif relationship['destination'] == old_name:
                    relationship['destination'] = new_name

            self.update_relationship_tracker()
            self.redraw_canvas()
            messagebox.showinfo("Rename Class", f"'{old_name}' has been renamed to '{new_name}'")   

    def add_attribute_to_class(self):
    
        AddAttributeDialog(self, title="Add Attribute")
    
    def add_attribute(self, class_name, attribute_name, attribute_type):
        if not attribute_name or not class_name or attribute_type not in ['field', 'method']:
            messagebox.showinfo("Error", "Invalid input provided.")
            return

        self.controller.add_attribute(class_name, attribute_name, attribute_type)

        parameters = []

        # Find the class box with the given class_name
        for class_box in self.class_boxes:
            if class_box['class_name'] == class_name:
                if attribute_type == 'field':
                    class_box.setdefault('fields', []).append(attribute_name)
                else:  # attribute_type == 'method'
                    # Append a dictionary for the method with its parameters
                    class_box.setdefault('methods', []).append({'name': attribute_name, 'parameters': parameters})

                self.redraw_canvas()  # Refresh the canvas to show the updated class box
                success_message = f"Field '{attribute_name}' added to class '{class_name}'." if attribute_type == 'field' else f"Method '{attribute_name}' added with parameters {parameters} to class '{class_name}'."
                messagebox.showinfo("Success", success_message)


    def delete_relationship(self):
        dialog = DeleteRelationshipDialog(self, "Delete Relationship", self.relationshipsList)
        if dialog.result:
            selected_rel = dialog.result
            # Extract the source and destination class names from the dialog's result
            source_class = selected_rel['source']
            destination_class = selected_rel['destination']

            
            # Attempt to delete the relationship using the controller
            self.controller.delete_relationship(source_class, destination_class)
            # If successful, update the relationships list and UI accordingly
            self.relationshipsList[:] = [rel for rel in self.relationshipsList if not (rel['source'] == source_class and rel['destination'] == destination_class)]
            self.update_relationship_tracker()
            self.redraw_canvas()
            messagebox.showinfo("Success", "Relationship deleted successfully.")

    def add_relationship(self):
        """
        Lists all relationships of a class
        Parameters:
            self -- the parent

        Returns:
            none
        """
        dialog = AddRelationshipDialog(self, "Add Relationship")
        if dialog.result:
            
            source_class, destination_class, relationship_type = dialog.result

            self.controller.add_relationship(source_class, destination_class, relationship_type)
            
            # Add the relationship
            self.relationshipsList.append({
                "source": source_class,
                "destination": destination_class,
                "type": relationship_type
            })

            self.update_relationship_tracker()

            self.redraw_canvas()

    def delete_attribute(self):
    # Ask for the class name from which to delete an attribute
        dialog_result = DeleteAttributeDialog(self, title="Delete Attribute").result
        if dialog_result:
            class_name, attribute_name, attribute_type = dialog_result
            self.controller.delete_attribute(class_name, attribute_name, attribute_type)
            # Find the class
            for class_box in self.class_boxes:
                if class_box['class_name'] == class_name:
                    # Check the attribute type and delete accordingly
                    if attribute_type == 'field' and 'fields' in class_box and attribute_name in class_box['fields']:
                        class_box['fields'].remove(attribute_name)
                    elif attribute_type == 'method' and 'methods' in class_box:
                        methods_list = class_box['methods']
                        class_box['methods'] = [m for m in methods_list if m['name'] != attribute_name]
                    else:
                        messagebox.showinfo("Error", f"{attribute_type.capitalize()} '{attribute_name}' not found in class '{class_name}'.")
                        return
                    self.redraw_canvas()
                    messagebox.showinfo("Success", f"{attribute_type.capitalize()} '{attribute_name}' deleted from class '{class_name}'.")
                    return
            messagebox.showinfo("Error", f"Class '{class_name}' not found.")

            return [class_name, attribute_name, attribute_type]

    def rename_attribute(self):
        class_name = simpledialog.askstring("Rename Attribute", "Enter the name of the class:", parent=self)
        
        attribute_name = simpledialog.askstring("Rename Attribute", "Enter the name of the attribute to rename:", parent=self)
        
        new_name = simpledialog.askstring("Rename Attribute", "Enter the new name for the attribute:", parent=self)
        
        for class_box in self.class_boxes:
            if class_box['class_name'] == class_name:
                # Check and rename in fields
                if attribute_name in class_box.get('fields', []):
                    self.controller.rename_attribute(class_name, attribute_name, new_name, "field")
                    index = class_box['fields'].index(attribute_name)
                    class_box['fields'][index] = new_name
                    self.redraw_canvas()
                    messagebox.showinfo("Success", f"Field '{attribute_name}' renamed to '{new_name}' in class '{class_name}'.")
                    return
                # Check and rename in methods
                elif attribute_name in class_box.get('methods', []):
                    self.controller.rename_attribute(class_name, attribute_name, new_name, "method")
                    index = class_box['methods'].index(attribute_name)
                    class_box['methods'][index] = new_name
                    self.redraw_canvas()
                    messagebox.showinfo("Success", f"Method '{attribute_name}' renamed to '{new_name}' in class '{class_name}'.")
                    return
        messagebox.showinfo("Error", "Attribute not found.")

        return [class_name, attribute_name, new_name]

    def new_param(self):
        """
        Adds a new parameter to a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        dialog_result = AddParameterDialog(self, title="Add Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result
            self.controller.add_param(class_name,method_name,param_name)

            if not class_name or not method_name or not param_name:
                messagebox.showinfo("Error","All fields are required.")
                return
            
            found_class = False
            for class_box in self.class_boxes:
                if class_box['class_name'] == class_name:
                    found_class = True
                    found_method = False
                    for method in class_box.get('methods',[]):
                        if method['name'] == method_name:
                            found_method = True
                            method.setdefault('parameters',[]).append(param_name)
                            break
                        if not found_method:
                            messagebox.showinfo("Add Parameter", f"Method '{method_name}' not found.")
                            return
                        break
            if not found_class:
                messagebox.showinfo("Add Parameter", f"Class '{class_name}' not found.")
                return
            
            self.redraw_canvas()
            messagebox.showinfo("Success", f"Parameter '{param_name}' added to '{class_name}")
            return [class_name, method_name, param_name]
    
    def delete_param(self):
        dialog_result = DeleteParameterDialog(self, "Delete Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result

            self.controller.delete_param(class_name, method_name, param_name)


            found_class = False
            for class_box in self.class_boxes:
                if class_box['class_name'] == class_name:
                    found_class = True
                    found_method = False
                    for method in class_box.get('methods', []):
                        if method['name'] == method_name:
                            found_method = True
                            if param_name in method.get('parameters', []):
                                method['parameters'].remove(param_name)
                                self.redraw_canvas()
                                messagebox.showinfo("Success", f"Parameter '{param_name}' removed from method '{method_name}' in class '{class_name}'.")
                                return
                            else:
                                messagebox.showinfo("Error", f"Parameter '{param_name}' not found in method '{method_name}'.")
                                return
                    if not found_method:
                        messagebox.showinfo("Error", f"Method '{method_name}' not found in class '{class_name}'.")
                        return
            if not found_class:
                messagebox.showinfo("Error", f"Class '{class_name}' not found.")
            return [class_name, method_name, param_name]
    
    def rename_param(self):
        """
        Renames a parameter in a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        dialog_result = RenameParameterDialog(self, title="Rename Parameter").result
        if dialog_result:
            class_name, method_name, old_param_name, new_param_name = dialog_result

            self.controller.rename_param(class_name, method_name , old_param_name, new_param_name)

            for class_box in self.class_boxes:
                if class_box['class_name'] == class_name:
                    for method in class_box.get('methods', []):
                        if method['name'] == method_name and old_param_name in method.get('parameters', []):
                            index = method['parameters'].index(old_param_name)
                            method['parameters'][index] = new_param_name
                            self.redraw_canvas()
                            messagebox.showinfo("Success", "Parameter renamed successfully.")
                            return
            messagebox.showinfo("Error", "Parameter not found.")
    
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

class RenameClassDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Old Class Name:").grid(row=0)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.grid(row=0, column=1)

        tk.Label(master, text="New Class Name:").grid(row=1)
        self.new_name_entry = tk.Entry(master)
        self.new_name_entry.grid(row=1, column=1)

        return self.class_name_entry  # Set focus on the first entry widget

    def apply(self):
        self.result = (self.class_name_entry.get(), self.new_name_entry.get())

class AddAttributeDialog(simpledialog.Dialog):

    def __init__(self, parent, title=None):
        super().__init__(parent, title=title)

    def body(self, master):

        tk.Label(master,text="Class Name:").grid(row=0)
        self.entry_class_name = tk.Entry(master)
        self.entry_class_name.grid(row = 0, column = 1)
        tk.Label(master, text="Attribute Name:").grid(row=1)
        self.entry_attribute_name = tk.Entry(master)
        self.entry_attribute_name.grid(row=1, column=1)

        self.attribute_type = tk.StringVar(value="field")
        tk.Radiobutton(master, text="Field", variable=self.attribute_type, value="field").grid(row=2, column=0)
        tk.Radiobutton(master, text="Method", variable=self.attribute_type, value="method").grid(row=2, column=1)

        return self.entry_attribute_name

    def apply(self):
        class_name = self.entry_class_name.get()
        attribute_name = self.entry_attribute_name.get()
        attribute_type = self.attribute_type.get()
        # Now, we can call the main method to add the attribute with all required information
        self.parent.add_attribute(class_name, attribute_name, attribute_type)

class DeleteAttributeDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Class Name:").grid(row=0)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.grid(row=0, column=1)

        tk.Label(master, text="Attribute Name:").grid(row=1)
        self.attribute_name_entry = tk.Entry(master)
        self.attribute_name_entry.grid(row=1, column=1)

        tk.Label(master, text="Attribute Type:").grid(row=2)
        self.attribute_type_var = tk.StringVar(value="field")
        tk.Radiobutton(master, text="Field", variable=self.attribute_type_var, value="field").grid(row=2, column=1)
        tk.Radiobutton(master, text="Method", variable=self.attribute_type_var, value="method").grid(row=2, column=2)

        return self.class_name_entry  # initial focus

    def apply(self):
        self.result = (self.class_name_entry.get(), self.attribute_name_entry.get(), self.attribute_type_var.get())

class AddParameterDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text="Class Name:").grid(row=0)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.grid(row=0, column=1)

        tk.Label(master, text="Method Name:").grid(row=1)
        self.method_name_entry = tk.Entry(master)
        self.method_name_entry.grid(row=1, column=1)

        tk.Label(master, text="Parameter Name:").grid(row=2)
        self.param_name_entry = tk.Entry(master)
        self.param_name_entry.grid(row=2, column=1)

        return self.class_name_entry  # initial focus

    def apply(self):
        class_name = self.class_name_entry.get()
        method_name = self.method_name_entry.get()
        param_name = self.param_name_entry.get()
        self.result = (class_name, method_name, param_name)

class DeleteParameterDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Class Name:").grid(row=0)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.grid(row=0, column=1)

        tk.Label(master, text="Method Name:").grid(row=1)
        self.method_name_entry = tk.Entry(master)
        self.method_name_entry.grid(row=1, column=1)

        tk.Label(master, text="Parameter Name:").grid(row=2)
        self.param_name_entry = tk.Entry(master)
        self.param_name_entry.grid(row=2, column=1)

        return self.class_name_entry  # Set focus on the first entry widget

    def apply(self):
        class_name = self.class_name_entry.get()
        method_name = self.method_name_entry.get()
        param_name = self.param_name_entry.get()
        self.result = (class_name, method_name, param_name)
  
class RenameParameterDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Class Name:").grid(row=0)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.grid(row=0, column=1)

        tk.Label(master, text="Method Name:").grid(row=1)
        self.method_name_entry = tk.Entry(master)
        self.method_name_entry.grid(row=1, column=1)

        tk.Label(master, text="Parameter Name:").grid(row=2)
        self.param_name_entry = tk.Entry(master)
        self.param_name_entry.grid(row=2, column=1)

        tk.Label(master, text="New Parameter Name:").grid(row=3)
        self.new_param_name_entry = tk.Entry(master)
        self.new_param_name_entry.grid(row=3, column=1)

        return self.class_name_entry  # Set focus on the first entry widget

    def apply(self):
        self.result = (self.class_name_entry.get(), self.method_name_entry.get(), self.param_name_entry.get(), self.new_param_name_entry.get())
        
class AddRelationshipDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Source Class:").grid(row=0)
        self.source_entry = tk.Entry(master)
        self.source_entry.grid(row=0, column=1)

        tk.Label(master, text="Destination Class:").grid(row=1)
        self.destination_entry = tk.Entry(master)
        self.destination_entry.grid(row=1, column=1)

        tk.Label(master, text="Relationship Type:").grid(row=2)
        self.relationship_type = tk.StringVar(master)
        self.relationship_type.set("Aggregation")  # default value
        tk.OptionMenu(master, self.relationship_type, "Aggregation", "Composition", "Generalization", "Inheritence").grid(row=2, column=1)

        return self.source_entry  # initial focus

    def apply(self):
        source_class = self.source_entry.get()
        destination_class = self.destination_entry.get()
        relationship_type = self.relationship_type.get()
        self.result = (source_class, destination_class, relationship_type)

class DeleteRelationshipDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, relationships=[]):
        self.relationshipsList = relationships
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Select Relationship:").grid(row=0)
        self.relationship_var = tk.StringVar(master)
        self.relationship_var.set("Choose a relationship")  # default value

        relationships_str = [f"{r['source']} - {r['type']} - {r['destination']}" for r in self.relationshipsList]
        self.relationship_menu = tk.OptionMenu(master, self.relationship_var, *relationships_str)
        self.relationship_menu.grid(row=0, column=1)

        return self.relationship_menu  # initial focus

    def apply(self):
        selected_relationship_str = self.relationship_var.get()
        self.result = next((r for r in self.relationshipsList if f"{r['source']} - {r['type']} - {r['destination']}" == selected_relationship_str), None)

if __name__ == "__main__":
    app = UMLDiagramEditor()
    app.mainloop()
