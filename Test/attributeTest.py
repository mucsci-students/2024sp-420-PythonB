import unittest
from Models.attribute import Attributes
from Models.diagram import Diagram


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.attributes = Attributes(self.classes)
        diagram.classes.update({"Students": []})
        diagram.classes["Students"].append("student1")
        diagram.classes["Students"].append("student2")

    def test_add_attribute(self):
        # Katie Dowlin: Class exists. Add should be successful, so should return True.
        self.assertEqual(self.attributes.add_attribute("Katie", "Students"), True)
        # Katie Dowlin: Class doesn't exist. Add should fail, so should return False.
        self.assertEqual(self.attributes.add_attribute("Katie", "Classes"), False)

    def test_delete_attribute(self):
        # Katie Dowlin: Attribute and class both exist. Delete should be successful, so should return True.
        self.assertEqual(self.attributes.delete_attribute("student1", "Students"), True)
        # Katie Dowlin: Class exists, but attribute doesn't. Delete should fail, so should return False.
        self.assertEqual(self.attributes.delete_attribute("student3", "Students"), False)
        # Katie Dowlin: Class doesn't exist. Delete should fail, so should return False.
        self.assertEqual(self.attributes.delete_attribute("student2", "Classes"), False)

    def test_rename_attribute(self):
        # Katie Dowlin: Class and old name both exist. Rename should be successful, so should return True.
        self.assertEqual(self.attributes.rename_attribute("student2", "student1", "Students"), True)
        # Katie Dowlin: Class exists, but old name doesn't. Rename should fail, so should return False.
        self.assertEqual(self.attributes.rename_attribute("student3", "student2", "Students"), False)
        # Katie Dowlin: Class doesn't exist. Rename should fail, so should return False.
        self.assertEqual(self.attributes.rename_attribute("student1", "student2", "Classes"), False)


if __name__ == '__main__':
    unittest.main()
