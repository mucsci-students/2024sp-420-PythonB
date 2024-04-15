from Models.uml_named_object import UML_Named_Object
from Models.uml_visitor import UML_Visitable, UML_Visitor
import pytest

def test_UML_Named_Object():
    with pytest.raises(Exception) as E:
        UML_Named_Object("test")
    assert isinstance(E.value, TypeError)

def test_UML_Visitable():
    with pytest.raises(Exception) as E:
        UML_Visitable()
    assert isinstance(E.value, TypeError)

def test_UML_Visitor():
    with pytest.raises(Exception) as E:
        UML_Visitor()
    assert isinstance(E.value, TypeError)