from Models.uml_method import UML_Method
from Models.uml_param import UML_Param as param

import pytest

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

    assert param("test1") == v._params[0]
    assert param("test2") == v._params[1]
    assert param("test3") == v._params[2]

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
    p1 = param('p1')
    p2 = param('Leaf')

    assert a.get_param("p1") == p1
    assert b.get_param("Leaf") == p2

    with pytest.raises(ValueError) as VE:
        a.get_param("badName")
    assert str(VE.value) == "No param with name badName exists"
        

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

    assert a.get_param("p3cO")
    assert len(a.get_params()) == 3

    with pytest.raises(ValueError) as VE:
        a.add_param("p3cO")
    assert str(VE.value) == "Param with name p3cO already exists"

def test_delete_param():
    a = UML_Method("Test", "int", "p1", "p2")
    a.delete_param("p1")

    assert param("p1") != a._params[0]
    assert param("p2") == a._params[0]

def test_change_params():
    a = UML_Method("Test", "int", "p1", "p2")
    p1 = param("Gorillaz")
    p2 = param("De La Soul")
    a.change_params("Gorillaz", "De La Soul")

    assert a.get_param("Gorillaz") == p1
    assert a.get_param("De La Soul") == p2
    assert len(a.get_params()) == 2


def test_append_params():
    a = UML_Method("Test", "int", "p1", "p2")
    a.append_params("Gorillaz", "De La Soul")

    assert len(a.get_params()) == 4
    assert a.get_param("p1")
    assert a.get_param("p2")
    assert a.get_param("Gorillaz")
    assert a.get_param("De La Soul")

    a.append_params("Gorillaz", "De La Soul")
    assert len(a.get_params()) == 4

#===================================== Operators =====================================#

def test_eq():
    a = UML_Method("Test", "int", "p1", "p2")
    b = UML_Method("Test", "void", "Branch", "Leaf")
    c = UML_Method("Same", "Same", "Same", "Same", "Samey")
    d = UML_Method("Same", "Same", "Same", "Samey")

    assert a == a
    assert c == d
    assert a != c
    assert b != d
    assert d == c
    assert d != 1
    assert a != "General Kenobi!"

