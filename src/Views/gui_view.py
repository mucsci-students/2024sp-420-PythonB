from tkinter import ttk

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

    def draw(self, photo, class_boxes):
        self._image = photo
        # margin = 500
        self.diagram_canvas.create_image(-500 - self._camera_x, -500 - self._camera_y, anchor=tk.NW, image=self._image)
        self._class_boxes = class_boxes
        #debug: display lines bounding class boxes
        for cb in self._class_boxes:
            top_left = cb['x'] - self._camera_x, cb['y'] - self._camera_y
            top_right = cb['x'] + cb['width'] - self._camera_x, cb['y'] - self._camera_y
            bot_left = cb['x'] - self._camera_x, cb['y'] + cb['height'] - self._camera_y
            bot_right = cb['x'] + cb['width'] - self._camera_x, cb['y'] + cb['height'] - self._camera_y
            self.diagram_canvas.create_line(top_left, top_right)
            self.diagram_canvas.create_line(top_right, bot_right)
            self.diagram_canvas.create_line(bot_right, bot_left)
            self.diagram_canvas.create_line(bot_left, top_left)

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
        print('Debugging: {}'.format(cmd))
        return cmd
    
    def get_all_positions(self):
        return [[cb._name, cb._last_x, cb._last_y] for cb in self._class_boxes]

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
        layout_menu.add_command(label="Return to Center", command=self.center)
        menu_bar.add_cascade(label="Layout", menu=layout_menu)
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

        self._btn_class = tk.Button(self._sidebar, text = "Classes", command = self.class_options_menu)
        self._btn_class.pack(fill = tk.X, padx = (5, 5), pady = (10, 5))

        self._btn_fields = tk.Button(self._sidebar, text = "Fields", command = self.fields_options_menu)
        self._btn_fields.pack(fill = tk.X, padx = (5, 5), pady = (5, 5))

        self._btn_methods = tk.Button(self._sidebar, text = "Methods", command = self.methods_options_menu)
        self._btn_methods.pack(fill = tk.X, padx = (5, 5), pady = (5, 5))

        self._btn_params = tk.Button(self._sidebar, text = "Parameters", command = self.params_options_menu)
        self._btn_params.pack(fill = tk.X, padx = (5, 5), pady = (5, 5))

        self._btn_relations = tk.Button(self._sidebar, text = "Relationships", command = self.relations_options_menu)
        self._btn_relations.pack(fill = tk.X, padx = (5, 5), pady = (5, 5))

    def update_button_state(self):
        self._btn_class.config(state = "disabled")
        self._btn_fields.config(state = "disabled")
        self._btn_methods.config(state = "disabled")
        self._btn_params.config(state = "disabled")
        self._btn_relations.config(state = "disabled")

        self._btn_class.config(state = "active")
        class_count = len(self._class_boxes)
        if class_count > 0:
            self._btn_fields.config(state = "active")
            self._btn_methods.config(state = "active")
            self._btn_relations.config(state = "active")
            method_count = sum(len(cb['methods']) for cb in self._class_boxes)
            if method_count > 0:
                self._btn_params.config(state = "active")

    def create_diagram_space(self):
        self.diagram_canvas = tk.Canvas(self, bg = 'white')
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
        if len(self._class_boxes) > 1:
            menu.add_command(label = "Add Relationship", command = self.add_relation)
            menu.add_command(label = "Delete Relationship", command = self.delete_relation)
        try:
            menu.tk_popup(x = self._sidebar.winfo_pointerx(), y = self._sidebar.winfo_pointery())
        finally:
            menu.grab_release()

