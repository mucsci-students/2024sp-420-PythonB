import unittest
from Models.attribute import Attributes
from Models.addclass import UMLClass
from Models.diagram import Diagram


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.attributes = Attributes(self.classes)
        self.classes = UMLClass()
        #self.umlclass.add_class("Students")
        diagram.classes.update({"Students": []})
        diagram.classes["Students"].append("student1")
        diagram.classes["Students"].append("student2")

    def test_add_attribute(self):
        # Katie Dowlin: Class exists. Add should be successful, so name should be in the list of attributes
        # in that class.
        self.attributes.add_attribute("Katie", "Students")
        self.assertIn(self.diagram.classes["Students"], "Katie")
        # Katie Dowlin: Class doesn't exist. Add should fail, so should receive a value error.
        self.assertRaises(ValueError, self.attributes.add_attribute, "Katie", "Class")

    def test_delete_attribute(self):
        # Katie Dowlin: Attribute and class both exist. Delete should be successful, so name should not be in
        # the list of attributes in that class.
        self.attributes.delete_attribute("student1", "Students")
        self.assertNotIn(self.diagram.classes["Students"], "student1")
        # Katie Dowlin: Class exists, but attribute doesn't. Delete should fail, so should receive a value error.
        self.assertRaises(ValueError, self.attributes.delete_attribute, "student3", "Students")
        # Katie Dowlin: Class doesn't exist. Delete should fail, so should receive a value error.
        self.assertRaises(ValueError, self.attributes.delete_attribute, "student2", "Class")

    def test_rename_attribute(self):
        print(self.diagram.classes["Students"])
        # Katie Dowlin: Class and old name both exist. Rename should be successful, so the new name should be
        # in the list of attributes in that class and the old name should no longer be in the list.
        self.attributes.rename_attribute("student2", "student1", "Students")
        self.assertIn(self.diagram.classes["Students"], "student1")
        self.assertNotIn(self.diagram.classes["Students"], student2)
        # Katie Dowlin: Class exists, but old name doesn't. Rename should fail, so should receive a value error.
        self.assertRaises(ValueError, self.attributes.rename_attribute, "student3", "student2", "Students")
        # Katie Dowlin: Class doesn't exist. Rename should fail, so should receive a value error.
        self.assertRaises(ValueError, self.attributes.rename_attribute, "student1", "student2", "Class")


if __name__ == '__main__':
    unittest.main()
