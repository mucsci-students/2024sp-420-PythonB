from tkinter import ttk
import customtkinter as ctk

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

import math

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
        self._class_boxes: list[Class_Box] = []
        self._sidebar_buttons = []
        self._relation_points = {}
        self._self_relations = []
        self.create_menu()
        self.create_sidebar()
        self.update_button_state()
        self.create_diagram_space()

        self._camera_x = 0
        self._camera_y = 0

        self._mouse_left_button_pressed = False
        self._cursor_x = 0
        self._cursor_y = 0
        self._dragged_class_box = None
        self.diagram_canvas.bind('<Button-1>', self.on_click)
        self.diagram_canvas.bind("<ButtonRelease-1>", self.on_release)
        self.diagram_canvas.bind('<B1-Motion>', self.on_move)

        self._user_command = tk.StringVar()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def error_message(self, message: str) -> None:
        messagebox.showinfo("Error - CWorld UML", message, parent=self)

    def on_close(self) -> None:
        self._user_command.set('quit')
        self.clear()

    def on_click(self, event: tk.Event) -> None:
        self._cursor_x = event.x
        self._cursor_y = event.y
        for cb in self._class_boxes:
            if cb._x <= self._cursor_x <= cb._x + cb._width and cb._y <= self._cursor_y <= cb._y + cb._height:
                self._dragged_class_box = cb
                break

    def on_release(self, event: tk.Event) -> None:
        self._dragged_class_box = None

    def on_move(self, event: tk.Event) -> None:
        delta_x = event.x - self._cursor_x
        delta_y = event.y - self._cursor_y
        self._cursor_x = event.x
        self._cursor_y = event.y
        if self._dragged_class_box:
            x = 'x' + str(delta_x).replace('-', '_')
            y = 'y' + str(delta_y).replace('-', '_')
            self._user_command.set(' '.join(['move', self._dragged_class_box._name, x, y]))
        else:
            self._camera_x -= delta_x
            self._camera_y -= delta_y
            self._user_command.set('redraw')
            
    def center(self) -> None:
        self._camera_x = 0
        self._camera_y = 0
        self._user_command.set('redraw')

    def draw_class(self, name, x=None, y=None, methods=[], fields=[], width=0) -> None:
        if x is None or y is None:
            x, y = self.get_next_position()
        self._class_boxes.append(Class_Box(self.diagram_canvas, name, x - self._camera_x, y - self._camera_y, methods, fields, width))

    def draw_relations(self, relations: list[list[str]]) -> None:
        for src, dst, type in relations:
            self._self_relations.append([src, dst, type])

            if src in self._relation_points:
                src_points = self._relation_points[src]
            else:
                src_class = next(x for x in self._class_boxes if x._name == src)
                src_points = []; self._relation_points[src] = src_points
                src_points.append([src_class._x + src_class._width / 2, src_class._y]                        ) # top
                src_points.append([src_class._x + src_class._width / 2, src_class._y + src_class._height]    ) # bot
                src_points.append([src_class._x,                        src_class._y + src_class._height / 2]) # left
                src_points.append([src_class._x + src_class._width,     src_class._y + src_class._height / 2]) # right
            if dst in self._relation_points:
                dst_points = self._relation_points[dst]
            else:
                dst_class = next(x for x in self._class_boxes if x._name == dst)
                dst_points = []; self._relation_points[dst] = dst_points
                dst_points.append([dst_class._x + dst_class._width / 2, dst_class._y]                        ) # top
                dst_points.append([dst_class._x + dst_class._width / 2, dst_class._y + dst_class._height]    ) # bot
                dst_points.append([dst_class._x,                        dst_class._y + dst_class._height / 2]) # left
                dst_points.append([dst_class._x + dst_class._width,     dst_class._y + dst_class._height / 2]) # right
            self.draw_relation(src_points, dst_points, type)

    def draw_relation(self, src: list[list[int]], dst: list[list[int]], type: str) -> None:
        a, b = -1, -1
        dist = float('inf')
        for i in range(len(src)):
            for j in range(len(dst)):
                d = math.dist(src[i], dst[j])
                if d < dist:
                    dist = d
                    a, b = i, j
        start = src[a]
        end = dst[b]
        if type == 'Aggregation':
            self.draw_aggregation(start, end)
        elif type == 'Composition':
            self.draw_composition(start, end)
        elif type == 'Inheritance':
            self.draw_inheritance(start, end)
        elif type == 'Realization':
            self.draw_realization(start, end)

    def clear(self) -> None:
        self.diagram_canvas.delete("all")
        self._class_boxes.clear()
        self._relation_points.clear()
        self._self_relations.clear()

    def listen(self) -> str:
        """
        Wait for user action and return as a command
        """
        self.update_button_state()

        self.wait_variable(self._user_command)
        cmd = self._user_command.get()
        self._user_command.set('')
        return cmd
    
    def get_all_positions(self):
        return [[cb._name, cb._last_x, cb._last_y] for cb in self._class_boxes]

    def create_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        # File Menu
        file_menu = Menu(menu_bar, tearoff=0)
        # file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Load", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_close)
        menu_bar.add_cascade(label="File", menu=file_menu)

        #Edit Menu (Undo/Redo)
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        #Layout Menu (Return to Center)
        layout_menu = Menu(menu_bar, tearoff=0)
        layout_menu.add_command(label="Return to Center", command=self.center)
        menu_bar.add_cascade(label="Layout", menu=layout_menu)

        # Help Menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="View Help", command=self.show_help_messagebox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        #menu_bar.add_separator()
        #menu_bar.add_separator()

        #menu_bar.add_command(label = "Undo", command = self.undo)
        #menu_bar.add_command(label = "Redo", command = self.redo)

    def undo(self):
        self._user_command.set('undo')

    def redo(self):
        self._user_command.set('redo')

    # TODO: Reformat this now that the relation tracker isn't there.
        # I'll do this later in the sprint when I have time
    def create_sidebar(self):
        self._sidebar = tk.Frame(self, width = 200, bg = 'lightgray')
        self._sidebar.pack(side = LEFT, fill = tk.Y, padx = (5, 0), pady = (13, 12))

        self._btn_class = ctk.CTkButton(self._sidebar, text="Classes", command=self.class_options_menu)
        self._btn_class.pack(fill=tk.X, padx=(5, 5), pady=(10, 5))

        self._btn_fields = ctk.CTkButton(self._sidebar, text="Fields", command=self.fields_options_menu)
        self._btn_fields.pack(fill=tk.X, padx=(5, 5), pady=(5, 5))

        self._btn_methods = ctk.CTkButton(self._sidebar, text="Methods", command=self.methods_options_menu)
        self._btn_methods.pack(fill=tk.X, padx=(5, 5), pady=(5, 5))

        self._btn_params = ctk.CTkButton(self._sidebar, text="Parameters", command=self.params_options_menu)
        self._btn_params.pack(fill=tk.X, padx=(5, 5), pady=(5, 5))

        self._btn_relations = ctk.CTkButton(self._sidebar, text="Relationships", command=self.relations_options_menu)
        self._btn_relations.pack(fill=tk.X, padx=(5, 5), pady=(5, 5))

    def update_button_state(self):
        self._btn_class.configure(state = "disabled")
        self._btn_fields.configure(state = "disabled")
        self._btn_methods.configure(state = "disabled")
        self._btn_params.configure(state = "disabled")
        self._btn_relations.configure(state = "disabled")

        self._btn_class.configure(state = "active")
        class_count = len(self._class_boxes)
        if class_count > 0:
            self._btn_fields.configure(state = "active")
            self._btn_methods.configure(state = "active")
            self._btn_relations.configure(state = "active")
            method_count = sum(len(cb._methods) for cb in self._class_boxes)
            if method_count > 0:
                self._btn_params.configure(state = "active")

    def create_diagram_space(self):
        self.diagram_canvas = tk.Canvas(self, bg = 'white')
        self.diagram_canvas.pack(side = tk.LEFT, padx = 10, pady = 10, fill = tk.BOTH, expand = True)

