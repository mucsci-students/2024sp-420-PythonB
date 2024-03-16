from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method

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

    fld1 = UML_Field("field1", "x")
    fld2 = UML_Field("field2", "x")
    fld3 = UML_Field("field1", "y")

    assert fld1 in cl._fields
    assert fld2 not in cl._fields
    assert fld3 not in cl._fields

def test_add_method():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")

    mthd1 = UML_Method("mthd", "int", "p1", "p2")
    mthd2 = UML_Method("mthd", "int")
    mthd3 = UML_Method("not", "void")

    assert mthd1 in cl._methods
    assert mthd2 not in cl._methods
    assert mthd3 not in cl._methods

def test_delete_field():
    cl = UML_Class("class")
    cl.add_field("field1", "x")
    cl.add_field("field2", "y")

    f1 = UML_Field("field1", "x")
    f2 = UML_Field("field2", "y")
    cl.delete_field("field1")

    assert f1 not in cl._methods
    assert f2 in cl._fields

def test_delete_method():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")
    cl.add_method("mth3", "void")

    m1 = UML_Method("mthd", "int", "p1", "p2")
    m2 = UML_Method("mth3", "void")

    cl.delete_method("mthd")

    assert m1 not in cl._methods
    assert m2 in cl._methods

def test_get_field():
    cl = UML_Class("class")
    cl.add_field("field1", "x")

    f1 = UML_Field("field1", "x")


    assert cl.get_field("field1")
    assert cl.get_field("field1") == f1

def test_get_method():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")

    m1 = UML_Method("mthd", "int", "p1", "p2")

    assert cl.get_method()
    assert cl.get_method() == m1

def test_get_fields():
    cl = UML_Class("class")
    cl.add_field("field1", "x")
    cl.add_field("field2", "y")

    flds = cl.get_fields()
    f1 = UML_Field("field1", "x")
    f2 = UML_Field("field2", "y")
    f3 = UML_Field("field3")
    f4 = UML_Field("field1")

    
    assert len(flds) == 2
    assert f1 in flds
    assert f2 in flds
    assert "hi" not in flds
    assert f3 not in flds
    assert f4 not in flds

def test_get_methods():
    cl = UML_Class("class")
    cl.add_method("mthd", "int", "p1", "p2")
    cl.add_method("mth3", "void")

    mthds = cl.get_methods()
    m1 = UML_Method("mthd", "int", "p1", "p2")
    m2 = UML_Method("mth3", "void")
    m3 = UML_Method("mth3", "int")
    m4 = UML_Method("hi", "hello")


    assert len(mthds) == 2
    assert m1 in mthds
    assert m2 in mthds
    assert "hi" not in mthds
    assert m3 not in mthds
    assert m4 not in mthds

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

    class_str = c1.get_name() + '\n\tFields:' + '\n\t\t%s' % str(fld) + '\n\tMethods:' + '\n\t\t%s' % str(mthd)

    assert str(c1) == class_str
    assert str(c1) != "Roger"
