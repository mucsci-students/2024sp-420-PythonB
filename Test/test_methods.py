from Models.attribute import Methods
from Models.classadd import UMLClass
from Models.diagram import Diagram
import pytest


@pytest.fixture
def setup():
    diagram = Diagram()
    classes = UMLClass(diagram)
    classes.add_class("CSCI")
    methods = Methods(classes)
    return methods


def test_add_method(setup):
    setup.add_method("CSCI", "Take_420")
    assert "Take_420" in setup.diagram_class.classes["CSCI"]["Methods"][0]

    with pytest.raises(ValueError):
        setup.add_method("InvalidClass", "Take_420")


def test_add_duplicate(setup):
    setup.add_method("CSCI", "Take_420")
    with pytest.raises(ValueError):
        setup.add_method("CSCI", "Take_420")


def test_delete_method(setup):
    setup.add_method("CSCI", "Take_420")
    setup.delete_method("CSCI", "Take_420")
    assert "Take_420" not in setup.diagram_class.classes["CSCI"]["Methods"]

    with pytest.raises(ValueError):
        setup.delete_method("CSCI", "NonExistent")


def test_rename_method(setup):
    setup.add_method("CSCI", "Take_420")
    setup.rename_method("CSCI", "Take_420", "Take_421")
    assert "Take_421" in setup.diagram_class.classes["CSCI"]["Methods"][0]


def test_rename_nonexistent_method(setup):
    setup.add_method("CSCI", "Take_420")
    with pytest.raises(ValueError):
        setup.rename_method("CSCI", "NonExistent", "Take_421")
