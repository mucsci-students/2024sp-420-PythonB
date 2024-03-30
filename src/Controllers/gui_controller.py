from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Views.gui_view import GUI_View

class GUI_Controller:

    def __init__(self):
        self._gui_view = GUI_View()

    def request_update(self):
        return self._gui_view.listen()
    
    def draw(self, diagram: UML_Diagram):
        self._gui_view.clear()
        for cls in diagram.get_all_classes():
            self.draw_class(cls)

    def draw_class(self, cls: UML_Class):
        self._gui_view.draw_class(cls.get_name(), cls.get_position_x(), cls.get_position_y())