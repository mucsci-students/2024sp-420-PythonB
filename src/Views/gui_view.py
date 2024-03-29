from tkinter import ttk
from Models.uml_diagram import UML_Diagram

import json
import tkinter as tk
from tkinter import filedialog
import webbrowser
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import simpledialog

class GUI_View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LambdaLegion UML Program (CWorld Edition) V1.1")
        # Calculate the center position and set the geometry
        window_width, window_height = 1000, 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.class_boxes = []
        self.relationshipsList = []
        self.create_menu()
        self.create_sidebar()
        self.create_diagram_space()
        self.update_relationship_tracker()
        self._commands = []

    def draw(self, diagram: UML_Diagram) -> None:
        #TODO: draw the whole diagram
        print('Draw this diagram')
        pass

    def clear(self) -> None:
        #TODO: remove everything of the diagram that was drawn
        print('clear this diagram')
        pass

    def listen(self) -> str:
        '''
        Wait for user action and return as a command
        '''
        #TODO: change this to an command received from user action
        #       Or do this in gui controller
        cmd = input('GUI is listening...')
        print('input received')
        cmd = 'undo'
        return cmd

    def create_menu(self):
        """
        Initializes the menu bar with cascading menus for File and Help.
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
        file_menu.add_command(label="Load", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)


        # We may want Undo/Redo in here
            # Will probably try to make buttons for this though
        # Edit
        # edit_menu = Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Help Menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="View Help", command=self.show_help_messagebox)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        menu_bar.add_separator()
        menu_bar.add_separator()

        menu_bar.add_command(label = "Undo", command = self.undo)
        menu_bar.add_command(label = "Redo", command = self.redo)
    
    def show_help_messagebox(self):
        help_content = """
            Valid Input:
                - Names must start with a letter
                - Can include numbers, dashes (-), and underscores (_).

            Requirements:
                - To create relationships, you need at least two classes.

            Visuals and Meanings:
                - Aggregation: An empty diamond to a normal arrow.
                - Composition: A filled diamond to a normal arrow.
                - Realization: A dashed line to a hollow arrow.
                - Inheritance: A solid line to an empty arrow.

            This quick guide helps you understand the basics of interacting with the UML editor.
                """
        messagebox.showinfo("Help - CWorld UML Program", help_content, parent=self)

    def undo(self):
        # TODO: Hook Undo in here
        pass

    def redo(self):
        # TODO: Hook Redo in here
        pass

    def create_sidebar(self):
        self.sidebar = tk.Frame(self, width=200, bg='lightgray')
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0), pady=(13, 12))

        # Example button with dropdown for "Add Class"
        self.btn_class = tk.Button(self.sidebar, text="Classes", command=self.class_options_menu)
        self.btn_class.pack(fill=tk.X, padx=(5, 5), pady=(10, 5))

        if True:
        # if len(self.class_boxes) > 1:
            self.btn_relationships = tk.Button(self.sidebar, text="Relationships", command=self.relationship_options_menu)
            self.btn_relationships.pack(fill=tk.X, padx=(5, 5), pady=(5, 5))

        # if True:
        if len(self.class_boxes) > 0:
            self.btn_methods = tk.Button(self.sidebar, text="Attributes", command=self.attributes_options_menu)
            self.btn_methods.pack(fill=tk.X, padx=(5, 5), pady=(5, 5))

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
        self.diagram_canvas = tk.Canvas(self, bg = 'white')
        # Pack the canvas to fill the remaining space after the sidebar
        self.diagram_canvas.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    def class_options_menu(self):
        # Create a menu that will appear at the current mouse position
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Add Class", command=self.add_class)
        # This will show Delete Class and Rename Class only when there is
            # at least one class card.
        if len(self.class_boxes) > 0:
            menu.add_command(label="Delete Class", command=self.delete_class)
            menu.add_command(label="Rename Class", command=self.rename_class)

        try:
            # Display the menu at the current mouse position
            menu.tk_popup(x=self.sidebar.winfo_pointerx(), y=self.sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            menu.grab_release()

    def attributes_options_menu(self):
        menu = Menu(self, tearoff=0)
        if len(self.class_boxes) > 0:
            # TODO: Implement this logic once new backend hooked in:
            menu.add_command(label="Add Attribute", command=self.add_attribute_to_class)
            ## If attributes > 0. For next 2 lines ##
            menu.add_command(label="Delete Attribute", command=self.delete_attribute)
            menu.add_command(label="Rename Rename", command=self.rename_attribute)
            ## if Methods > 0. Indent next 4 ##
            menu.add_separator()
            menu.add_command(label="Add Parameter", command=self.add_param)
            ## if Parameters > 0. Indent next 2 ##
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
        if len(self.class_boxes) > 1:
            menu.add_command(label="Add", command=self.add_relationship)
        # The below check *should* work, but given the state of things, I can't add a relation to test
            # Until then, as long as there is at least 2 classes, Delete relation will appear.
        # if len(self.relationshipsList) > 0:
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
        # TODO: This either needs removed or needs to ask if you want to save, then restart the program
            # new Diagram and everything
            # If removed, this needs to be removed from the file menu
        # Placeholder for new file action
        messagebox.showinfo("Action", "Create a new file")

    # TODO: self.controller
    def open_file(self):
        file_name = simpledialog.askstring("Load a File","Enter a Valid Filename", parent = self)
        data = self.controller.open_file(file_name)

        self.class_boxes.clear()
        self.relationshipsList.clear()

        # Assuming classes and relationships are directly stored under the top-level object
        for class_data in data['classes']:
            fields = [{'name': f['name'], 'type': f.get('type', 'Unknown')} for f in class_data.get('fields', [])]
            methods = [{
                'name': m['name'],
                'return_type': m.get('return_type', 'void'),
                'params': [{'name': p['name'], 'type': p.get('type', 'Unknown')} for p in m.get('params', [])]
            } for m in class_data.get('methods', [])]

            # Use your existing logic to calculate the next position
            next_x, next_y = self.get_next_position()

            # Append the class along with its fields and methods
            self.class_boxes.append({
                'class_name': class_data['name'],
                'fields': fields,
                'methods': methods,
                'x': next_x,
                'y': next_y
            })

    # Handling relationships
        for relationship in data['relationships']:
            self.relationshipsList.append({
                'source': relationship['source'],
                'destination': relationship['destination'],
                'type': relationship['type']
            })

        # Refreshing GUI elements
        self.update_relationship_tracker()
        self.redraw_canvas()
        messagebox.showinfo("Open Diagram", f"Diagram loaded successfully from {file_name}.")


    def save_file(self):
        # Open a dialog asking for the filename to save to
        filename = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not filename:
            # User cancelled the save
            return

        # TODO: Hook save in here

        # Notify the user of success
        messagebox.showinfo("Save File", "The diagram has been saved successfully.")

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

        # TODO: self.controller
        new_command = 'add class ' + class_name
        self._commands.append(new_command)
        # self.controller.add_class(class_name)

        next_x, next_y = self.get_next_position()
        box = Class_Box(self.diagram_canvas, class_name, next_x, next_y)
        self.class_boxes.append(box)
        # TODO:
        # This doesn't work, creates a second sidebar instead of replacing original
        # May not need it depending on what we recreate on load
        # if len(self.class_boxes) <= 2:
        #     self.create_sidebar()

        # self.create_class_box(self.diagram_canvas, class_name, fields, methods, next_x,next_y)

        return class_name

    def get_next_position(self):
        # TODO: This should probably be more involved as the cards won't just appear in a row
            # Probably not high priority
        # For simplicity, let's just arrange them in a horizontal line for now
        spacing = 10  # Spacing between class boxes
        box_width = 150  # Assume a fixed width for now
        x, y = 50, 50  # Starting position for the first class box

        if self.class_boxes:
            # Get the position of the last class box
            index = len(self.class_boxes) - 1
            last_box = self.class_boxes[index]
            x, y = last_box._x, last_box._y

            # Move to the next position to the right
            x += box_width + spacing

        return x, y

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
        # TODO: self.controller
        new_command = "delete class " + class_name
        self._commands.add(new_command)
        # self.controller.delete_class(class_name)

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
        # for class_box in self.class_boxes:
        #     self.create_class_box(self.diagram_canvas, class_box['class_name'], class_box.get('fields', []), class_box.get('methods', []), class_box['x'], class_box['y'])

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
        dialog = Rename_Class_Dialog(self,"Rename Class")
        if dialog.result:
            old_name, new_name = dialog.result
            # TODO: self.controller
            new_command = "rename class " + old_name + " " + new_name
            self._commands.add(new_command)
            # self.controller.rename_class(old_name,new_name)

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
        Add_Attribute_Dialog(self, title="Add Attribute")

    # TODO: This either needs broken into add_field and add_method
        # Or needs a conditional for if field do x if method do x
    def add_attribute(self, class_name, attribute_name, attribute_type):
        if not attribute_name or not class_name or attribute_type not in ['field', 'method']:
            messagebox.showinfo("Error", "Invalid input provided.")
            return
        # TODO: self.controller
        new_command = "add "
        if (attribute_type == "field"):
            new_command += "field " + attribute_name
        else:
            new_command += "method " + attribute_name
        # self.controller.add_attribute(class_name, attribute_name, attribute_type)

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
        dialog = Delete_Relationship_Dialog(self, "Delete Relationship", self.relationshipsList)
        if dialog.result:
            selected_rel = dialog.result
            # Extract the source and destination class names from the dialog's result
            src = selected_rel['source']
            dest = selected_rel['destination']

            # Attempt to delete the relationship using the controller
            # TODO: self.controller
            new_command = "delete relationship " + src + " " + dest
            self._commands.add(new_command)
            # self.controller.delete_relationship(source_class, destination_class)
            
            # If successful, update the relationships list and UI accordingly
            self.relationshipsList[:] = [rel for rel in self.relationshipsList if not (rel['source'] == src and rel['destination'] == dest)]
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
        # TODO: This will break once our back end is in
        # Create list of classes in Diagram
        class_options = []
        for cb in self.class_boxes:
            
            class_options.append(cb._name)
        
        dialog = Add_Relationship_Dialog(self, class_options, "Add Relationship")
        if dialog.result:

            src, dest, rel = dialog.result
            # TODO: self.controller
            new_command = "add relation " + src + " " + dest + " " + rel
            self._commands.add(new_command)
            # self.controller.add_relationship(source_class, destination_class, relationship_type)

            # Add the relationship
            self.relationshipsList.append({
                "source": src,
                "destination": dest,
                "type": rel
            })

            self.update_relationship_tracker()

            self.redraw_canvas()

    # TODO: This is the same as the above attribute
    def delete_attribute(self):
        # Ask for the class name from which to delete an attribute
        dialog_result = Delete_Attribute_Dialog(self, title="Delete Attribute").result
        if dialog_result:
            class_name, attribute_name, attribute_type = dialog_result
            # TODO: self.controller
            new_command = "delete " + attribute_type + " " + class_name + " " + attribute_name
            self._commands.add(new_command)
            # self.controller.delete_attribute(class_name, attribute_name, attribute_type)
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

    # TODO: Either needs broken apart, or needs to be told if it's method or field
            # Should not assume there is not a method and a field with the same name
    def rename_attribute(self):
        class_name = simpledialog.askstring("Rename Attribute", "Enter the name of the class:", parent=self)

        old_name = simpledialog.askstring("Rename Attribute", "Enter the name of the attribute to rename:", parent=self)

        new_name = simpledialog.askstring("Rename Attribute", "Enter the new name for the attribute:", parent=self)

        for class_box in self.class_boxes:
            if class_box['class_name'] == class_name:
                # Check and rename in fields
                if old_name in class_box.get('fields', []):
                    # TODO: self.controller
                    new_command = "rename field " + class_name + " " + old_name + " " + new_name
                    self._commands.add(new_command)
                    # self.controller.rename_attribute(class_name, attribute_name, new_name, "field")
                    index = class_box['fields'].index(old_name)
                    class_box['fields'][index] = new_name
                    self.redraw_canvas()
                    messagebox.showinfo("Success", f"Field '{old_name}' renamed to '{new_name}' in class '{class_name}'.")
                    return
                # Check and rename in methods
                elif old_name in class_box.get('methods', []):
                    # TODO: self.controller
                    new_command = "rename method " + class_name + " " + old_name + " " + new_name
                    self._commands.add(new_command)
                    # self.controller.rename_attribute(class_name, attribute_name, new_name, "method")
                    index = class_box['methods'].index(old_name)
                    class_box['methods'][index] = new_name
                    self.redraw_canvas()
                    messagebox.showinfo("Success", f"Method '{old_name}' renamed to '{new_name}' in class '{class_name}'.")
                    return
        messagebox.showinfo("Error", "Attribute not found.")
        return [class_name, old_name, new_name]

    def add_param(self):
        """
        Adds a new parameter to a class

        Parameters:
            self -- The parent

        Returns:
            None
        """
        dialog_result = Add_Parameter_Dialog(self, title="Add Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result
            # TODO: self.controller
            new_command = "add param " + " " + class_name + " " + param_name
            self._commands.add(new_command)
            # self.controller.add_param(class_name,method_name,param_name)

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
        dialog_result = Delete_Parameter_Dialog(self, "Delete Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result
            # TODO: self.controller
            new_command = "delete param " + class_name + " " + method_name + " " + param_name
            self._commands(new_command)
            # self.controller.delete_param(class_name, method_name, param_name)

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
        # This is all yellow because these paramaters don't exist anymore
            # I'm leaving the function here as a stump/reminder for what we need to do
                # Just meaning to do rename_param, not that this code is necessary
        dialog_result = Rename_Parameter_Dialog(self, title="Rename Parameter").result
        if dialog_result:
            class_name, method_name, old_name, new_name = dialog_result
            # TODO: self.controller
            new_command = "rename param " + class_name + " " + method_name + " " + old_name + " " + new_name
            self._commands.add(new_command)
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
        webbrowser.open(url, new = new)

    # TODO: This is effectively just a proof f concept, it does not work quite right
        # commented out because it pops up on load.
    # def help_input(self):
    #     """
    #     Displays valid input options
    #     """
    #     display = (
    #         "Valid inputs must start with a letter."
    #         "\nOther characters can be alphanumeric, -, or _."
    #     )
    #     popup = tk.Tk()
    #     popup.wm_title("!")
    #     label = ttk.Label(popup, text = display)
    #     label.pack(side="top", fill="x", pady=10)
    #     tk.messagebox.showinfo(display)
    #     B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    #     B1.pack()


