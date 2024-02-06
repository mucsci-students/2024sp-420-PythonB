import unittest
from Models.addclass import UMLClass


class TestClass(unittest.TestCase):

    def setUp(self):
        self.classname = UMLClass()

    def test_add_class(self):
        result = self.classname.add_class('Students')
        self.assertEqual(result, 'Students')

    def test_existing_class(self):
        result = self.classname.add_class('Students')
        self.assertEqual(result, 'Students')

    """
    def test_empty_class(self):
        result = self.classname.add_class('')
        self.assertEqual(result, '')
    """
    # test for rename class
    def test_rename_class(self):
        self.classname.add_class('Student')
        self.classname.rename_class('Student', 'Manager')

    def test_delete_class(self):
        result = self.classname.delete_class('Student')
        self.assertEqual(result, 'Student')

    def test_listclasses(self):
        self.classname.add_class('Students')
        self.classname.add_class('MID')
        self.classname.add_class('Grade')
        exist_class = self.classname.list_class()
        expected = {
            "Students": [],
            "MID":      [],
            "Grade":    []
        }
        self.assertDictEqual(exist_class, expected)


if __name__ == '__main__':
    unittest.main()
