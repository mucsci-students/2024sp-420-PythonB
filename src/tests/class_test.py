from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method

import pytest

def test_ctor():
    cl = UML_Class("class")
    assert cl._name == "class"
    assert len(cl._fields) == 0
    assert len(cl._methods) == 0

def test_get_name():
    cl = UML_Class("class")

    assert cl.get_name() == "class"
    assert cl.get_name() != "Minecraft"

def test_set_class():
    cl = UML_Class("class")
    assert cl.get_name() == "class"

    cl.set_name("class2")
    assert cl.get_name() == "class2"


def test_add_field():
    cl = UML_Class("class")
    field = UML_Field("field1")
    cl.add_field(field.get_name(), field.get_type())

    assert field == cl._fields[0]
    assert UML_Field("field2", "x") != cl._fields[0]

    with pytest.raises(ValueError) as VE:
        cl.add_field(field.get_name(), field.get_type())
    assert str(VE.value) == "field1 already exists"

def test_add_method():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")

    assert UML_Method("mthd", "int", "p1", "p2") == cl._methods[0]
    assert UML_Method("mthd", "int") != str(cl._methods[0])

    with pytest.raises(ValueError) as VE:
        cl.add_method("mthd", "int", "p1", "p2")
    assert str(VE.value) == "mthd already exists"

def test_delete_field():
    cl = UML_Class("class")
    cl.add_field("field1", "x")
    cl.add_field("field2", "y")

    assert UML_Field("field1", "x") == cl._fields[0]
    assert UML_Field("field2", "y") == cl._fields[1]
    cl.delete_field("field1")
    assert UML_Field("field1", "x") != cl._fields[0]
    assert UML_Field("field2", "y") == cl._fields[0]

    with pytest.raises(ValueError) as VE:
        cl.delete_field("field1")
    assert str(VE.value) == "Field field1 does not exist"



def test_delete_method():
    cl = UML_Class("class")
    cl.add_method("Kwanzaa", "int", "p1", "p2")
    cl.add_method("mth3", "void")

    m1 = UML_Method("Kwanzaa", "int", "p1", "p2")
    m2 = UML_Method("mth3", "void")

    assert next((m for m in cl._methods if m == m1), False)
    assert next((m for m in cl._methods if m == m2), False)

    cl.delete_method("Kwanzaa")

    assert next((m for m in cl._methods if m == m1), True)
    assert next((m for m in cl._methods if m == m2), False)

    with pytest.raises(ValueError) as VE:
        cl.delete_method("Kwanzaa")
    assert str(VE.value) == "Method Kwanzaa does not exist"

def test_get_field():
    cl = UML_Class("class")
    cl.add_field("field1", "x")
    f1 = UML_Field("field1", "x")

    assert cl.get_field("field1")
    assert cl.get_field("field1") == f1

    with pytest.raises(ValueError) as VE:
        cl.get_field("badname")
    assert str(VE.value) == "Field badname does not exist"

def test_get_method():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")
    m1 = UML_Method("mthd", "int", "p1", "p2")

    assert cl.get_method("mthd")
    assert cl.get_method("mthd") == m1

    with pytest.raises(ValueError) as VE:
        cl.get_method("badname")
    assert str(VE.value) == "Method badname does not exist"

def test_get_fields():
    cl = UML_Class("class")
    cl.add_field("field1", "x")
    cl.add_field("field2", "y")

    flds = cl.get_fields()

    assert len(flds) == 2
    assert UML_Field("field1", "x") == flds[0]
    assert UML_Field("field2", "y") == flds[1]
    assert UML_Field("field1", "x") != flds[1]
    assert UML_Field("field2", "y") != flds[0]

def test_get_methods():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")
    cl.add_method("mth3", "void")

    mthds = cl.get_methods()
    m1 = UML_Method("mthd", "int", "p1", "p2")
    m2 = UML_Method("mth3", "void")

    assert len(mthds) == 2
    assert m1 == cl._methods[0]
    assert m2 == cl._methods[1]

def test_get_position():
    cls1 = UML_Class("Class1")
    assert cls1.get_position() == [0, 0]

def test_get_position_x():
    cls1 = UML_Class("Class1")
    assert cls1.get_position_x() == 0

def test_get_position_y():
    cls1 = UML_Class("Class1")
    assert cls1.get_position_y() == 0

def test_set_position_with_delta():
    cls1 = UML_Class("Class1")
    cls1.set_position_with_delta([1, -1])
    assert cls1.get_position() == [1, -1]
    # These two are actually part of get_position_x() / get_position_y() test
    assert cls1.get_position_x() == 1
    assert cls1.get_position_y() == -1

def test_eq():
    c1 = UML_Class("class")
    c2 = UML_Class("class")
    c3 = UML_Class("attribute")
    c4 = UML_Field("hi")
    c5 = UML_Class("class")
    c5.set_position_with_delta([1, 2])

    assert c1 == c1
    assert c1 == c2
    assert c1 != c3
    assert c1 != c4
    assert c1 == c5