class Rename_Class_Dialog(simpledialog.Dialog):
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

class Add_Attribute_Dialog(simpledialog.Dialog):

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

class Delete_Attribute_Dialog(simpledialog.Dialog):
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

class Add_Parameter_Dialog(simpledialog.Dialog):
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

class Delete_Parameter_Dialog(simpledialog.Dialog):
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

class Rename_Parameter_Dialog(simpledialog.Dialog):
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

class Add_Relationship_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options = None, title = None):
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Source Class:").grid(row=0)
        self._src = tk.StringVar(master)
        tk.OptionMenu(master, self._src, *self._class_options).grid(row = 0, column = 1)

        tk.Label(master, text="Destination Class:").grid(row=1)
        self._dest = tk.StringVar(master)
        tk.OptionMenu(master, self._dest, *self._class_options).grid(row = 1, column = 1)

        tk.Label(master, text="Relationship Type:").grid(row=2)
        self._rel_type = tk.StringVar(master)
        rel_options = ["Aggregation", "Composition", "Inheritance", "Realization"]
        tk.OptionMenu(master, self._rel_type, *rel_options).grid(row=2, column=1)

        return self._src # initial focus

    def apply(self):
        src = self._src.get()
        dest = self._dest.get()
        rel_type = self._rel_type.get()
        self.result = (src, dest, rel_type)

