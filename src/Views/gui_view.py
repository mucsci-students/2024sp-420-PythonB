from tkinter import ttk

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#===================================== View Setup =====================================#

class GUI_View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LambdaLegion UML Program (CWorld Edition) V1.1")

        # Center the window on the screen
        window_width, window_height = 1000, 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # Set the window size and position
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self._class_boxes = []
        self._sidebar_buttons = []

        # TODO: class_list could be moved here
        self.relationshipsList = []
        self.create_menu()
        self.create_sidebar()
        self.update_button_state()
        self.create_diagram_space()
        self.update_relationship_tracker()

        self._user_command = tk.StringVar()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self) -> None:
        self._user_command.set('quit')
        self.clear()

    def draw_class(self, name, x=None, y=None) -> None:
        if not x or not y:
            x, y = self.get_next_position()
        self._class_boxes.append(Class_Box(self.diagram_canvas, name, x, y))

    def clear(self) -> None:
        self.diagram_canvas.delete("all")
        self._class_boxes.clear()

    def listen(self) -> str:
        '''
        Wait for user action and return as a command
        '''
        self.update_button_state()

        self.wait_variable(self._user_command)
        cmd = self._user_command.get()
        self._user_command.set('')
        print('Debugging: {}'.format(cmd))
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

    def undo(self):
        # TODO: Hook Undo in here
        pass

    def redo(self):
        # TODO: Hook Redo in here
        pass

    def create_sidebar(self):
        self._sidebar = tk.Frame(self, width = 200, bg = 'lightgray')
        self._sidebar.pack(side = LEFT, fill = tk.Y, padx = (5, 0), pady = (13, 12))

        self._btn_class = tk.Button(self._sidebar, text = "Classes", command = self.class_options_menu)
        self._btn_class.pack(fill = tk.X, padx = (5, 5), pady = (10, 5))

        self._btn_methods = tk.Button(self._sidebar, text = "Methods", command = self.methods_options_menu)
        self._btn_methods.pack(fill = tk.X, padx = (5, 5), pady = (5, 5))

        self._btn_fields = tk.Button(self._sidebar, text = "Fields", command = self.fields_options_menu)
        self._btn_fields.pack(fill = tk.X, padx = (5, 5), pady = (5, 5))

        self._btn_relations = tk.Button(self._sidebar, text = "Relationships", command = self.relations_options_menu)
        self._btn_relations.pack(fill = tk.X, padx = (5, 5), pady = (5, 5))
        
        tk.Label(self._sidebar, text="Relationships Tracker", bg = 'lightgray', font = ('TkDefaultFont', 10, 'bold')).pack(pady = (10, 0))

        # Relationship Tracker Listbox
        self.relationship_tracker = tk.Listbox(self._sidebar, height = 10)
        self.relationship_tracker.pack(padx = 5, pady = 5, fill = tk.BOTH, expand = True)

    def update_button_state(self):
        self._btn_class.config(state="disabled")
        self._btn_fields.config(state="disabled")
        self._btn_methods.config(state="disabled")
        self._btn_relations.config(state="disabled")

        class_count = len(self._class_boxes)
        if class_count == 0:
            self._btn_class.config(state="active")
        elif class_count == 1:
            self._btn_class.config(state="active")
            self._btn_fields.config(state="active")
            self._btn_methods.config(state="active")
        elif class_count > 1:
            self._btn_class.config(state="active")
            self._btn_fields.config(state="active")
            self._btn_methods.config(state="active")
            self._btn_relations.config(state="active")

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

