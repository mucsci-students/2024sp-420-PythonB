from Models.classadd import UMLClass
from Models.diagram import Diagram
import pytest


def test_add_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    with not pytest.raises(TypeError):
        test_class.add_class('Students')


def test_add_class_error():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    with pytest.raises(TypeError):
        test_class.add_class('')


def test_add_existing_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    result = test_class.add_class('Students')
    assert result == 'Students'


def test_add_empty_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    result = test_class.add_class('')
    assert result == None


# test for rename class
def test_rename_class():
    test_diagram = Diagram()
    test_class = UMLClass(test_diagram)
    test_class.add_class('Student')
    test_class.rename_class('Student', 'Manager')


def test_rename_NotExist(self):
    self.classname.rename_class('Student', 'Manager')


def test_rename_To_reservedWord(self):
    self.classname.add_class('Student')
    self.classname.rename_class('Student', 'class')


def test_rename_Exist(self):
    self.classname.add_class('Student')
    self.classname.add_class('MID')
    self.classname.rename_class('Student', 'MID')


def test_delete_class(self):
    self.classname.add_class('Student')
    result = self.classname.delete_class('Student')
    self.assertEqual(result, 'Student')


def test_delete_class_notExist(self):
    result = self.classname.delete_class('Grade')
    self.assertEqual(result, 'Grade')


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