class Delete_Relationship_Dialog(simpledialog.Dialog):
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

class Class_Box():
    def __init__(self, canvas, name:str, x, y) -> None:
        self._name = name
        self._canvas = canvas
        self._methods = []
        self._fields = []
        self._width = 150
        self._text_spacing = 20
        self._indent_spacing = 10
        self._x = x
        self._y = y
        self._click_x = x
        self._click_y = y
        self._last_x = 0
        self._last_y = 0
        self._box, self._box_text, self._height = self.create_class_box(canvas)

        canvas.tag_bind(self._box, '<Button-1>', self.on_click)
        canvas.tag_bind(self._box, '<B1-Motion>', self.on_move)
        canvas.tag_bind(self._box_text, '<Button-1>', self.on_click)
        canvas.tag_bind(self._box_text, '<B1-Motion>', self.on_move)

    def on_move(self, e):
        offset_x = e.x - self._last_x
        offset_y = e.y - self._last_y
        self._canvas.move(self._box, offset_x, offset_y)
        self._canvas.move(self._box_text, offset_x, offset_y)
        self._last_x = self._last_x + offset_x
        self._last_y = self._last_y + offset_y
        self._x = self._last_x
        self._y = self._last_y

    def on_click(self, e):
        self._last_x = e.x
        self._last_y = e.y

    def create_class_box(self, canvas):
        # TODO: This value is just hard coded (obviously)
            # It should could the number of lines in the class box
        num_text_lines = 2
        # Calculate box height dynamically based on contents
        box_height = self._text_spacing * num_text_lines

        box = canvas.create_rectangle(self._x, self._y, self._x + self._width, self._y + box_height, fill='lightgray', outline='black')
        box_text = canvas.create_text(self._x + self._width / 2, self._y + self._text_spacing, text=self._name, font=('TkDefaultFont', 10, 'bold'))

        # TODO: We will need to add more info to the Class_Box
            # Removed all of the old functionality as it would never be used again.
        return box, box_text, box_height
        
if __name__ == "__main__":
    app = GUI_View()
    app.mainloop()