from ..Models.uml_field import UML_Field


def test_ctor_field():
    fld1 = UML_Field("field1", "int")
    assert isinstance(fld1, UML_Field)
    fld2 = UML_Field("field2", "void")
    assert isinstance(fld2, UML_Field)
    assert fld1._name == "field1"
    assert fld1._type == "int"
    assert fld2._name == "field2"
    assert fld2._type == "void"

def test_get_name_field():
    fld1 = UML_Field("field1", "int")
    fld2 = UML_Field("field2", "str")
    fld3 = UML_Field("field3", "int")
    fld4 = UML_Field("field1", "str")
    name1 = fld1.get_name()
    name2 = fld2.get_name()
    name3 = fld3.get_name()
    name4 = fld4.get_name()
    assert name1 == "field1"
    assert name1 == fld1._name
    assert name2 == "field2"
    assert name2 == fld2._name
    assert name3 == "field3"
    assert name3 == fld3._name
    assert name4 == name1

def test_get_type_field():
    fld1 = UML_Field("field1", "int")
    fld2 = UML_Field("field2", "str")
    fld3 = UML_Field("field3", "int")
    fld4 = UML_Field("field1", "str")
    fld5 = UML_Field("field1", "int")
    type1 = fld1.get_type()
    type2 = fld2.get_type()
    type3 = fld3.get_type()
    type4 = fld4.get_type()
    type5 = fld5.get_type()
    assert type1 == "int"
    assert type1 == fld1._type
    assert type2 == "str"
    assert type2 == fld2._type
    assert type3 == "int"
    assert type3 == fld3._type
    assert type4 == type2
    assert type5 == type1
    assert type5 == type3

def test_set_name_field():
    fld1 = UML_Field("field1", "int")
    fld2 = UML_Field("field2", "str")
    fld3 = UML_Field("field3", "int")
    assert fld1._name == "field1"
    assert fld2._name == "field2"
    assert fld3._name == "field3"
    fld1.set_name("Dio")
    fld2.set_name("Jotaro Kujo")
    fld3.set_name("Star Platinum")
    assert fld1._name == "Dio"
    assert fld1._name != "field1"
    assert fld2._name == "Jotaro Kujo"
    assert fld2._name != "field2"
    assert fld3._name == "Star Platinum"
    assert fld3._name != "field3"

def test_set_type_field():
    fld1 = UML_Field("field1", "int")
    fld2 = UML_Field("field2", "str")
    fld3 = UML_Field("field3", "int")
    assert fld1._type == "int"
    assert fld2._type == "str"
    assert fld3._type == "int"
    fld1.set_type("MUDA!")
    fld2.set_type("Good Grief...")
    fld3.set_type("ORA!")
    assert fld1._type == "MUDA!"
    assert fld1._type != "int"
    assert fld2._type == "Good Grief..."
    assert fld2._type != "str"
    assert fld3._type == "ORA!"
    assert fld3._type != "int"

def test_eq_field():
    fld1 = UML_Field("field1", "int")
    fld2 = UML_Field("field2", "str")
    fld3 = UML_Field("field3", "int")
    fld4 = UML_Field("field1", "str")
    fld5 = UML_Field("field1", "int")
    assert fld1 == fld1
    assert fld1 != fld2
    assert fld1 != fld3
    assert fld1 != fld4
    assert fld1 == fld5

def test_str_field():
    fld1 = UML_Field("field1", "int")
    result1 = "int field1"
    test1 = str(fld1)
    print(test1)
    assert test1 == result1
