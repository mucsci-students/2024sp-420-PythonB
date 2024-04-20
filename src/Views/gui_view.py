from tkinter import ttk
import customtkinter as ctk

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from abc import ABC, abstractmethod

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
        self._class_boxes: list[dict] = []
        self._sidebar_buttons = []
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

    def camera_pos(self) -> tuple[int, int]:
        return self._camera_x, self._camera_y
    
    def viewport_size(self) -> tuple[int, int]:
        return 1000, 800

    def error_message(self, message: str) -> None:
        messagebox.showinfo("Error - CWorld UML", message, parent=self)

    def on_close(self) -> None:
        self._user_command.set('quit')
        self.clear()

    def on_click(self, event: tk.Event) -> None:
        self._cursor_x = event.x
        self._cursor_y = event.y
        for cb in self._class_boxes:
            if cb['x'] <= self._cursor_x + self._camera_x <= cb['x'] + cb['width'] and cb['y'] <= self._cursor_y + self._camera_y <= cb['y'] + cb['height']:
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
            self._user_command.set(' '.join(['move', self._dragged_class_box['name'], x, y]))
        else:
            self._camera_x -= delta_x
            self._camera_y -= delta_y
            self._user_command.set('redraw')
            
    def center(self) -> None:
        self._camera_x = 0
        self._camera_y = 0
        self._user_command.set('redraw')

    def last(self) -> None:
        if self._class_boxes:
            self._camera_x = self._class_boxes[-1]['x'] - 100
            self._camera_y = self._class_boxes[-1]['y'] - 100
        self._user_command.set('redraw')

    def draw(self, photo, class_boxes):
        self._image = photo
        self.diagram_canvas.create_image(0, 0, anchor=tk.NW, image=self._image)
        self._class_boxes = class_boxes

    def clear(self) -> None:
        self.diagram_canvas.delete("all")
        self._class_boxes.clear()

    def listen(self) -> str:
        """
        Wait for user action and return as a command
        """
        self.update_button_state()
        self.wait_variable(self._user_command)
        cmd = self._user_command.get()
        self._user_command.set('')
        return cmd
    
    def create_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        # File Menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Load", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Export", command=self.export_image)
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
        layout_menu.add_command(label="Move Camera to Center", command=self.center)
        layout_menu.add_command(label="Move Camera to Last Class", command=self.last)
        menu_bar.add_cascade(label="View", menu=layout_menu)
        # Help Menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="View Help", command=self.show_help_messagebox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

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
            method_count = sum(len(cb['methods']) for cb in self._class_boxes)
            if method_count > 0:
                self._btn_params.configure(state = "active")

    def create_diagram_space(self):
        self.diagram_canvas = tk.Canvas(self, bg = '#{:02x}{:02x}{:02x}'.format(100, 100, 100))
        self.diagram_canvas.pack(side = tk.LEFT, padx = 10, pady = 10, fill = tk.BOTH, expand = True)

