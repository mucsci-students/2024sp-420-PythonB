from Models.uml_save_load import UML_Save_Visitor, encode_json, decode_json
from Models.uml_save_load import load_field
from Models.uml_save_load import load_param
from Models.uml_save_load import load_method
from Models.uml_save_load import load_class
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

    mth3 = UML_Method('Method2', 'void', 'param1', 'param2')
    #save 'Method3'
    obj = mth3.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Method3'
    loaded_mth3 = load_method(content)
    assert mth3 is not loaded_mth3
    assert mth3 == loaded_mth3

def test_save_load_class():
    save_visitor = UML_Save_Visitor()

    cls1 = UML_Class('Class1')
    #save 'Class1'
    obj = cls1.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Class1'
    loaded_cls1 = load_class(content)
    assert cls1 is not loaded_cls1
    assert cls1 == loaded_cls1

    cls2 = UML_Class('Class2')
    cls2.add_field('Field1', 'string')
    #save 'Class2'
    obj = cls2.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Class2'
    loaded_cls2 = load_class(content)
    assert cls2 is not loaded_cls2
    assert cls2 == loaded_cls2

    cls3 = UML_Class('Class3')
    cls3.add_field('Field1', 'string')
    cls3.add_field('Field2', 'void')
    #save 'Class3'
    obj = cls3.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Class3'
    loaded_cls3 = load_class(content)
    assert cls3 is not loaded_cls3
    assert cls3 == loaded_cls3

    cls4 = UML_Class('Class4')
    cls4.add_method('Method1', 'string')
    #save 'Class4'
    obj = cls4.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Class4'
    loaded_cls4 = load_class(content)
    assert cls4 is not loaded_cls4
    assert cls4 == loaded_cls4

    cls5 = UML_Class('Class5')
    cls5.add_method('Method1', 'string')
    cls5.add_method('Method2', 'void', 'Param1')
    cls5.add_method('Method3', 'int', 'Param1', 'Param2')
    #save 'Class5'
    obj = cls5.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Class5'
    loaded_cls5 = load_class(content)
    assert cls5 is not loaded_cls5
    assert cls5 == loaded_cls5

    cls6 = UML_Class('Class6')
    cls6.add_field('Field1', 'string')
    cls6.add_field('Field2', 'void')
    cls6.add_method('Method1', 'string')
    cls6.add_method('Method2', 'void', 'Param1')
    cls6.add_method('Method3', 'int', 'Param1', 'Param2')
    #save 'Class6'
    obj = cls6.accept(save_visitor)
    json = encode_json(obj)
    content = decode_json(json)
    #load 'Class6'
    loaded_cls6 = load_class(content)
    assert cls6 is not loaded_cls6
    assert cls6 == loaded_cls6