#===================================== Diagram Functions =====================================#

    def add_class(self):
        dialog_params = Dialog_Parts("text", "Class Name")
        Dialog_Factory.create("Add Class", dialog_params, lambda result:self._user_command.set("add class " + result[0]))
        
    def delete_class(self) -> str:
        class_options = [cb['name'] for cb in self._class_boxes]
        dialog_params = Dialog_Parts("combo", "Class Name", class_options)
        Dialog_Factory.create("Delete Class", dialog_params, lambda result:self._user_command.set("delete class " + result[0]))
    
    def rename_class(self) -> None:
        class_options = [cb._name for cb in self._class_boxes]
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("text", "New Name")
            ]
        Dialog_Factory.create("Rename Class", dialog_params, lambda result:self._user_command.set("rename class " + result[0] + " " + result[1]))

        class_options = [cb['name'] for cb in self._class_boxes]

        dialog = Rename_Class_Dialog(self, class_options, "Rename Class")
        if dialog.result:
            old_name, new_name = dialog.result
            new_command = "rename class " + old_name + " " + new_name
            self._user_command.set(new_command)

    def add_field(self) -> None:
        class_options = [cb['name'] for cb in self._class_boxes]
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("text", "Field"),
            Dialog_Parts("text", "Type")
        ]
        Dialog_Factory.create("Add Field", dialog_params, lambda result:self._user_command.set("add field " + result[0] + " " + result[1] + " " + result[2]))

    def delete_field(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        # dialog_params = [
        #     Dialog_Parts("combo", "Class", class_options),
        #     Dialog_Parts("combo", "Field", something)
        # ]
        dialog_result = Delete_Field_Dialog(self, class_options, title = "Delete Field").result
        if dialog_result:
            class_name, field_name = dialog_result
            
            new_command = "delete field " + class_name + " " + field_name
            self._user_command.set(new_command)

    def rename_field(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        dialog_result = Rename_Field_Dialog(self, class_options, title = "Rename Field").result
        if dialog_result:
            class_name, old_name, new_name = dialog_result

            new_command = "rename field " + class_name + " " + old_name + " " + new_name
            self._user_command.set(new_command)

    def add_method(self):
        class_options = [cb['name'] for cb in self._class_boxes]
        dialog_params = [
            Dialog_Parts("combo", "Class", class_options),
            Dialog_Parts("text", "Method"),
            Dialog_Parts("text", "Type")
        ]
        Dialog_Factory.create("Add Method", dialog_params, lambda result:self._user_command.set("add method " + result[0] + " " + result[1] + " " + result[2]))

    def delete_method(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        dialog_result = Delete_Method_Dialog(self, class_options, title = "Delete Method").result
        if dialog_result:
            class_name, method_name = dialog_result
            
            new_command = "delete method " + class_name + " " + method_name
            self._user_command.set(new_command)

    def rename_method(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        dialog_result = Rename_Method_Dialog(self, class_options, title = "Rename Method").result
        if dialog_result:
            class_name, old_name, new_name = dialog_result
        
            new_command = "rename method " + class_name + " " + old_name + " " + new_name
            self._user_command.set(new_command)

    def add_param(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        dialog_result = Add_Parameter_Dialog(self, class_options, title="Add Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result

            new_command = "add param " + class_name + " " + method_name + " " + param_name
            self._user_command.set(new_command)

    def delete_param(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        dialog_result = Delete_Parameter_Dialog(self, class_options, "Delete Parameter").result
        if dialog_result:
            class_name, method_name, param_name = dialog_result

            new_command = "delete param " + class_name + " " + method_name + " " + param_name
            self._user_command.set(new_command)

    def rename_param(self):
        class_options = [cb['name'] for cb in self._class_boxes]

        dialog_result = Rename_Parameter_Dialog(self, class_options, title="Rename Parameter").result
        if dialog_result:
            class_name, method_name, old_name, new_name = dialog_result

            new_command = "rename param " + class_name + " " + method_name + " " + old_name + " " + new_name
            self._user_command.set(new_command)

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

#===================================== Helper Functions =====================================#
            
    def get_next_position(self):
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
        
#===================================== Dialog Factory =====================================#
        
class Dialog_Parts:
    def __init__(self, input_type:str, title:str, values = None, default = None):
        self._input_type = input_type
        self._title = title
        self._values = values
        self._default = default

class Dialog_Factory:
    @abstractmethod
    def create(dialog_name, params, callback):
        if isinstance(params, Dialog_Parts):
            params = [params]
        if isinstance(params, list):
            Dialog_Factory._create(dialog_name, params, callback)

    def _create(dialog_name, params, callback):
        frame = tk.Tk()
        frame.title(dialog_name)
        selects = []

        def action_ok():
            result = []
            for s in selects:
                result.append(s.get())
            callback(result)
            action_destroy()
        
        def action_destroy():
            frame.destroy()

        for i, p in enumerate(params):
            tk.Label(frame, text = f'{ p._title }:').grid(row = i, column = 0, padx = 5, pady = 5, sticky = tk.W)
            if p._input_type == 'combo':
                sel = tk.StringVar()
                out = ttk.Combobox(frame, values = p._values, textvariable = sel)
                if p._default is not None:
                    sel.set(p._default)
                else:
                    sel.set(p._values[0])
            elif p._input_type == 'text':
                out = tk.Entry(frame)
                if p._default is not None:
                    out.insert(tk.END, p._default)
            out.grid(row = i, column = 1, padx = 5, pady = 5)
            selects.append(out)

        btn_ok = tk.Button(frame, text = "OK", command = action_ok)
        btn_ok.grid(row = len(params) + 1, column = 0, padx = 5, pady = 10)

        btn_cncl = tk.Button(frame, text = "Cancel", command = action_destroy)
        btn_cncl.grid(row = len(params) + 1, column = 1, padx = 5, pady = 10)

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

        return master

    def update_options(self, *args):
        self._delete_field.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb['name'] == class_name:
                options = cb['fields']
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

        return master

    def update_options(self, *args):
        self._delete_field.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb['name'] == class_name:
                options = cb['fields']
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

        return master

    def update_options(self, *args):
        self._delete_method.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb['name'] == class_name:
                options = list(cb['methods'])
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

        return master

    def update_options(self, *args):
        self._delete_method.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb['name'] == class_name:
                options = list(cb['methods'])
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

        return master

    def update_options(self, *args):
        self._method_select.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb['name'] == class_name:
                options = list(cb['methods'])
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

        return master

    def update_options(self, *args):
        self._method_select.set('')
        class_name = self._class.get()
        for cb in self.parent._class_boxes:
            if cb['name'] == class_name:
                options = list(cb['methods'])
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
                if cb['name'] == class_name:
                    options = cb['methods'][self._method_select.get()]
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
            if cb['name'] == class_name:
                options = list(cb['methods'])
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
                if cb['name'] == class_name:
                    options = cb['methods'][self._method_select.get()]
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

#===================================== Class Card =====================================#

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