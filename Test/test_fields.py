import pytest
from Models.attribute import Fields
from Models.classadd import UMLClass
from Models.diagram import Diagram


def test_add_field():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    test_class.add_class('Students')
    test_field.add_field('Students', 'Katie')
    assert 'Katie' in test_class.classes['Students']['Fields']


def test_add_duplicate_field():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    test_class.add_class('Students')
    test_field.add_field('Students', 'Katie')
    with pytest.raises(ValueError):
        test_field.add_field('Students', 'Katie')


def test_add_field_class_not_exist():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    with pytest.raises(ValueError):
        test_field.add_field('Test', 'test1')


def test_rename_field():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    test_class.add_class('Students')
    test_field.add_field('Students', 'Katie')
    test_field.rename_field('Students', 'Katie', 'Jillian')
    assert 'Katie' not in test_class.classes['Students']['Fields']
    assert 'Jillian' in test_class.classes['Students']['Fields']


def test_rename_field_not_exist():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    test_class.add_class('Students')
    with pytest.raises(ValueError):
        test_field.rename_field('Students', 'student1', 'student2')


def test_rename_to_duplicate_name():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    test_class.add_class('Classes')
    test_field.add_field('Classes', 'CSCI366')
    test_field.add_field('Classes', 'CSCI420')
    with pytest.raises(ValueError):
        test_field.rename_field('Classes', 'CSCI366', 'CSCI420')


def test_rename_field_class_not_exist():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    with pytest.raises(ValueError):
        test_field.rename_field('Test', 'test1', 'test2')


def test_delete_field():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    test_class.add_class('Classes')
    test_field.add_field('Classes', 'CSCI420')
    test_field.delete_field('Classes', 'CSCI420')
    assert 'CSCI420' not in test_class.classes['Classes']['Fields']


def test_delete_field_not_exist():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    test_class.add_class('Classes')
    with pytest.raises(ValueError):
        test_field.delete_field('Classes', 'CSCI545')


def test_delete_field_class_not_exist():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_field = Fields(test_class)
    with pytest.raises(ValueError):
        test_field.delete_field('Test', 'test1')