#===================================== Menu Methods =====================================#

    def new_file(self):
        # TODO: This either needs removed or needs to ask if you want to save, then restart the program
            # new Diagram and everything
            # If removed, this needs to be removed from the file menu
        # Placeholder for new file action
        messagebox.showinfo("Action", "Create a new file")

    # TODO: self.controller
    def open_file(self):
        file_name = filedialog.askopenfilename(initialdir='saves/', defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not file_name:
            return
        new_command = 'load ' + file_name[file_name.rfind('/') + 1:].removesuffix('.json')
        self._user_command.set(new_command)


    def save_file(self):
        # Open a dialog asking for the filename to save to
        file_name = filedialog.asksaveasfilename(initialfile='untitled.json', initialdir='saves/', defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not file_name:
            return
        new_command = 'save ' + file_name[file_name.rfind('/') + 1:].removesuffix('.json')
        self._user_command.set(new_command)
    
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

            Undo/Redo:
                - Use the Edit menu to undo or redo your last action.

            This quick guide helps you understand the basics of interacting with the UML editor.
                """
        messagebox.showinfo("Help - CWorld UML Program", help_content, parent=self)

#===================================== Create Menus =====================================#

    def class_options_menu(self):
        # Create a menu that will appear at the current mouse position
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label = "Add Class", command = self.add_class)
        
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
            menu.add_command(label = "Rename Method", command = self.rename_method)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

    def params_options_menu(self):
        menu = Menu(self, tearoff = 0)
        if len(self._class_boxes) > 0:
            # TODO: See methods_options_menu above
            menu.add_command(label = "Add Parameter", command = self.add_param)
            menu.add_command(label = "Delete Parameter", command = self.delete_param)
            menu.add_command(label = "Rename Parameter", command = self.rename_param)
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
            menu.add_command(label = "Delete Relationship", command = self.delete_relation)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

#===================================== Diagram Functions =====================================#

    def add_class(self) -> str:
        class_name = simpledialog.askstring("Input", "Enter Class Name:", parent = self)
        if not class_name:
            return
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
        class_options = [cb._name for cb in self._class_boxes]

        dialog = Rename_Class_Dialog(self, class_options, "Rename Class")
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
        # class_name = simpledialog.askstring("Rename Field", "Enter the name of the class:", parent=self)
        # if not class_name:
        #     return
        # old_name = simpledialog.askstring("Rename Field", "Enter the name of the field to rename:", parent=self)
        # if not old_name:
        #     return
        # new_name = simpledialog.askstring("Rename Field", "Enter the new name for the field:", parent=self)
        # if not new_name:
        #     return

        class_options = [cb._name for cb in self._class_boxes]

        dialog_result = Rename_Field_Dialog(self, class_options, title = "Rename Field").result
        if dialog_result:
            class_name, old_name, new_name = dialog_result

            new_command = "rename field " + class_name + " " + old_name + " " + new_name
            self._user_command.set(new_command)

        # messagebox.showinfo("Success", f"Field '{old_name}' renamed to '{new_name}' in class '{class_name}'.")
        # messagebox.showinfo("Error", "Attribute not found.")

    def add_method(self):
        class_options = [cb._name for cb in self._class_boxes]

        dialog = Add_Method_Dialog(self, class_options, "Add Method")
        if dialog.result:
            class_name, method_name, return_type = dialog.result
            new_command = "add method " + class_name + " " + method_name + " " + return_type
            self._user_command.set(new_command)

    def delete_method(self):
        class_options = [cb._name for cb in self._class_boxes]

        dialog_result = Delete_Method_Dialog(self, class_options, title = "Delete Method").result
        if dialog_result:
            class_name, method_name = dialog_result
            
            new_command = "delete method " + class_name + " " + method_name
            self._user_command.set(new_command)

    def rename_method(self):
        # class_name = simpledialog.askstring("Rename Method", "Enter the name of the class:", parent=self)
        # if not class_name:
        #     return
        # old_name = simpledialog.askstring("Rename Method", "Enter the name of the method to rename:", parent=self)
        # if not old_name:
        #     return
        # new_name = simpledialog.askstring("Rename Method", "Enter the new name for the method:", parent=self)
        # if not new_name:
        #     return

        class_options = [cb._name for cb in self._class_boxes]

        dialog_result = Rename_Method_Dialog(self, class_options, title = "Rename Method").result
        if dialog_result:
            class_name, old_name, new_name = dialog_result
        
            new_command = "rename method " + class_name + " " + old_name + " " + new_name
            self._user_command.set(new_command)

    def add_param(self):
        class_options = [cb._name for cb in self._class_boxes]

        dialog_result = Add_Parameter_Dialog(self, class_options, title="Add Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result

            new_command = "add param " + class_name + " " + method_name + " " + param_name
            self._user_command.set(new_command)

            # messagebox.showinfo("Error","All fields are required.")
            # messagebox.showinfo("Add Parameter", f"Method '{method_name}' not found.")
            # messagebox.showinfo("Add Parameter", f"Class '{class_name}' not found.")
            # messagebox.showinfo("Success", f"Parameter '{param_name}' added to '{class_name}")

    def delete_param(self):
        class_options = [cb._name for cb in self._class_boxes]

        dialog_result = Delete_Parameter_Dialog(self, class_options, "Delete Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result

            new_command = "delete param " + class_name + " " + method_name + " " + param_name
            self._user_command.set(new_command)

            # messagebox.showinfo("Success", f"Parameter '{param_name}' removed from method '{method_name}' in class '{class_name}'.")
            # messagebox.showinfo("Error", f"Parameter '{param_name}' not found in method '{method_name}'.")
            # messagebox.showinfo("Error", f"Method '{method_name}' not found in class '{class_name}'.")
            # messagebox.showinfo("Error", f"Class '{class_name}' not found.")

    def rename_param(self):
        class_options = [cb._name for cb in self._class_boxes]

        dialog_result = Rename_Parameter_Dialog(self, class_options, title="Rename Parameter").result
        if dialog_result:
            class_name, method_name, old_name, new_name = dialog_result

            new_command = "rename param " + class_name + " " + method_name + " " + old_name + " " + new_name
            self._user_command.set(new_command)

            # messagebox.showinfo("Success", "Parameter renamed successfully.")
            # messagebox.showinfo("Error", "Parameter not found.")

    def vec(self, p1: list[int], p2: list[int]):
        return p2[0] - p1[0], p2[1] - p1[1]
    
    def rotate(self, v: tuple[int], rad: float):
        return v[0] * math.cos(rad) - v[1] * math.sin(rad), v[0] * math.sin(rad) + v[1] * math.cos(rad)
    
    def normalized(self, v: tuple[int]):
        ac = 1e-11 + (v[0]**2 + v[1]**2)**0.5
        return v[0] / ac, v[1] / ac

    def draw_diamond(self, start: list[int], end: list[int], color: str, side_length: int=30) -> None:
        orgin = self.vec(start, end)
        left = self.normalized(self.rotate(orgin, -5 * math.pi / 6))
        right = self.normalized(self.rotate(orgin, 5 * math.pi / 6))
        p1 = end[0] + left[0] * side_length, end[1] + left[1] * side_length
        p2 = end[0] + right[0] * side_length, end[1] + right[1] * side_length
        v = self.normalized(self.vec(end, start))
        to = end[0] + v[0] * side_length * 3**0.5, end[1] + v[1] * side_length * 3**0.5
        self.diagram_canvas.create_polygon(*end, *p1, *to, *p2, outline="black", fill=color)

    def draw_triangle(self, start: list[int], end: list[int], color: str, side_length: int=40) -> None:

        orgin = self.vec(start, end)
        left = self.normalized(self.rotate(orgin, -5 * math.pi / 6))
        right = self.normalized(self.rotate(orgin, 5 * math.pi / 6))
        p1 = end[0] + left[0] * side_length, end[1] + left[1] * side_length
        p2 = end[0] + right[0] * side_length, end[1] + right[1] * side_length
        self.diagram_canvas.create_polygon(*end, *p1, *p2, outline="black", fill=color)

    def draw_aggregation(self, start: list[int], end: list[int]) -> None:
        # line with white diamond
        self.diagram_canvas.create_line(start[0], start[1], end[0], end[1], width=5)
        self.draw_diamond(start, end, 'white')

    def draw_composition(self, start: list[int], end: list[int]) -> None:
        # line with solid diamond
        self.diagram_canvas.create_line(start[0], start[1], end[0], end[1], width=5)
        self.draw_diamond(start, end, 'black')

    def draw_inheritance(self, start: list[int], end: list[int]) -> None:
        # line with white triangle
        self.diagram_canvas.create_line(start[0], start[1], end[0], end[1], width=5)
        self.draw_triangle(start, end, 'white')

    def draw_realization(self, start: list[int], end: list[int]) -> None:
        # dash line with white triangle
        self.diagram_canvas.create_line(start[0], start[1], end[0], end[1], width=5, dash=(4, 4))
        self.draw_triangle(start, end, 'white')

    def add_relation(self):
        # TODO: This will break once our back end is in
        # Create list of classes in Diagram
        class_options = [cb._name for cb in self._class_boxes]

        dialog = Add_Relation_Dialog(self, class_options, "Add Relationship")
        if dialog.result:
            src, dest, rel = dialog.result

            new_command = "add relation " + src + " " + dest + " " + rel
            self._user_command.set(new_command)

    def delete_relation(self):
        class_options = [cb._name for cb in self._class_boxes]

        dialog = Delete_Relation_Dialog(self, class_options, "Delete Relationship")
        if dialog.result:
            src, dst = dialog.result
            new_command = "delete relation " + src + " " + dst
            self._user_command.set(new_command)

            # messagebox.showinfo("Success", "Relationship deleted successfully.")

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
    def __init__(self, parent, class_options:list = None, title=None):
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Old Class Name:").grid(row = 0)
        self.class_name_entry = tk.StringVar(master)
        tk.OptionMenu(master, self.class_name_entry, *self._class_options).grid(row = 0, column = 1)

        tk.Label(master, text="New Class Name:").grid(row=1)
        self.new_name_entry = tk.Entry(master)
        self.new_name_entry.grid(row=1, column=1)

        # return self.class_name_entry  # Set focus on the first entry widget
        return master

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
        self.parent = parent
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace_add("write",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        tk.Label(master, text = "Field Name:").grid(row = 1)
        self._delete_field = tk.StringVar(master)
        self._field_options = tk.OptionMenu(master, self._delete_field, ())
        self._field_options.grid(row = 1, column = 1)

        # return self._class, self._delete_field
        return master

    def update_options(self, *args):
        self._delete_field.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb._name == class_name:
                options = [x for _, x in cb._fields]
                break
        
        menu = self._field_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._field_options['menu'].add_command(label = o, command = tk._setit(self._delete_field,o))

    def apply(self):
        class_name = self._class.get()
        field_name = self._delete_field.get()
        self.result = class_name, field_name

class Rename_Field_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title:str = None):
        self.parent = parent
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace_add("write",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        tk.Label(master, text = "Field Name:").grid(row = 1)
        self._delete_field = tk.StringVar(master)
        self._field_options = tk.OptionMenu(master, self._delete_field, ())
        self._field_options.grid(row = 1, column = 1)

        tk.Label(master, text="New Field Name:").grid(row = 2)
        self._new_field = tk.Entry(master)
        self._new_field.grid(row = 2, column = 1)

        # return self._class, self._delete_field
        return master

    def update_options(self, *args):
        self._delete_field.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb._name == class_name:
                options = [x for _, x in cb._fields]
                break
        
        menu = self._field_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._field_options['menu'].add_command(label = o, command = tk._setit(self._delete_field,o))

    def apply(self):
        class_name = self._class.get()
        field_name = self._delete_field.get()
        new_field = self._new_field.get()
        self.result = class_name, field_name, new_field

class Add_Method_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options = None, title=None):
        self._class_options = class_options
        super().__init__(parent, title = title)

    def body(self, master):
        tk.Label(master, text = "Class:").grid(row=0)
        self._class = tk.StringVar(master)
        tk.OptionMenu(master, self._class, *self._class_options).grid(row = 0, column = 1)

        tk.Label(master, text = "Method Name:").grid(row = 1)
        self._method_name_entry = tk.Entry(master)
        self._method_name_entry.grid(row = 1, column = 1)


        tk.Label(master, text="Return Type:").grid(row=2)

        self._return_type_entry = tk.Entry(master)
        self._return_type_entry.grid(row = 2, column = 1)

        # return self._class, self._method_entry # initial focus
        return master # initial focus

    def apply(self):
        class_name = self._class.get()
        method_name = self._method_name_entry.get()
        return_type = self._return_type_entry.get()
        self.result = class_name, method_name, return_type

class Delete_Method_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title:str = None):
        self.parent = parent
        self._class_options = class_options
        super().__init__(parent, title = title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace_add("write",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        tk.Label(master, text = "Method Name:").grid(row = 1)
        self._delete_method = tk.StringVar(master)
        self._method_options = tk.OptionMenu(master, self._delete_method, ())
        self._method_options.grid(row = 1, column = 1)

        # return self._class, self._delete_method
        return master

    def update_options(self, *args):
        self._delete_method.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb._name == class_name:
                options = [lst[0][1] for lst in cb._methods]
                break
        
        menu = self._method_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._method_options['menu'].add_command(label = o, command = tk._setit(self._delete_method,o))

    def apply(self):
        class_name = self._class.get()
        method_name = self._delete_method.get()
        self.result = class_name, method_name

class Rename_Method_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title:str = None):
        self.parent = parent
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace_add("write",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        tk.Label(master, text = "Method Name:").grid(row = 1)
        self._delete_method = tk.StringVar(master)
        self._method_options = tk.OptionMenu(master, self._delete_method, ())
        self._method_options.grid(row = 1, column = 1)

        tk.Label(master, text="New Method Name:").grid(row = 2)
        self._new_method = tk.Entry(master)
        self._new_method.grid(row = 2, column = 1)

        # return self._class, self._delete_method
        return master

    def update_options(self, *args):
        self._delete_method.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb._name == class_name:
                options = [lst[0][1] for lst in cb._methods]
                break
        
        menu = self._method_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._method_options['menu'].add_command(label = o, command = tk._setit(self._delete_method,o))

    def apply(self):
        class_name = self._class.get()
        method_name = self._delete_method.get()
        new_method = self._new_method.get()
        self.result = class_name, method_name, new_method

class Add_Parameter_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options:list = None, title=None):
        self.parent = parent
        self._class_options = class_options
        super().__init__(parent, title)

    def body(self, master):

        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace_add("write",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        tk.Label(master, text = "Method Name:").grid(row = 1)
        self._method_select = tk.StringVar(master)
        self._method_options = tk.OptionMenu(master, self._method_select, ())
        self._method_options.grid(row = 1, column = 1)


        tk.Label(master, text = "Parameter Name:").grid(row = 2)
        self.param_name_entry = tk.Entry(master)
        self.param_name_entry.grid(row = 2, column = 1)

        # return self.class_name_entry  # initial focus
        return master

    def update_options(self, *args):
        self._method_select.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb._name == class_name:
                options = [lst[0][1] for lst in cb._methods]
                break
        
        menu = self._method_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._method_options['menu'].add_command(label = o, command = tk._setit(self._method_select,o))

    def apply(self):
        class_name = self._class.get()
        method_name = self._method_select.get()
        param_name = self.param_name_entry.get()
        self.result = class_name, method_name, param_name

class Delete_Parameter_Dialog(simpledialog.Dialog):

    def __init__(self, parent, class_options:list = None, title=None):
        self.parent = parent
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace_add("write",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        tk.Label(master, text = "Method Name:").grid(row = 1)
        self._method_select = tk.StringVar(master)
        self._method_select.trace_add("write",self.update_options2)
        self._method_options = tk.OptionMenu(master, self._method_select, ())
        self._method_options.grid(row = 1, column = 1)

        tk.Label(master, text = "Parameter Name:").grid(row = 2)
        self._param_select = tk.StringVar(master)
        self._param_options = tk.OptionMenu(master, self._param_select, ())
        self._param_options.grid(row = 2, column = 1)


        # return self.class_name_entry  # Set focus on the first entry widget
        return master

    def update_options(self, *args):
        self._method_select.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb._name == class_name:
                options = [lst[0][1] for lst in cb._methods]
                break
        
        menu = self._method_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._method_options['menu'].add_command(label = o, command = tk._setit(self._method_select,o))

    def update_options2(self, *args):
        self._param_select.set('')
        class_name = self._class.get()
        if not self._method_select.get():
            options = []
        else:
            for cb in self.parent._class_boxes:
                if cb._name == class_name:
                    options = next(lst[1:] for lst in cb._methods if lst[0][1] == self._method_select.get())
                    options = [x[0] for x in options]
                    break
        
        menu = self._param_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._param_options['menu'].add_command(label = o, command = tk._setit(self._param_select,o))

    def apply(self):
        class_name = self._class.get()
        method_name = self._method_select.get()
        param_name = self._param_select.get()
        self.result = class_name, method_name, param_name

class Rename_Parameter_Dialog(simpledialog.Dialog):

    def __init__(self, parent, class_options:list = None, title=None):
        self.parent = parent
        self._class_options = class_options
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text = "Select Class:").grid(row = 0)
        self._class = tk.StringVar(master)
        self._class.trace_add("write",self.update_options)
        self._class_select = tk.OptionMenu(master, self._class, *self._class_options)
        self._class_select.grid(row = 0, column = 1)

        tk.Label(master, text = "Method Name:").grid(row = 1)
        self._method_select = tk.StringVar(master)
        self._method_select.trace_add("write",self.update_options2)
        self._method_options = tk.OptionMenu(master, self._method_select, ())
        self._method_options.grid(row = 1, column = 1)

        tk.Label(master, text = "Parameter Name:").grid(row = 2)
        self._param_select = tk.StringVar(master)
        self._param_options = tk.OptionMenu(master, self._param_select, ())
        self._param_options.grid(row = 2, column = 1)

        tk.Label(master, text="New Parameter Name:").grid(row=3)
        self._new_param_name = tk.Entry(master)
        self._new_param_name.grid(row=3, column=1)

        return master

    def update_options(self, *args):
        self._method_select.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb._name == class_name:
                options = [lst[0][1] for lst in cb._methods]
                break
        
        menu = self._method_options['menu']
        menu.delete(0,'end')


        for o in options:
            self._method_options['menu'].add_command(label = o, command = tk._setit(self._method_select,o))

    def update_options2(self, *args):
        self._param_select.set('')
        class_name = self._class.get()
        if not self._method_select.get():
            options = []
        else:
            for cb in self.parent._class_boxes:
                if cb._name == class_name:
                    options = next(lst[1:] for lst in cb._methods if lst[0][1] == self._method_select.get())
                    options = [x[0] for x in options]
                    break
        
        menu = self._param_options['menu']
        menu.delete(0,'end')

        for o in options:
            self._param_options['menu'].add_command(label = o, command = tk._setit(self._param_select,o))

    def apply(self):
        class_name = self._class.get()
        method_name = self._method_select.get()
        param_name = self._param_select.get()
        new_name = self._new_param_name.get()
        self.result = class_name, method_name, param_name, new_name

class Add_Relation_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options = None, title = None):
        self._class_options = class_options
        super().__init__(parent, title = title)

    def body(self, master):
        tk.Label(master, text="Source Class:").grid(row = 0)
        self._src = tk.StringVar(master)
        tk.OptionMenu(master, self._src, *self._class_options).grid(row = 0, column = 1)

        tk.Label(master, text="Destination Class:").grid(row = 1)
        self._dest = tk.StringVar(master)
        tk.OptionMenu(master, self._dest, *self._class_options).grid(row = 1, column = 1)

        tk.Label(master, text="Relationship Type:").grid(row = 2)
        self._rel_type = tk.StringVar(master)
        rel_options = ["Aggregation", "Composition", "Inheritance", "Realization"]
        tk.OptionMenu(master, self._rel_type, *rel_options).grid(row = 2, column = 1)

        # return self._src # initial focus
        return master

    def apply(self):
        src = self._src.get()
        dest = self._dest.get()
        rel_type = self._rel_type.get()
        self.result = (src, dest, rel_type)

class Delete_Relation_Dialog(simpledialog.Dialog):
    def __init__(self, parent, class_options = None, title = None):
        self._class_options = class_options
        super().__init__(parent, title = title)

    def body(self, master):
        tk.Label(master, text="Source Class:").grid(row = 0)
        self._src = tk.StringVar(master)
        tk.OptionMenu(master, self._src, *self._class_options).grid(row = 0, column = 1)

        tk.Label(master, text="Destination Class:").grid(row = 1)
        self._dest = tk.StringVar(master)
        tk.OptionMenu(master, self._dest, *self._class_options).grid(row = 1, column = 1)

        return master

    def apply(self):
        src = self._src.get()
        dest = self._dest.get()
        self.result = src, dest

#===================================== Class Cards =====================================#
class Class_Box():
    def __init__(self, canvas: tk.Canvas, name:str, x: int, y: int, methods: list[list[list[str]]], fields: list[list[str]], width: int) -> None:
        self._name = name
        self._canvas = canvas
        self._methods = methods
        self._fields = fields
        self._width = 150 + width * 4
        self._text_spacing = 20
        self._indent_spacing = 10
        self._x = x
        self._y = y

        self._line_count = 0
        self._line_count += 1 # class_name
        self._line_count += 1 # separator
        self._line_count += len(self._fields) # fields
        self._line_count += 1 # separator
        self._line_count += len(self._methods) # methods

        self._box, self._box_text, self._height = self.create_class_box(canvas)

    def create_class_box(self, canvas: tk.Canvas):
        # TODO: This value is just hard coded (obviously)
            # It should could the number of lines in the class box
            
        # Calculate the height of the box
        num_text_lines = 2 + 2 + len(self._fields) + len(self._methods) # class_name + fields + methods
        # Calculate box height dynamically based on contents
        box_height = self._text_spacing * num_text_lines

        ################################################# 0
        #                                               # 1
        #                  class_name                   # 2
        #------------------separater--------------------# 3
        #                  fields                       # 4
        #------------------separater--------------------# 5
        #                  methods                      # 6
        #                                               # 7
        ################################################# 8

        box = canvas.create_rectangle(self._x, self._y, self._x + self._width, self._y + box_height, fill = 'lightgray', outline = 'black')
        current_line = 1
        box_text = canvas.create_text(self._x + self._width / 2, self._y + self._text_spacing * current_line,\
                                      text = self._name,\
                                        font = ('TkDefaultFont', 10, 'bold'))
        current_line += 1
        self._separator1 = canvas.create_line([self._x, self._y + self._text_spacing * current_line],\
                                              [self._x + self._width, self._y + self._text_spacing * current_line])
        current_line += 1
        self._moveable_text = []
        for lst in self._fields:
            self._moveable_text.append(canvas.create_text(self._x + self._width / 2, self._y + self._text_spacing * current_line,\
                                                          text = ' '.join(lst),\
                                                            font = ('TkDefaultFont', 10, 'bold')))
            current_line += 1
        self._separator2 = canvas.create_line([self._x, self._y + self._text_spacing * current_line],\
                                              [self._x + self._width, self._y + self._text_spacing * current_line])
        current_line += 1
        for lst in self._methods:
            self._moveable_text.append(canvas.create_text(self._x + self._width / 2, self._y + self._text_spacing * current_line,\
                                                          text=' '.join(lst[0]) + '(' + ', '.join(' '.join(x) for x in lst[1:]) + ')',\
                                                            font=('TkDefaultFont', 10, 'bold')))
            current_line += 1

        return box, box_text, box_height