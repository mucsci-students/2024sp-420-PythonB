from ..Models.uml_class import UML_Class
from ..Models.uml_field import UML_Field
from ..Models.uml_method import UML_Method

def test_ctor():
    cl = UML_Class("class")
    assert cl._name == "class"
    assert len(cl._fields) == 0
    assert len(cl._methods) == 0

def test_get_name():
    cl = UML_Class("class")

    assert cl.get_name() == "class"
    assert cl.get_name() != "Minecraft"

def test_add_field():
    cl = UML_Class("class")
    cl.add_field("field1", "x")

    assert str(UML_Field("field1", "x")) == str(cl._fields[0])
    assert str(UML_Field("field2", "x")) != str(cl._fields[0])

def test_add_method():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")

    assert str(UML_Method("mthd", "int", "p1", "p2")) == str(cl._methods[0])
    assert str(UML_Method("mthd", "int")) != str(cl._methods[0])

def test_delete_field():
    cl = UML_Class("class")
    cl.add_field("field1", "x")
    cl.add_field("field2", "y")

    assert str(UML_Field("field1", "x")) == str(cl._fields[0])
    assert str(UML_Field("field2", "y")) == str(cl._fields[1])
    cl.delete_field("field1")
    assert str(UML_Field("field1", "x")) != str(cl._fields[0])
    assert str(UML_Field("field2", "y")) == str(cl._fields[0])

def test_delete_method():
    cl = UML_Class("class")
    cl.add_method("Kwanzaa", "int", "p1", "p2")
    cl.add_method("mth3", "void")

    m1 = UML_Method("Kwanzaa", "int", "p1", "p2")
    m2 = UML_Method("mth3", "void")

    assert next((m for m in cl._methods if str(m) == str(m1)), False)
    assert next((m for m in cl._methods if str(m) == str(m2)), False)

    cl.delete_method("Kwanzaa")

    assert next((m for m in cl._methods if str(m) == str(m1)), True)
    assert next((m for m in cl._methods if str(m) == str(m2)), False)

def test_get_field():
    cl = UML_Class("class")
    cl.add_field("field1", "x")

    f1 = UML_Field("field1", "x")


    assert cl.get_field("field1")
    assert str(cl.get_field("field1")) == str(f1)

def test_get_method():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")

    m1 = UML_Method("mthd", "int", "p1", "p2")

    assert cl.get_method("mthd")
    assert str(cl.get_method("mthd")) == str(m1)

def test_get_fields():
    cl = UML_Class("class")
    cl.add_field("field1", "x")
    cl.add_field("field2", "y")

    flds = cl.get_fields()

    assert len(flds) == 2
    assert str(UML_Field("field1", "x")) == str(flds[0])
    assert str(UML_Field("field2", "y")) == str(flds[1])
    assert str(UML_Field("field1", "x")) != str(flds[1])
    assert str(UML_Field("field2", "y")) != str(flds[0])

def test_get_methods():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")
    cl.add_method("mth3", "void")

    mthds = cl.get_methods()
    m1 = UML_Method("mthd", "int", "p1", "p2")
    m2 = UML_Method("mth3", "void")

    assert len(mthds) == 2
    assert str(m1) == str(cl._methods[0])
    assert str(m2) == str(cl._methods[1])

def test_eq():
    c1 = UML_Class("class")
    c2 = UML_Class("class")
    c3 = UML_Class("attribute")
    c4 = UML_Field("hi")

    assert c1 == c1
    assert c1 == c2
    assert c1 != c3
    assert c1 != c4

def test_str():
    c1 = UML_Class("class")
    c1.add_field("field", "type")
    c1.add_method("method", "ret", "p1")

    fld = UML_Field("field", "type")
    mthd = UML_Method("method", "ret", "p1")

    class_str = c1.get_name() + ':\n   Fields:' + '\n      %s' % str(c1.get_field("field")) + '\n   Methods:' + '\n      %s' % str(c1.get_method("method"))
    assert str(c1) == class_str
    assert str(c1) != "Roger"
