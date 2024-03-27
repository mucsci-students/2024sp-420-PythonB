from Models.uml_diagram import UML_Diagram
from Views.gui_view import GUI_View

class GUI_Controller:

    def __init__(self):
        self._gui_view = GUI_View()

    def request_update(self):
        return self._gui_view.listen()
    
    def draw(self, diagram: UML_Diagram):
        self._gui_view.clear()
        self._gui_view.draw(diagram)