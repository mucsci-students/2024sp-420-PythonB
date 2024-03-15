from Models.UML_Param import UML_Param as param



def test_ctor():
    p = param("Named")
    assert p._name == "Named"
    assert p._name != "x"
    assert isinstance(p, param)
    assert not isinstance(p, Exception)

p = param("Named")
q = param("")
r = param("Same")
s = param("Same")

def test_get_name():
    assert p.get_name() == "Named"
    assert q.get_name() == ""
    assert q.get_name() != "Zoinks!"

def test_set_name():
    p.set_name("Bazinga!")
    q.set_name("Geronimo!")

    assert p.get_name() == "Bazinga!"
    assert p.get_name() != "Named"
    assert q.get_name() == "Geronimo!"
    assert q.get_name() != ""

def test_eq():
    assert r == s
    assert r != p

def test_str():
    assert str(r) == "Same"
    #this was updated in test_set_name
    assert str(p) == "Bazinga!"
    assert str(p) != "Named"