#===================================== Menu Methods =====================================#

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

        self._class_boxes.clear()
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
            self._class_boxes.append({
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

#===================================== Create Menus =====================================#

    def class_options_menu(self):
        # Create a menu that will appear at the current mouse position
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label = "Add Class", command = self.add_class)
        # This will show Delete Class and Rename Class only when there is
            # at least one class card.
        if len(self._class_boxes) > 0:
            menu.add_command(label = "Delete Class", command = self.delete_class)
            menu.add_command(label = "Rename Class", command = self.rename_class)

        try:
            # Display the menu at the current mouse position
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            # Make sure the menu is torn down properly
            menu.grab_release()

    def fields_options_menu(self):
        menu = Menu(self, tearoff = 0)
        if len(self._class_boxes) > 0:
            # TODO: Replace this menu with all available classes, then when you click one of those give a dialog?
                # Potentially a second menu for these three related to that class?
            menu.add_command(label = "Add Field", command = self.add_field)
            menu.add_command(label = "Delete Field", command = self.delete_field)
            menu.add_command(label = "Rename Field", command = self.rename_field)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

    def methods_options_menu(self):
        menu = Menu(self, tearoff = 0)
        if len(self._class_boxes) > 0:
            # TODO: See field_options_menu above
            menu.add_command(label = "Add Method", command = self.add_method)
            menu.add_command(label = "Delete Method", command = self.delete_method)
            # menu.add_command(label = "Rename Method", command = self.rename_method)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

    def relations_options_menu(self):
        menu = Menu(self, tearoff=0)
        menu = Menu(self, tearoff=0)
        if True:
        # if len(self._class_boxes) > 1:
            menu.add_command(label = "Add Relationship", command = self.add_relation)
        # The below check *should* work, but given the state of things, I can't add a relation to test
            # Until then, as long as there is at least 2 classes, Delete relation will appear.
        # if len(self.relationshipsList) > 0:
            menu.add_command(label = "Delete Relation", command = self.delete_relation)

#===================================== Diagram Functions =====================================#

    def add_class(self) -> str:
        class_name = simpledialog.askstring("Input", "Enter Class Name:", parent = self)
        new_command = 'add class ' + class_name
        self._user_command.set(new_command)
      
    def delete_class(self) -> str:
        class_options = [cb._name for cb in self._class_boxes]

        dialog = Delete_Class_Dialog(self, class_options, "Delete Class")
        if dialog.result:
            class_name = dialog.result
            
            new_command = "delete class " + class_name
            self._user_command.set(new_command)
    
    def rename_class(self) -> None:
        dialog = Rename_Class_Dialog(self,"Rename Class")
        if dialog.result:
            old_name, new_name = dialog.result
            new_command = "rename class " + old_name + " " + new_name
            self._user_command.set(new_command)

            # messagebox.showinfo("Rename Class", f"'{old_name}' has been renamed to '{new_name}'")

    def add_field(self) -> None:
        class_options = [cb._name for cb in self._class_boxes]

        dialog = Add_Field_Dialog(self, class_options, "Add Field")
        if dialog.result:
            class_name, field_name, field_type = dialog.result
            new_command = "add field " + class_name + " " + field_name + " " + field_type
            self._user_command.set(new_command)

    def delete_field(self):
        class_options = [cb._name for cb in self._class_boxes]

        dialog_result = Delete_Field_Dialog(self, class_options, title = "Delete Field").result
        if dialog_result:
            class_name, field_name = dialog_result
            
            new_command = "delete field " + class_name + " " + field_name
            self._user_command.set(new_command)

    def rename_field(self):
        class_name = simpledialog.askstring("Rename Field", "Enter the name of the class:", parent=self)
        old_name = simpledialog.askstring("Rename Field", "Enter the name of the field to rename:", parent=self)
        new_name = simpledialog.askstring("Rename Field", "Enter the new name for the field:", parent=self)

        new_command = "rename field " + class_name + " " + old_name + " " + new_name
        self._user_command.set(new_command)

        # messagebox.showinfo("Success", f"Field '{old_name}' renamed to '{new_name}' in class '{class_name}'.")
        # messagebox.showinfo("Error", "Attribute not found.")

    def add_method(self):
        class_options = []
        for cb in self._class_boxes:
            class_options.append(cb._name)

        dialog = Add_Method_Dialog(self, class_options, "Add Method")

        if dialog.result:
            class_name, method = dialog.result
            new_command = "add method " + class_name + " " + method
            self._user_command.set(new_command)

    def delete_method(self):
        class_options = []
        for cb in self._class_boxes:
            class_options.append(cb._name)

        dialog_result = Delete_Method_Dialog(self, class_options, title = "Delete Method").result
        if dialog_result:
            class_name, method_name = dialog_result
            
            new_command = "delete method " + class_name + " " + method_name
            self._user_command.set(new_command)

    def rename_method(self):
        pass

    def add_param(self):
        dialog_result = Add_Parameter_Dialog(self, title="Add Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result

            new_command = "add param " + " " + class_name + " " + param_name
            self._user_command.set(new_command)

            if not class_name or not method_name or not param_name:
                messagebox.showinfo("Error","All fields are required.")
                return

            found_class = False
            for class_box in self._class_boxes:
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

            new_command = "delete param " + class_name + " " + method_name + " " + param_name
            self._user_command.set(new_command)

            found_class = False
            for class_box in self._class_boxes:
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
        # This is all yellow because these paramaters don't exist anymore
            # I'm leaving the function here as a stump/reminder for what we need to do
                # Just meaning to do rename_param, not that this code is necessary
        dialog_result = Rename_Parameter_Dialog(self, title="Rename Parameter").result
        if dialog_result:
            class_name, method_name, old_name, new_name = dialog_result

            new_command = "rename param " + class_name + " " + method_name + " " + old_name + " " + new_name
            self._user_command.set(new_command)
            self.controller.rename_param(class_name, method_name , old_param_name, new_param_name)

            for class_box in self._class_boxes:
                if class_box['class_name'] == class_name:
                    for method in class_box.get('methods', []):
                        if method['name'] == method_name and old_param_name in method.get('parameters', []):
                            index = method['parameters'].index(old_param_name)
                            method['parameters'][index] = new_param_name
                            self.redraw_canvas()
                            messagebox.showinfo("Success", "Parameter renamed successfully.")
                            return
            messagebox.showinfo("Error", "Parameter not found.")

    def add_relation(self):
        # TODO: This will break once our back end is in
        # Create list of classes in Diagram
        class_options = []
        for cb in self._class_boxes:
            class_options.append(cb._name)

        dialog = Add_Relation_Dialog(self, class_options, "Add Relationship")
        if dialog.result:

            src, dest, rel = dialog.result

            new_command = "add relation " + src + " " + dest + " " + rel
            self._user_command.set(new_command)

            # Add the relationship
            self.relationshipsList.append({
                "source": src,
                "destination": dest,
                "type": rel
            })
            self.update_relationship_tracker()

            self.redraw_canvas()

    def delete_relation(self):
        dialog = Delete_Relation_Dialog(self, "Delete Relationship", self.relationshipsList)
        if dialog.result:
            selected_rel = dialog.result
            # Extract the source and destination class names from the dialog's result
            src = selected_rel['source']
            dest = selected_rel['destination']

            new_command = "delete relationship " + src + " " + dest
            self._user_command.set(new_command)

            # If successful, update the relationships list and UI accordingly
            self.relationshipsList[:] = [rel for rel in self.relationshipsList if not (rel['source'] == src and rel['destination'] == dest)]
            self.update_relationship_tracker()
            self.redraw_canvas()
            messagebox.showinfo("Success", "Relationship deleted successfully.")

#===================================== Helper Functions =====================================#
            
    def get_next_position(self):
        # TODO: This should probably be more involved as the cards won't just appear in a row
            # Probably not high priority
        # For simplicity, let's just arrange them in a horizontal line for now
        spacing = 10  # Spacing between class boxes
        box_width = 150  # Assume a fixed width for now
        x, y = 50, 50  # Starting position for the first class box

        if self._class_boxes:
            # Get the position of the last class box
            index = len(self._class_boxes) - 1
            last_box = self._class_boxes[index]
            x, y = last_box._x, last_box._y

            # Move to the next position to the right
            x += box_width + spacing

        return x, y

    def redraw_canvas(self):
        self.diagram_canvas.delete("all")  # Clears the canvas
        # Draw relationships
        for relationship in self.relationshipsList:
            source = next((box for box in self._class_boxes if box['class_name'] == relationship["source"]), None)
            destination = next((box for box in self._class_boxes if box['class_name'] == relationship["destination"]), None)

            if source and destination:
                # Calculate center points of source and destination boxes
                source_center = (source['x'] + 75, source['y'] + (20 * (2 + len(source.get('fields', [])) + len(source.get('methods', []))) / 2))
                destination_center = (destination['x'] + 75, destination['y'] + (20 * (2 + len(destination.get('fields', [])) + len(destination.get('methods', []))) / 2))

                # Draw a line between them
                self.diagram_canvas.create_line(source_center, destination_center, arrow=tk.LAST)

        # Re-draw each class box
        # for class_box in self.class_boxes:
        #     self.create_class_box(self.diagram_canvas, class_box['class_name'], class_box.get('fields', []), class_box.get('methods', []), class_box['x'], class_box['y'])
        
#===================================== Dialog Classes =====================================#

class Delete_Class_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title:str = None):
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Class:").grid(row = 0)
        self._class_delete = tk.StringVar(master)
        tk.OptionMenu(master, self._class_delete, *self._class_options).grid(row = 0, column = 1)

        # return self._class_delete
        return master

    def apply(self):
        class_name = self._class_delete.get()
        self.result = class_name

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

class Add_Field_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title = None):
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Class:").grid(row=0)
        self._class = tk.StringVar(master)
        tk.OptionMenu(master, self._class, *self._class_options).grid(row = 0, column = 1)

        tk.Label(master, text="Field Name:").grid(row=1)
        self._field_name_entry = tk.Entry(master)
        self._field_name_entry.grid(row = 1, column = 1)

        tk.Label(master, text="Field Type:").grid(row=2)
        self._field_type_entry = tk.Entry(master)
        self._field_type_entry.grid(row = 2, column = 1)

        # return self._class, self._field_entry # initial focus
        return master # initial focus

    def apply(self):
        class_name = self._class.get()
        field_name = self._field_name_entry.get()
        field_type = self._field_type_entry.get()
        self.result = class_name, field_name, field_type

