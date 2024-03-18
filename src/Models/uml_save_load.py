from Models.uml_visitor import UML_Visitor
from Models.uml_class import UML_Class

class UML_Save_Visitor(UML_Visitor):
    def __init__(self) -> None:
        pass

    def visit_diagram(self, uml_diagram):
        raise NotImplementedError
    
    def visit_class(self, uml_class):
        return uml_class.get_name()
    
    def visit_field(self, uml_field):
        raise NotImplementedError
    
    def visit_method(self, uml_method):
        raise NotImplementedError
    
    def visit_param(self, uml_param):
        raise NotImplementedError
    
    def visit_relation(self, uml_relation):
        raise NotImplementedError
