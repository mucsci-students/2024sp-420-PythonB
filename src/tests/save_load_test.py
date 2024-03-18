from Models.uml_save_load import UML_Save_Visitor, decode_json, load_field, load_param
from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method
from Models.uml_param import UML_Param
from Models.uml_relation import UML_Relation

def test_save_load_field():
    save_visitor = UML_Save_Visitor()

    fld1 = UML_Field('Field1')
    #save 'Field1'
    json_content = fld1.accept(save_visitor)
    content = decode_json(json_content)
    #load 'Field1'
    loaded_fld1 = load_field(content)
    assert fld1 == loaded_fld1

def test_save_load_param():
    save_visitor = UML_Save_Visitor()

    prm1 = UML_Param('Param1')
    #save 'Param1'
    json_content = prm1.accept(save_visitor)
    content = decode_json(json_content)
    #load 'Param1'
    loaded_prm1 = load_param(content)
    assert prm1 == loaded_prm1