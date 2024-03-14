import unittest
from Models.attribute import Attributes
from Models.addclass import UMLClass
from Models.diagram import Diagram


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.diagram = Diagram()
        self.diagram.classes.update({"Students": []})
        self.diagram.classes["Students"].append("student1")
        self.diagram.classes["Students"].append("student2")
        self.attributes = Attributes(self.diagram)

    def test_add_attribute(self):
        # Class exists. Add should be successful, so should return True.
        self.assertEqual(self.attributes.add_attribute("Katie", "Students"), True)
        # Class doesn't exist. Add should fail, so should return False.
        self.assertEqual(self.attributes.add_attribute("Katie", "Classes"), False)

    def test_delete_attribute(self):
        # Attribute and class both exist. Delete should be successful, so should return True.
        self.assertEqual(self.attributes.delete_attribute("student1", "Students"), True)
        # Class exists, but attribute doesn't. Delete should fail, so should return False.
        self.assertEqual(self.attributes.delete_attribute("student3", "Students"), False)
        # Class doesn't exist. Delete should fail, so should return False.
        self.assertEqual(self.attributes.delete_attribute("student2", "Classes"), False)

    def test_rename_attribute(self):
        # Class and old name both exist. Rename should be successful, so should return True.
        self.assertEqual(self.attributes.rename_attribute("student2", "student1", "Students"), True)
        # Class exists, but old name doesn't. Rename should fail, so should return False.
        self.assertEqual(self.attributes.rename_attribute("student3", "student2", "Students"), False)
        # Class doesn't exist. Rename should fail, so should return False.
        self.assertEqual(self.attributes.rename_attribute("student1", "student2", "Classes"), False)


if __name__ == '__main__':
    unittest.main()
