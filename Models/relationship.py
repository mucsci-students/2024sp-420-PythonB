# Primary: Zhang
# secondary : Danish
# Feb 9,2024
from Models.classadd import UMLClass


class UMLRelationship:

    # Zhang: Interacting with UMLClass
    # Zhang: Note that the data structure of relationship is a list of lists:
    def __init__(self, classes):
        self.uml_class = classes
        self.relationships = []
        self.relationship_types = ["Aggregation", "Composition", "Generalization", "Inheritance"]

    '''add_relationship function.'''
    def add_relationship(self, src, des, type_rel):

        # Zhang: Check the existent of the source class.
        if src not in self.uml_class.classes:
            raise ValueError(f"Source class, '{src}' does not exist.")

        # Zhang: Check the existent of the destination class.
        if des not in self.uml_class.classes:
            raise ValueError(f"Destination class, '{des}' does not exist.")

        # Zhang: Check the validation of the relationship types.
        if type_rel not in self.relationship_types:
            raise ValueError(f"Relationship type: '{type_rel}' is not valid.")

        # Zhang: Relationship can't be created by the same class.
        if src == des:
            raise ValueError(f"The source class, '{src}', cannot be the same as the destination class.")

        else:
            # Zhang: Check the existent of the relationship.
            found = False
            for rel in self.relationships:
                if rel[0] == src or rel[1] == des:
                    found = True
            if found:
                raise ValueError(f"Relationship from '{src}' to '{des}' already exists.")
            else:
                # Zhang: Append to the new relationship to the list.
                self.relationships.append([src, des, type_rel])
                print("relationship added!")

    '''delete_relationship'''
    def delete_relationship(self, src, des):

        # Zhang: Check the existent of the source class.
        if src not in self.uml_class.classes:
            raise ValueError(f"Source class, '{src}' does not exist.")

        # Zhang: Check the existent of the destination.
        if des not in self.uml_class.classes:
            raise ValueError(f"Destination class, '{des}' does not exist.")

        removed = False
        # Zhang: For each relationship tuple in the list, if relationship exist, remove it.
        for rel in self.relationships[:]:
            if rel[0] == src and rel[1] == des:
                self.relationships.remove(rel)
                removed = True

        # Zhang: Show error message if relationship exists.
        if not removed:
            raise ValueError(f"No relationship from '{src}' to '{des}' exists.")
        else:
            print("Relationship deleted!")

    '''removed_class'''
    # Zhang: When a class is deleted, remove all its relationships
    def removed_class(self, removed_class):
        removed = False

        # Zhang: Remove the relationship for each removed source or destination class.
        for rel in self.relationships[:]:
            if rel[0] == removed_class or rel[1] == removed_class:
                self.relationships.remove(rel)
                removed = True
        if removed:
            print("Relationship removed!")

    '''renamed_class'''
    def renamed_class(self, old_name, new_name):
        renamed = False

        # Zhang: Update each renamed source or destination class in the relationship list.
        for rel in self.relationships[:]:
            if rel[0] == old_name:
                rel[0] = new_name
                renamed = True
            if rel[1] == old_name:
                rel[1] = new_name
                renamed = True
        if renamed:
            print("relationship renamed!")
