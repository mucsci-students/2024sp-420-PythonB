from Models.uml_save_load import UML_Save_Visitor, load_schema, load_metaschema, encode_json, encode_json_without_validate
from Models.uml_save_load import encode_json_without_validate, decode_json_without_validate
from Models.uml_save_load import load_field
from Models.uml_save_load import load_param
from Models.uml_save_load import load_method
from Models.uml_save_load import load_class
from Models.uml_save_load import load_diagram
from Models.uml_save_load import diagram_to_json, json_to_diagram
from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method
from Models.uml_param import UML_Param
from Models.uml_relation import UML_Relation

import pytest

def test_save_load_field():
    save_visitor = UML_Save_Visitor()

    fld1 = UML_Field('Field1')
    #save 'Field1'
    obj = fld1.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Field1'
    loaded_fld1 = load_field(content)
    assert fld1 is not loaded_fld1
    assert fld1 == loaded_fld1

def test_save_load_param():
    save_visitor = UML_Save_Visitor()

    prm1 = UML_Param('Param1')
    #save 'Param1'
    obj = prm1.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Param1'
    loaded_prm1 = load_param(content)
    assert prm1 is not loaded_prm1
    assert prm1 == loaded_prm1

def test_save_load_method():
    save_visitor = UML_Save_Visitor()

    mth1 = UML_Method('Method1', 'string')
    #save 'Method1'
    obj = mth1.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Method1'
    loaded_mth1 = load_method(content)
    assert mth1 is not loaded_mth1
    assert mth1 == loaded_mth1

    mth2 = UML_Method('Method2', 'void', 'param1')
    #save 'Method2'
    obj = mth2.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Method2'
    loaded_mth2 = load_method(content)
    assert mth2 is not loaded_mth2
    assert mth2 == loaded_mth2

    mth3 = UML_Method('Method2', 'void', 'param1', 'param2')
    #save 'Method3'
    obj = mth3.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Method3'
    loaded_mth3 = load_method(content)
    assert mth3 is not loaded_mth3
    assert mth3 == loaded_mth3

def test_save_load_class():
    save_visitor = UML_Save_Visitor()

    cls1 = UML_Class('Class1')
    #save 'Class1'
    obj = cls1.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Class1'
    loaded_cls1 = load_class(content)
    assert cls1 is not loaded_cls1
    assert cls1 == loaded_cls1

    cls2 = UML_Class('Class2')
    cls2.add_field('Field1', 'string')
    #save 'Class2'
    obj = cls2.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Class2'
    loaded_cls2 = load_class(content)
    assert cls2 is not loaded_cls2
    assert cls2 == loaded_cls2

    cls3 = UML_Class('Class3')
    cls3.add_field('Field1', 'string')
    cls3.add_field('Field2', 'void')
    #save 'Class3'
    obj = cls3.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Class3'
    loaded_cls3 = load_class(content)
    assert cls3 is not loaded_cls3
    assert cls3 == loaded_cls3

    cls4 = UML_Class('Class4')
    cls4.add_method('Method1', 'string')
    #save 'Class4'
    obj = cls4.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
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
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
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
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Class6'
    loaded_cls6 = load_class(content)
    assert cls6 is not loaded_cls6
    assert cls6 == loaded_cls6

    cls7 = UML_Class('Class7')
    cls7.add_field('Field1', 'string')
    cls7.add_field('Field2', 'void')
    cls7.add_method('Method1', 'string')
    cls7.add_method('Method2', 'void', 'Param1')
    cls7.add_method('Method3', 'int', 'Param1', 'Param2')
    cls7.set_position_with_delta([1, -1])
    #save 'Class7'
    obj = cls7.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Class7'
    loaded_cls7 = load_class(content)
    assert cls7 is not loaded_cls7
    assert cls7 == loaded_cls7
    assert cls7.get_position() == loaded_cls7.get_position()
    assert cls7.get_position_x() == loaded_cls7.get_position_x()
    assert cls7.get_position_y() == loaded_cls7.get_position_y()

def test_save_load_diagram():
    save_visitor = UML_Save_Visitor()

    dgm1 = UML_Diagram()
    dgm1.add_class('Class1')
    cls1 = dgm1.get_class('Class1')
    dgm1.add_class('Class2')
    cls2 = dgm1.get_class('Class2')
    cls2.add_field('Field1', 'string')
    cls2.add_field('Field2', 'int')
    dgm1.add_class('Class3')
    cls3 = dgm1.get_class('Class3')
    cls3.add_method('Method1', 'string')
    cls3.add_method('Method2', 'int', 'Param1')
    cls3.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_class('Class4')
    cls4 = dgm1.get_class('Class4')
    cls4.add_field('Field1', 'string')
    cls4.add_field('Field2', 'int')
    cls4.add_method('Method1', 'string')
    cls4.add_method('Method2', 'int', 'Param1')
    cls4.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_relation('Class1', 'Class2', 'Aggregation')
    dgm1.add_relation('Class2', 'Class1', 'composition')
    #save 'Diagram1'
    obj = dgm1.accept(save_visitor)
    json = encode_json_without_validate(obj)
    content = decode_json_without_validate(json)
    #load 'Method1'
    loaded_dgm1 = load_diagram(content)
    assert dgm1 is not loaded_dgm1
    assert dgm1 == loaded_dgm1

    #TODO: add more tests for diagram

def test_simple_diagram_json_convert_func():
    dgm1 = UML_Diagram()
    dgm1.add_class('Class1')
    cls1 = dgm1.get_class('Class1')
    dgm1.add_class('Class2')
    cls2 = dgm1.get_class('Class2')
    cls2.add_field('Field1', 'string')
    cls2.add_field('Field2', 'int')
    dgm1.add_class('Class3')
    cls3 = dgm1.get_class('Class3')
    cls3.add_method('Method1', 'string')
    cls3.add_method('Method2', 'int', 'Param1')
    cls3.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_class('Class4')
    cls4 = dgm1.get_class('Class4')
    cls4.add_field('Field1', 'string')
    cls4.add_field('Field2', 'int')
    cls4.add_method('Method1', 'string')
    cls4.add_method('Method2', 'int', 'Param1')
    cls4.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_relation('Class1', 'Class2', 'Aggregation')
    dgm1.add_relation('Class2', 'Class1', 'composition')

    json = diagram_to_json(dgm1)
    loaded_dgm1 = json_to_diagram(json)
    assert dgm1 is not loaded_dgm1
    assert dgm1 == loaded_dgm1

def test_wild_exceptions():
    with pytest.raises(ValueError) as FNF: 
        load_schema("badname")
    assert str(FNF.value) == "Schema file not found."

    with pytest.raises(ValueError) as MFNF:
        load_metaschema("badname")
    assert str(MFNF.value) == "Schema file not found."

    with pytest.raises(Exception) as E:
        encode_json_without_validate(pytest.raises)
    assert isinstance(E.value, TypeError)

    with pytest.raises(Exception) as E2:
        encode_json(pytest.raises)
    assert isinstance(E.value, TypeError)