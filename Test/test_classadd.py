from Models.classadd import UMLClass
from Models.diagram import Diagram
from Models.attribute import Fields
from Models.attribute import Methods
from Models.attribute import Parameters
import pytest


def test_add_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    with not pytest.raises(TypeError):
        test_class.add_class('Students')


def test_add_duplicate_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Duplicate')
    with pytest.raises(TypeError):
        test_class.add_class('Duplicate')


def test_rename_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Classes')
    with not pytest.raises(TypeError):
        test_class.rename_class('Classes', 'Schools')


def test_rename_class_not_exist():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    with pytest.raises(TypeError):
        test_class.rename_class('Employees', 'Managers')


def test_rename_to_duplicate_name():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Class1')
    test_class.add_class('Class2')
    with pytest.raises(TypeError):
        test_class.rename_class('Class1', 'Class2')


def test_delete_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Managers')
    with pytest.raises(TypeError):
        test_class.delete_class('Managers')


def test_delete_class_not_exist():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    with pytest.raises(TypeError):
        test_class.delete_class('Grade')


def test_listclasses():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Students')
    test_class.add_class('MID')
    test_class.add_class('Grade')
    expected = {'Students': [], 'MID': [], 'Grade': []}
    assert test_class.list_classes() == expected


def test_list_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_diagram, test_class)
    test_method = Methods(test_diagram, test_class)
    test_parameter = Parameters(test_method)
    test_class.add_class('CSCI420')
    test_field.add_field('Katie', 'CSCI420')
    test_field.add_field('Danish', 'CSCI420')
    test_field.add_field('Jillian', 'CSCI420')
    test_field.add_field('Patrick', 'CSCI420')
    test_field.add_field('Zhang', 'CSCI420')
    test_method.add_method('Project', 'CSCI420')
    test_parameter.add_parameter('due_date', 'Project')
    expected = {'CSCI420': {'Fields': ['Katie', 'Danish', 'Jillian', 'Patrick', 'Zhang'],
                            'Methods': [{'Project': {'Parameters': ['due_date']}}]}}
    assert test_class.list_class() == expected

def test_list_class_no_methods_fields_params():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('CSCI420')
    expected = {'CSCI420': {'Fields': [], 'Methods': []}}
    assert test_class.list_class() == expected
