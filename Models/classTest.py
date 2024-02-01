import unittest
import addclass
from addclass import UMLClass

class TestClass(unittest.TestCase):

    def setUp(self):
        self.classname = UMLClass()

    def test_addclass(self):
        result = self.classname.addclass('Students')
        self.assertEqual(result,'Students')


    """
    def test_exisitingclass(self):
        self.classname.addclass('Students')
    """


    #test for rename class

    def test_renameclass(self):
        self.classname.addclass('Student')
        result = self.classname.rename('Student', 'Manager')

    

    def test_deleteclass(self):
        result = self.classname.delectClass('Student')
        self.assertEqual(result,'Student')

"""
    def test_listclasses(self):
        self.classname.addclass('Students')
        self.classname.addclass('MID')
        self.classname.addclass('Grade')
        existclass = self.classname.listclass()
        expected = {
            "Students": {},
            "MID":      {},
            "Grade":    {}
        }
        self.assertDictEqual(existclass, expected)
    """
if __name__ == '__main__':
    unittest.main()