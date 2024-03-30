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
        width = len(cls.get_name())
        text_fields = []
        for field in cls.get_fields():
            text_fields.append([field.get_type(), field.get_name()])
            width = max(width, len(field.get_type()) + 1 + len(field.get_name()))
        text_methods = []
        for method in cls.get_methods():
            text_method = [[method.get_ret(), method.get_name()]]; text_methods.append(text_method)
            # ret name(param1, param2, param3)
            ac = len(method.get_ret()) + 1 + len(method.get_name()) + 1 + (len(method.get_params()) - 1) * 2 + 1
            for param in method.get_params():
                #TODO: Param type is undefined
                text_param = [param.get_name()]; text_method.append(text_param)
                ac += len(param.get_name())
            width = max(width, ac)
        self._gui_view.draw_class(cls.get_name(), cls.get_position_x(), cls.get_position_y(), text_methods, text_fields, width)