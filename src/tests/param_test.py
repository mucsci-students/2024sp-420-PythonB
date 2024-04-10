from ..Models.uml_param import UML_Param as param



def test_ctor():
    p = param("Named")
    assert p._name == "Named"
    assert p._name != "x"
    assert isinstance(p, param)
    assert not isinstance(p, Exception)

def test_get_name():
    p = param("Named")
    q = param("")

    assert p.get_name() == "Named"
    assert q.get_name() == ""
    assert q.get_name() != "Zoinks!"

def test_set_name():
    p = param("Named")
    q = param("")

    p.set_name("Bazinga!")
    q.set_name("Geronimo!")

    assert p.get_name() == "Bazinga!"
    assert p.get_name() != "Named"
    assert q.get_name() == "Geronimo!"
    assert q.get_name() != ""

def test_eq():
    r = param("Same")
    s = param("Same")
    p = param("Different")

    assert r == s
    assert r != p