class Delete_Field_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title:str = None):
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace("w",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        # TODO: Get Fields from entered class.
        self._fields = []
        tk.Label(master, text = "Field Name:").grid(row = 1)
        self._delete_field = tk.StringVar(master)
        self._field_options = tk.OptionMenu(master, self._delete_field, self._fields)
        self._field_options.grid(row = 1, column = 1)

        # return self._class, self._delete_field
        return master

    def update_options(self, *args):
        self._delete_field.set('')
        class_name = self._class.get()
        # TODO: This needs to be poplulated with the fields from the class.
        new_opts = [f'{class_name}1', f'{class_name}2', f'{class_name}3']
        
        menu = self._field_options['menu']
        menu.delete(0,'end')

        for o in new_opts:
            self._field_options['menu'].add_command(label = o, command = tk._setit(self._delete_field,o))

    def apply(self):
        class_name = self._class.get()
        field_name = self._delete_field.get()
        self.result = class_name, field_name

class Add_Method_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options = None, title=None):
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Class:").grid(row=0)
        self._class = tk.StringVar(master)
        tk.OptionMenu(master, self._class, *self._class_options).grid(row = 0, column = 1)

        tk.Label(master, text="Method Name:").grid(row=1)
        self._method_entry = tk.Entry(master)
        self._method_entry.grid(row = 1, column = 1)

        # return self._class, self._method_entry # initial focus
        return master # initial focus

    def apply(self):
        class_name = self._class.get()
        method_name = self._method_entry.get()
        self.result = class_name, method_name