#===================================== Menu Methods =====================================#

    def open_file(self):
        file_name = filedialog.askopenfilename(initialdir='saves/', defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not file_name:
            return
        new_command = 'load ' + file_name[file_name.rfind('/') + 1:].removesuffix('.json')
        self._user_command.set(new_command)


    def save_file(self):
        file_name = filedialog.asksaveasfilename(initialfile='untitled.json', initialdir='saves/', defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not file_name:
            return
        new_command = 'save ' + file_name[file_name.rfind('/') + 1:].removesuffix('.json')
        self._user_command.set(new_command)

    def export_image(self):
        file_name = filedialog.asksaveasfilename(initialfile='untitled.png', initialdir='images/', defaultextension=".png",
                                                filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if not file_name:
            return
        new_command = 'export ' + file_name[file_name.rfind('/') + 1:].removesuffix('.png')
        self._user_command.set(new_command)
    
    def show_help_messagebox(self):
        help_content = """
            Valid Input:
                - Names must start with a letter
                - Can include numbers, dashes (-), and underscores (_).

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
            menu.add_command(label = "Add Field", command = self.add_field)
        # Only show the delete and rename options if there are fields to delete or rename
        if any(len(cb['fields']) > 0 for cb in self._class_boxes):
            menu.add_command(label = "Delete Field", command = self.delete_field)
            menu.add_command(label = "Rename Field", command = self.rename_field)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

    def methods_options_menu(self):
        menu = Menu(self, tearoff = 0)
        if len(self._class_boxes) > 0:
            menu.add_command(label = "Add Method", command = self.add_method)
        # Only show the delete and rename options if there are methods to delete or rename
        if any(len(cb['methods']) > 0 for cb in self._class_boxes):
            menu.add_command(label = "Delete Method", command = self.delete_method)
            menu.add_command(label = "Rename Method", command = self.rename_method)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

    def params_options_menu(self):
        menu = Menu(self, tearoff = 0)
        if len(self._class_boxes) > 0:
            menu.add_command(label = "Add Parameter", command = self.add_param)
            menu.add_command(label = "Delete Parameter", command = self.delete_param)
            menu.add_command(label = "Rename Parameter", command = self.rename_param)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

    def relations_options_menu(self):
        menu = Menu(self, tearoff=0)
        if len(self._class_boxes) > 0:
            menu.add_command(label = "Add Relationship", command = self.add_relation)
            menu.add_command(label = "Delete Relationship", command = self.delete_relation)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

#===================================== Diagram Functions =====================================#

    def add_class(self):
        dialog_params = Dialog_Parts("text", "Class Name")
        Dialog_Factory.create("Add Class", dialog_params, lambda result:self._user_command.set(f'add class { result[0] }'))
        
    def delete_class(self) -> str:
        class_options = [cb['name'] for cb in self._class_boxes]
        dialog_params = Dialog_Parts("combo", "Class Name", class_options)
        Dialog_Factory.create("Delete Class", dialog_params, lambda result:self._user_command.set(f'delete class { result[0] }'))
    
    def rename_class(self) -> None:
        class_options = [cb['name'] for cb in self._class_boxes]
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("text", "New Name")
            ]
        Dialog_Factory.create("Rename Class", dialog_params, lambda result:self._user_command.set(f'rename class { result[0] } { result[1] }'))

    def add_field(self) -> None:
        class_options = [cb['name'] for cb in self._class_boxes]
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("text", "Field"),
            Dialog_Parts("text", "Type")
        ]
        Dialog_Factory.create("Add Field", dialog_params, lambda result:self._user_command.set(f'add field { result[0] } { result[1] } { result[2] }'))

    def delete_field(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        field_options = {cb['name']: cb['fields'] for cb in self._class_boxes}
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("dynamic_combo", "Field", field_options, 1)
        ]
        Dialog_Factory.create("Delete Field", dialog_params, lambda result:self._user_command.set(f'delete field { result[0] } { result[1] }'))

    def rename_field(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        field_options = {cb['name']: cb['fields'] for cb in self._class_boxes}
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("dynamic_combo", "Field", field_options, 1),
            Dialog_Parts("text", "New Name")
        ]
        Dialog_Factory.create("Rename Field", dialog_params, lambda result:self._user_command.set(f'rename field { result[0] } { result[1] } { result[2] }'))

    def add_method(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("text", "Method"),
            Dialog_Parts("text", "Return Type")
        ]
        Dialog_Factory.create("Add Method", dialog_params, lambda result:self._user_command.set(f'add method { result[0] } { result[1] } { result[2] }'))

    def delete_method(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        meth_options = {cb['name']: list(cb['methods'].keys()) for cb in self._class_boxes}
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("dynamic_combo", "Method", meth_options, 1)
        ]
        Dialog_Factory.create("Delete Method", dialog_params, lambda result:self._user_command.set(f'delete method { result[0] } { result[1]}'))

    def rename_method(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        meth_options = {cb['name']: list(cb['methods'].keys()) for cb in self._class_boxes}
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("dynamic_combo", "Method", meth_options, 1),
            Dialog_Parts("text", "New Name")
        ]
        Dialog_Factory.create("Rename Method", dialog_params, lambda result: self._user_command.set(f'rename method { result[0] } { result[1] } { result[2] }'))

    def add_param(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        meth_options = {cb['name']: list(cb['methods'].keys()) for cb in self._class_boxes}
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("dynamic_combo", "Method", meth_options, 1),
            Dialog_Parts("text", "Name")
        ]
        Dialog_Factory.create("Add Parameter", dialog_params, lambda result:self._user_command.set(f'add param { result[0] } { result[1] } { result[2] }'))

    def delete_param(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        meth_options = {cb['name']: list(cb['methods'].keys()) for cb in self._class_boxes}
        param_options = {cb['name']: cb['methods'] for cb in self._class_boxes}
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("dynamic_combo", "Method", meth_options, 1),
            Dialog_Parts("dynamic_combo", "Param", param_options, 2)
        ]
        Dialog_Factory.create("Delete Parameter", dialog_params, lambda result:self._user_command.set(f'delete param { result[0] } { result[1] } { result[2] }'))

    def rename_param(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        meth_options = {cb['name']: list(cb['methods'].keys()) for cb in self._class_boxes}
        param_options = {cb['name']: cb['methods'] for cb in self._class_boxes}
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("dynamic_combo", "Method", meth_options, 1),
            Dialog_Parts("dynamic_combo", "Param", param_options, 2),
            Dialog_Parts("text", "New Name")
        ]
        Dialog_Factory.create("Delete Parameter", dialog_params, lambda result:self._user_command.set(f'delete param { result[0] } { result[1] } { result[2] } { result[3] }'))

    def add_relation(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        rel_options = ["Aggregation", "Composition", "Inheritance", "Realization"]
        dialog_params = [
            Dialog_Parts("combo", "Source", class_options),
            Dialog_Parts("combo", "Destination", class_options),
            Dialog_Parts("combo", "Type", rel_options)
        ]
        Dialog_Factory.create("Add Relation", dialog_params, lambda result:self._user_command.set("add relation " + result[0] + " " + result[1] + " " + result[2]))

    def delete_relation(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        dialog_params = [
            Dialog_Parts("combo", "Source", class_options),
            Dialog_Parts("combo", "Destination", class_options)
        ]
        Dialog_Factory.create("Add Relation", dialog_params, lambda result:self._user_command.set("delete relation " + result[0] + " " + result[1]))

#===================================== Dialog Factory =====================================#
        
class Dialog_Parts:
    """
    Input Type: Text, Combo, or Dynamic Combo.
        Text: A label and text input.
        Combo: A label and a drop down menu populated from a list.
        Dynamic Combo: A label and dropdown populated based on the selection of the previous.

    Title: The Title of the Dialog Card

    Values: The values of the rows in the Dialog Card
    """
    def __init__(self, input_type:str, title:str, values = None, check_count=0):
        self._input_type = input_type
        self._title = title
        self._values = values
        self._check_count = check_count

class Dialog_Factory:
    """
    Creates a Dialog based on the parts passed to it.

    Return:
        A list of strings.
            NOTE: Based on how our application works, you need to make sure you
            are adding spaces correctly when you recreate the command.
    """
    @staticmethod
    def create(dialog_name, params, callback):
        """
        Creates the base of the Dialog, and calls the actual create function.
        """
        if isinstance(params, Dialog_Parts):
            params = [params]
        if isinstance(params, list):
            Dialog_Factory._create(dialog_name, params, callback)

    @staticmethod
    def _create(dialog_name, params: list[Dialog_Parts], callback):
        frame = tk.Tk()
        frame.title(dialog_name)
        selects = []

        def action_ok():
            """
            Appends the selections/entry to the return result
            """
            result = []
            for s in selects:
                result.append(s.get())
            callback(result)
            action_destroy()
        
        def action_destroy():
            frame.destroy()

        def update_options(curr_box: ttk.Combobox, index: int, check_count: int, dy_values: dict):
            """
            Updates the options in the Dynamic Combo based on selection of previous dropdowns.
            """
            for i in range(index - check_count, index):
                prev_selection = selects[i].get()
                if prev_selection:
                    dy_values = dy_values[prev_selection]
                else:
                    dy_values = []
            curr_box["values"] = dy_values
            if len(curr_box["values"]) > 0:
                curr_box.current(0)
            else:
                curr_box.set('')
            curr_box.event_generate("<<ComboboxSelected>>")

        for i, p in enumerate(params):
            tk.Label(frame, text = f'{ p._title }:').grid(row = i, column = 0, padx = 5, pady = 5, sticky = tk.W)
            # Creates a dropdown for the dialog
            if p._input_type == 'combo':
                sel = tk.StringVar()
                out = ttk.Combobox(frame, values = p._values, textvariable = sel, state = "readonly")
                out.current(0)
                sel.set(p._values[0])
            # Creates a dropdown that is linked to previous dropdown
            elif p._input_type == 'dynamic_combo':
                sel = tk.StringVar()
                out = ttk.Combobox(frame, values = p._values, textvariable = sel, state = "readonly")
                prev_combo = selects[i - 1]
                update_options(out, i, p._check_count, p._values)
                prev_combo.bind("<<ComboboxSelected>>",
                                lambda event, curr_box=out, index=i, check_count=p._check_count, dy_values=p._values:\
                                update_options(curr_box, index, check_count, dy_values))
            # Creates a text entry
            elif p._input_type == 'text':
                out = tk.Entry(frame)

            out.grid(row = i, column = 1, padx = 5, pady = 5)
            selects.append(out)

        btn_ok = tk.Button(frame, text = "OK", command = action_ok)
        btn_ok.grid(row = len(params) + 1, column = 0, padx = 5, pady = 10)

        btn_cncl = tk.Button(frame, text = "Cancel", command = action_destroy)
        btn_cncl.grid(row = len(params) + 1, column = 1, padx = 5, pady = 10)

        # This is putting the pop up in the middle of my screen. Which is better than way off to the side
        frame.update_idletasks()

        # monitor resolution
        win_width = frame.winfo_screenwidth()
        win_height = frame.winfo_screenheight()

        # calculated frame dimensions
        frame_height = frame.winfo_reqheight()
        frame_width = frame.winfo_reqwidth()

        # integer offset for positions of anchor for frame
        x_offset = (win_width - frame_width) // 2
        y_offset = (win_height - frame_height) // 2

        # use frame.geometry to set, uses a 'secret sauce' string like "1024x768+400+200"
        frame.geometry(f'{ frame_width }x{ frame_height }+{ x_offset }+{ y_offset }')
