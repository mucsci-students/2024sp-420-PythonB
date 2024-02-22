from Models.classadd import UMLClass
from Models.diagram import Diagram
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


# test for rename class
def test_rename_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Classes')
    with not pytest.raises(TypeError):
        test_class.rename_class('Classes', 'Schools')


def test_rename_class_not_exist(self):
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    with pytest.raises(TypeError):
        test_class.rename_class('Employees', 'Managers')


def test_rename_to_duplicate_name(self):
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Class1')
    test_class.add_class('Class2')
    with pytest.raises(TypeError):
        test_class.rename_class('Class1', 'Class2')


def test_delete_class(self):
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Managers')
    with pytest.raises(TypeError):
        test_class.delete_class('Managers')


def test_delete_class_not_exist(self):
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    with pytest.raises(TypeError):
        test_class.delete_class('Grade')


def test_delete_classrelationship(self):
    self.classname.add_class('Teacher')
    result = self.classname.delete_class('Teacher')
    self.assertEqual(result, 'Teacher')


def test_listclasses(self):
    self.classname.add_class('Students')
    self.classname.add_class('MID')
    self.classname.add_class('Grade')
    exist_class = self.classname.list_class()
    expected = {
        "Students": [],
        "MID": [],
        "Grade": []
    }
    self.assertDictEqual(exist_class, expected)
