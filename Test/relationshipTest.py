import unittest
from Models.relationship import UMLRelationship
from Models.classadd import UMLClass


class TestRelationship(unittest.TestCase):
    def setUp(self):
        self.classes = UMLClass()
        self.classes.add_class('Source')
        self.classes.add_class('Destination')
        self.relationships = UMLRelationship(self.classes)

    '''The following tests are designed for the add_relationship function'''
    # Zhang: Test for valid inputs.
    def test_valid_inputs(self):
        self.relationships.add_relationship('Source', 'Destination', 'Aggregation')
        self.assertIn(['Source', 'Destination', 'Aggregation'], self.relationships.relationships)

    # Zhang:Test for invalid source.
    def test_invalid_source(self):
        self.assertRaises(ValueError, self.relationships.add_relationship, 'InvalidSource', 'Destination', 'Aggregation')

    # Zhang: Test for invalid destination.
    def test_invalid_destination(self):
        self.assertRaises(ValueError, self.relationships.add_relationship, 'Source', 'InvalidDestination', 'Aggregation')

    # Zhang: Test for undefined relationship type.
    def test_invalid_relationship_type(self):
        self.assertRaises(ValueError, self.relationships.add_relationship, 'Source', 'Destination', 'InvalidType')

    # Zhang: Test for the same source and destination.
    def test_same_source_destination(self):
        self.assertRaises(ValueError, self.relationships.add_relationship, 'Source', 'Source', 'Aggregation')

    # Zhang: Test for adding a duplicate relationship.
    def test_duplicate_relationship(self):
        self.relationships.add_relationship('Source', 'Destination', 'Aggregation')
        self.assertRaises(ValueError, self.relationships.add_relationship, 'Source', 'Destination', 'Aggregation')

    '''The following tests are designed for the delete_relationship function'''
    # Zhang: Test for deleting the existing relationship.
    def test_delete_relationship(self):
        self.relationships.add_relationship('Source', 'Destination', 'Aggregation')
        self.relationships.delete_relationship('Source', 'Destination')
        self.assertNotIn(['Source', 'Destination', 'Aggregation'], self.relationships.relationships)

    # Zhang: Test for deleting non-existing relationship.
    def test_delete_non_existing_relationship(self):
        self.assertRaises(ValueError, self.relationships.delete_relationship, 'Source', 'Destination')

    '''The following tests are designed for the removed_class function'''
    def test_delete_all_relationships_for_removed_classes(self):
        self.relationships.add_relationship('Source', 'Destination', 'Aggregation')
        self.relationships.removed_class('Source')
        self.assertNotIn(['Source', 'Destination', 'Aggregation'], self.relationships.relationships)

    '''The following tests are designed for the renamed_class function'''
    def test_update_class_names_in_relationship_list(self):
        self.relationships.add_relationship('Source', 'Destination', 'Aggregation')
        self.relationships.renamed_class('Source', 'SourceNew')
        self.assertIn(['SourceNew', 'Destination', 'Aggregation'], self.relationships.relationships)


if __name__ == '__main__':
    unittest.main()
