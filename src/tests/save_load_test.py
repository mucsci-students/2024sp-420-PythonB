from Models.uml_save_load import UML_Save_Visitor, encode_json, decode_json
from Models.uml_save_load import load_field
from Models.uml_save_load import load_param
from Models.uml_save_load import load_method
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
    obj = fld1.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Field1'
    loaded_fld1 = load_field(content)
    assert fld1 is not loaded_fld1
    assert fld1 == loaded_fld1

def test_save_load_param():
    save_visitor = UML_Save_Visitor()

    prm1 = UML_Param('Param1')
    #save 'Param1'
    obj = prm1.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Param1'
    loaded_prm1 = load_param(content)
    assert prm1 is not loaded_prm1
    assert prm1 == loaded_prm1

def test_save_load_method():
    save_visitor = UML_Save_Visitor()

    mth1 = UML_Method('Method1', 'string')
    #save 'Method1'
    obj = mth1.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Method1'
    loaded_mth1 = load_method(content)
    assert mth1 is not loaded_mth1
    assert mth1 == loaded_mth1

    mth2 = UML_Method('Method2', 'void', 'param1')
    #save 'Method2'
    obj = mth2.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Method2'
    loaded_mth2 = load_method(content)
    assert mth2 is not loaded_mth2
    assert mth2 == loaded_mth2