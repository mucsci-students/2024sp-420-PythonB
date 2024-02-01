import unittest

from Models.addclass import UMLClass


class TestClass(unittest.TestCase):

    def setUp(self):
        self.classname = UMLClass()

    def test_add_class(self):
        result = self.classname.addclass('Student')
        self.assertEqual(result,'Student')

    def test_rename_class(self):
        self.classname.addclass('Student')
        self.classname.rename('Student', 'Manager')
        print("rename class test passed")

    def test_delete_class(self):
        result = self.classname.deleteClass('Student')
        self.assertEqual(result, 'Student')
        print("delete class test passed")


if __name__ == '__main__':
    unittest.main()
