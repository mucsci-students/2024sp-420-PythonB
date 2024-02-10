import unittest
from Models.attribute import Attributes
from Models.addclass import UMLClass
from Models.diagram import Diagram
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.attributes = Attributes()
        self.diagram = Diagram()
        self.umlclass = UMLClass()
        self.umlclass.add_class("Students")
        self.diagram.classes["Students"].append("student1")


    def test_add_attribute(self):
        # Katie Dowlin: Class exists. Expected return value: "Katie"
        result = self.attributes.add_attribute("Katie", "Student")
        self.assertEqual(result, "Katie")
        # Katie Dowlin: Valid name, class_name doesn't exist.
        result9 = self.attributes.add_attribute("name", "Imaginary")
        self.assertEqual(result9, "name")


    def test_delete_attribute(self):
        # Katie Dowlin: Both name and class_name exist.
        result = self.attributes.delete_attribute("attribute2", "Class")
        self.assertEqual(result, "attribute2")
        # Katie Dowlin: Name doesn't exist, class_name exists.
        result2 = self.attributes.delete_attribute("hello", "Class")
        self.assertEqual(result2, "hello")
        # Katie Dowlin: Class_name doesn't exist.
        result3 = self.attributes.delete_attribute("attribute", "Imaginary")


    def test_rename_attribute(self):
        # Katie Dowlin: Class_name exists, old_name exists, new_name is valid
        result = self.attributes.rename_attribute("attribute", "attribute1", "Class")
        self.assertEqual(result, "attribute1")
        # Katie Dowlin: Class_name exists, old_name exists, new_name is not valid
        result2 = self.attributes.rename_attribute("attribute3", "for", "Class")
        self.assertEqual(result2, "attribute3")
        # Katie Dowlin: Class_name exists, old_name doesn't exist
        result3 = self.attributes.rename_attribute("attribute5", "attribute6", "Class")
        self.assertEqual(result3, "attribute5")
        # Katie Dowlin: Class_name doesn't exist
        result4 = self.attributes.rename_attribute("hello", "goodbye", "Imaginary")
        self.assertEqual(result4, "hello")


if __name__ == '__main__':
    unittest.main()
