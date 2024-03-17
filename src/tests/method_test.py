from ..Models.uml_method import UML_Method
from ..Models.uml_param import UML_Param as param

def test_ctor():
    t = UML_Method("Shaggy", "void")
    u = UML_Method("Matt", "int")
    v = UML_Method("Velma","void", "test1", "test2", "test3")

    assert t._name == "Shaggy"
    assert t._ret == "void"
    assert t._name != "Matt" 
    assert t._name != "Peetuh" 

    assert u._name == "Matt" 
    assert u._ret == "int"
    assert u._ret != "void"
    #TODO: Uncomment these when the params are added deterministically
    # assert str(param("test1")) == str(v._params[0])
    # assert str(param("test2")) == str(v._params[1])
    # assert str(param("test3")) == str(v._params[2])

#===================================== Accessors =====================================#

def test_get_name():
    a = UML_Method("Test", "int", "p1", "p2")
    b = UML_Method("Test", "void", "Branch", "Leaf")
    c = UML_Method("Same", "Same", "Same", "Same", "Samey")

    assert a.get_name() == "Test"
    assert a.get_name() != "Marvin Gaye"

    assert b.get_name() == "Test"
    assert b.get_name() != "Johnny Cash"

    assert c.get_name() == "Same"
    assert c.get_name() != "Bon Jovi"

def test_get_ret():
    a = UML_Method("Test", "int", "p1", "p2")
    b = UML_Method("Test", "void", "Branch", "Leaf")
    c = UML_Method("Same", "Same", "Same", "Same", "Samey")

    assert a.get_ret() == "int"
    assert a.get_ret() != "void"

    assert b.get_ret() == "void"
    assert b.get_ret() != "int"

    assert c.get_ret() == "Same"
    assert c.get_ret() != "Different"

def test_get_param():
    a = UML_Method("Test", "int", "p1", "p2")
    b = UML_Method("Test", "void", "Branch", "Leaf")

    assert str(a.get_param("p1")) == "p1"
    assert str(b.get_param("Leaf")) == "Leaf"

def test_get_params():
    a = UML_Method("Test", "int", "p1", "p2")
    b = UML_Method("Test", "void", "Branch", "Leaf")
    c = UML_Method("Same", "Same", "Same", "Same", "Samey")

    assert a.get_params() == a._params
    assert a.get_params() != b.get_params()

    assert b.get_params() == b._params
    assert b.get_params() != c.get_params()

    assert c.get_params() == c._params
    assert c.get_params() != a.get_params()

#===================================== Mutators =====================================#   

def test_set_name():
    a = UML_Method("Test", "int", "p1", "p2")

    a.set_name("Zynga")
    assert a.get_name() == "Zynga"
    assert a.get_name() != "Supercell"

def test_set_ret():
    a = UML_Method("Test", "int", "p1", "p2")
    a.set_ret("UML_Hearse")

    assert a.get_ret() == "UML_Hearse"
    assert a.get_ret() != "UML_Hospital"

def test_add_param():
    a = UML_Method("Test", "int", "p1", "p2")
    a.add_param("p3cO")

    assert str(param("p3cO")) == str(a._params[2])

def test_delete_param():
    a = UML_Method("Test", "int", "p1", "p2")
    a.delete_param("p1")

    assert str(param("p1")) != str(a._params[0])
    assert str(param("p2")) == str(a._params[0])

def test_change_params():
    a = UML_Method("Test", "int", "p1", "p2")

    a.change_params("Gorillaz", "De La Soul")

    assert str(a.get_param("Gorillaz")) == "Gorillaz"
    assert str(a.get_param("De La Soul")) == "De La Soul"
    assert len(a.get_params()) == 2


def test_append_params():
    a = UML_Method("Test", "int", "p1", "p2")
    a.append_params("Gorillaz", "De La Soul")

    assert len(a.get_params()) == 4
    #TODO: Fix once append params is deterministic
    # assert str(param("p1")) == str(a._params[0])
    # assert str(param("p2")) == str(a._params[1])
    # assert str(param("Gorillaz")) == str(a._params[2])
    # assert str(param("De La Soul")) == str(a._params[3])

#===================================== Operators =====================================#

def test_eq():
    a = UML_Method("Test", "int", "p1", "p2")
    b = UML_Method("Test", "void", "Branch", "Leaf")
    c = UML_Method("Same", "Same", "Same", "Same", "Samey")
    d = UML_Method("Same", "Same", "Same", "Samey")

    assert c == d
    assert a != c
    assert b != d
    assert d == c
    assert d != 1
    assert a != "General Kenobi!"

def test_str():
    c = UML_Method("Same", "Same", "Same", "Same", "Samey")

    assert len(str(c)) == len("Same\nSame (Samey, Same)")
    assert str(c) != "Tim forgot to test string in UML_Field"
