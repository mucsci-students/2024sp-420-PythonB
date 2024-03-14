from Models.uml_field import UML_Field

def test_ctor_field():
    fld1 = UML_Field("field1", "int")
    assert isinstance(fld1, UML_Field)
    fld2 = UML_Field("field2", "void")
    assert isinstance(fld2, UML_Field)
    assert fld1._name == "field1"
    assert fld1._type == "int"
    assert fld2._name == "field2"
    assert fld2._type == "void"

fld1 = UML_Field("field1", "int")
fld2 = UML_Field("field2", "str")
fld3 = UML_Field("field3", "int")
fld4 = UML_Field("field1", "str")
fld5 = UML_Field("field1", "int")

def test_get_name_field():
    name1 = fld1.get_name()
    name2 = fld2.get_name()
    name3 = fld3.get_name()
    name4 = fld4.get_name()
    name5 = fld5.get_name()
    assert name1 == "field1"
    assert name1 == fld1._name
    assert name2 == "field2"
    assert name2 == fld2._name
    assert name3 == "field3"
    assert name3 == fld3._name
    assert name4 == name1
    assert name5 == name1
    assert name5 == name4
