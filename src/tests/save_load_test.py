from ..Models.uml_save_load import UML_Save_Visitor
from ..Models.uml_class import UML_Class

def test_save():
    cls = UML_Class('Class1')
    save_visitor = UML_Save_Visitor()
    assert cls.accept(save_visitor) == 'Class1'