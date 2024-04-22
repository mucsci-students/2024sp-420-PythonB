from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_relation import UML_Relation
from Views.gui_view import GUI_View

class GUI_Controller:

    def __init__(self):
        self._gui_view = GUI_View()

    def error_message(self, message: str) -> None:
        self._gui_view.error_message(message)

    def request_update(self):
        return self._gui_view.listen()
    
    def draw(self, diagram: UML_Diagram, image_data, class_boxes):
        self._gui_view.clear()
        self._gui_view.draw(image_data, class_boxes)

    def get_camera_pos(self):
        return self._gui_view.camera_pos()
    
    def get_viewport_size(self):
        return self._gui_view.viewport_size()
    
    def should_save(self) -> bool:
        return self._gui_view.should_save()