class Delete_Method_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title:str = None):
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace("w",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        # TODO: Get Methods from entered class.
        self._methods = []
        tk.Label(master, text = "Method Name:").grid(row = 1)
        self._delete_method = tk.StringVar(master)
        self._method_options = tk.OptionMenu(master, self._delete_method, self._methods)
        self._method_options.grid(row = 1, column = 1)

        return self._class, self._delete_method

    def update_options(self, *args):
        self._delete_method.set('')
        class_name = self._class.get()
        # TODO: This needs to be poplulated with the methods from the class.
        new_opts = [f'{class_name}1', f'{class_name}2', f'{class_name}3']
        
        menu = self._field_options['menu']
        menu.delete(0,'end')

        for o in new_opts:
            self._field_options['menu'].add_command(label = o, command = tk._setit(self._delete_field,o))

    def apply(self):
        class_name = self._class.get()
        field_name = self._delete_field.get()
        self.result = class_name, field_name

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

class Add_Relation_Dialog(simpledialog.Dialog):
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

    def __init__(self, parent, relations:list, title:str = None):
        self._relations = relations
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Relationship:").grid(row = 0)
        self._relation_delete = tk.StringVar(master)
        tk.OptionMenu(master, self._relation_delete, *self._relations).grid(row = 0, column = 1)

        return self._relation_delete

    def apply(self):
        relation = self._relation_delete
        self.result = relation

#===================================== Class Cards =====================================#
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