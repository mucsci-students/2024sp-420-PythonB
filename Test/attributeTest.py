import unittest
from Models.attribute import Attributes
from Models.diagram import Diagram
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.attributes = Attributes()
        self.diagram = Diagram()
        self.diagram.update("Student", [])
        self.diagram.update("Class", ["attribute", "attribute2", "attribute3", "attribute4"])

    def test_add_attribute(self):
        # Katie Dowlin: Valid name that starts with a letter, class_name that exists.
        result = self.attributes.add_attribute("Katie", "Student")
        self.assertEqual(result, "Katie")
        # Katie Dowlin: Name that is reserved keyword, class_name that exists.
        result2 = self.attributes.add_attribute("for", "Student")
        self.assertEqual(result2, "for")
        # Katie Dowlin: Name that is not a string, class_name that exists.
        result3 = self.attributes.add_attribute(4, "Student")
        self.assertEqual(result3, 4)
        # Katie Dowlin: Name that contains special characters, class_name that exists.
        result4 = self.attributes.add_attribute("*&$&*#", "Student")
        self.assertEqual(result4, "*&$&*#")
        # Katie Dowlin: Valid name that starts with an _, class_name that exists.
        result5 = self.attributes.add_attribute("_Katie", "Student")
        self.assertEqual(result5, "_Katie")
        # Katie Dowlin: Name that starts with a number, class_name that exists.
        result6 = self.attributes.add_attribute("4abc", "Student")
        self.assertEqual(result6, "4abc")
        # Katie Dowlin: Name is the empty string, class_name that exists.
        result7 = self.attributes.add_attribute("", "Student")
        self.assertEqual(result7, "")
        # Katie Dowlin: Trying to add a duplicate name into a class that exists.
        result8 = self.attributes.add_attribute("attribute", "Class")
        self.assertEqual(result8, "attribute")
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
