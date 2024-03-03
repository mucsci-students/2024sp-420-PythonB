#Primary: Danish
from Models.classadd import UMLClass
from Models.attribute import Methods, Parameters
from Models.diagram import Diagram
import pytest


@pytest.fixture
def setup():
    diagram = Diagram()
    classes = UMLClass(diagram)
    classes.add_class("CSCI")
    methods = Methods(diagram)
    methods.add_method("CSCI", "420")
    parameters = Parameters(methods)
    return parameters


def test_add_parameter(setup):

    setup.add_parameters("CSCI", "420", "Quiz1")
    for method_dict in setup.method_class.diagram_class.classes["CSCI"]['Methods']:
        if "420" in method_dict:
            assert "Quiz1" in method_dict["420"]['Parameters']

    with pytest.raises(ValueError):
        setup.add_parameters("CSCI", "Invalid Method", "Quiz1")


def test_add_duplicate_parameter(setup):

    setup.add_parameters("CSCI", "420", "Quiz1")
    for method_dict in setup.method_class.diagram_class.classes["CSCI"]['Methods']:
        if "420" in method_dict:
            assert "Quiz1" in method_dict["420"]['Parameters']

    with pytest.raises(ValueError):
        setup.add_parameters("CSCI", "420", "Quiz1")


def test_delete_parameter(setup):
    setup.add_parameters("CSCI", "420", "Quiz1")
    setup.delete_parameters("CSCI", "420", "Quiz1")
    for method_dict in setup.method_class.diagram_class.classes["CSCI"]['Methods']:
        if "420" in method_dict:
            assert "Quiz1" not in method_dict["420"]['Parameters']

    with pytest.raises(ValueError):
        setup.delete_parameters("CSCI", "420", "nonExistant")


def test_delete_all_parameter_nonexistent_class(setup):
    with pytest.raises(ValueError):
        setup.delete_all_parameters("NonExistentClass", "420")


def test_delete_all_parameter_nonexistent_method(setup):
    with pytest.raises(ValueError):
        setup.delete_all_parameters("CSCI", "NonExistentMethod")

def test_change_parameter(setup):
    setup.add_parameters("CSCI", "420", "Quiz1")
    setup.change_parameters("CSCI", "420", "Quiz1", "Quiz2")
    for method_dict in setup.method_class.diagram_class.classes["CSCI"]['Methods']:
        if "420" in method_dict:
            assert "Quiz2" in method_dict["420"]['Parameters']


def test_change_nonexistant_parameter(setup):
    setup.add_parameters("CSCI", "420", "Quiz")
    with pytest.raises(ValueError):
        setup.change_parameters("CSCI", "420", "Nonexistant", "Quiz2")
