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

def test_get_type_field():
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
    assert fld1._name == "field1"
    assert fld2._name == "field2"
    assert fld3._name == "field3"
    assert fld4._name == "field1"
    assert fld5._name == "field1"
    fld1.set_name("Robert E. O. Speedwagon")
    fld2.set_name("Joseph Joestar")
    fld3.set_name("Dio")
    fld4.set_name("Jotaro Kujo")
    fld5.set_name("Star Platinum")
    assert fld1._name == "Robert E. O. Speedwagon"
    assert fld1._name != "field1"
    assert fld2._name == "Joseph Joestar"
    assert fld2._name != "field2"
    assert fld3._name == "Dio"
    assert fld3._name != "field3"
    assert fld4._name == "Jotaro Kujo"
    assert fld4._name != "field1"
    assert fld5._name == "Star Platinum"
    assert fld5._name != "field1"

fld1.set_name("field1")
fld2.set_name("field2")
fld3.set_name("field3")
fld4.set_name("field1")
fld5.set_name("field1")

def test_set_type_field():
    assert fld1._type == "int"
    assert fld2._type == "str"
    assert fld3._type == "int"
    assert fld4._type == "str"
    assert fld5._type == "int"
    fld1.set_type("I'll always be there for you guys!")
    fld2.set_type("Next you'll say...")
    fld3.set_type("MUDA!")
    fld4.set_type("Good Grief...")
    fld5.set_type("ORA!")
    assert fld1._type == "I'll always be there for you guys!"
    assert fld1._type != "int"
    assert fld2._type == "Next you'll say..."
    assert fld2._type != "str"
    assert fld3._type == "MUDA!"
    assert fld3._type != "int"
    assert fld4._type == "Good Grief..."
    assert fld4._type != "str"
    assert fld5._type == "ORA!"
    assert fld5._type != "int"
    
fld1.set_type("int")
fld2.set_type("str")
fld3.set_type("int")
fld4.set_type("str")
fld5.set_type("int")

def test_eq_field():
    assert fld1 == fld1
    assert fld1 != fld2
    assert fld1 != fld3
    assert fld1 != fld4
    assert fld1 != fld5
    assert fld2 == fld2
    assert fld2 != fld3
    assert fld2 != fld4
    assert fld2 != fld5
    assert fld3 == fld3
    assert fld3 != fld4
    assert fld3 != fld5
    assert fld4 == fld4
    assert fld4 != fld5
    assert fld5 == fld5

def test_str_field():
    result1 = "int\nfield1"
    
    assert str(fld1) == result1