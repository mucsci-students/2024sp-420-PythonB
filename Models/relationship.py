from Models.errorHandler import ErrorHandler


class UMLRelationship:

    # Interacting with UMLClass
    #
    def __init__(self, classes):
        """
        Initializes the UMLRelationship instance.

        Parameters:
            classes (dictionary): A dictionary of class names.

        Precondition:
            'classes' should be a non-empty.

        Postcondition:
            Initializes 'uml_class' with the given dictionary of classes, 'relationships' with an empty list, and
        'relationship_types' with a list of predefined types.

        Returns:
            None
        """

        self.uml_class = classes
        self.relationships = []
        self.relationship_types = ["Aggregation", "Composition", "Generalization", "Inheritance"]

    def add_relationship(self, src, des, type_rel):
        """
        Adds a new relationship if it's valid and doesn't already exist.

        Parameters:
            src (str): The source class name.
            des (str): The destination class name.
            type_rel (str): The type of relationship.

        Precondition:
            Both 'src' and 'des' must exist in 'uml_class', 'type_rel' must be in 'relationship_types', and 'src'
        should not be equal to 'des'.

        Postcondition:
            Adds a new relationship to 'relationships' if all conditions are met.

        Returns:
            None
        """

        # Check the existent of the source class.
        if src not in self.uml_class.classes:
            raise ValueError(f"Source class, '{src}' does not exist.")

        # Check the existent of the destination class.
        elif des not in self.uml_class.classes:
            raise ValueError(f"Destination class, '{des}' does not exist.")

        # Check the validation of the relationship types.
        elif type_rel not in self.relationship_types:
            raise ValueError(f"Relationship type, '{type_rel}' is not valid.")

        # Relationship can't be created by the same class.
        elif src == des:
            raise ValueError(f"The source class, '{src}', cannot be the same as the destination class.")

        else:
            # Check the existent of the relationship.
            found = False
            for rel in self.relationships:
                if rel[0] == src and rel[1] == des:
                    found = True
            if found:
                raise ValueError(f"Relationship from '{src}' to '{des}' already exists.")
            else:
                # Append to the new relationship to the list.
                self.relationships.append([src, des, type_rel])
                return("Relationship added.")

    def delete_relationship(self, src, des):
        """
        Deletes an existing relationship between the specified source and destination classes.

        Parameters:
            src (str): The source class name.
            des (str): The destination class name.

        Precondition:
            A relationship between 'src' and 'des' must exist in 'relationships'.

        Postcondition:
            The specified relationship is removed from 'relationships'.

        Returns:
            None
        """

        # Check the existent of the source class.
        if src not in self.uml_class.classes:
            raise ValueError(f"Source class- '{src}' does not exist.")

        # Check the existent of the destination.
        elif des not in self.uml_class.classes:
            raise ValueError(f"Destination class- '{des}' does not exist.")

        removed = False
        # For each relationship tuple in the list, if relationship exist, remove it.
        for rel in self.relationships[:]:
            if rel[0] == src and rel[1] == des:
                self.relationships.remove(rel)
                removed = True

        # Show error message if relationship exists.
        if not removed:
            raise ValueError(f"No relationship from '{src}' to '{des}' exists.")
        else:
            return("Relationship deleted!")

    # When a class is deleted, remove all its relationships
    def removed_class(self, removed_class):
        """
        Removes all relationships involving a specified class when it's removed.

        Parameters:
            removed_class (str): The name of the class being removed.

        Precondition:
            'removed_class' should exist in 'uml_class'.

        Postcondition:
            All relationships involving 'removed_class' are removed from 'relationships'.

        Returns:
            None
        """

        removed = False

        # Remove the relationship for each removed source or destination class.
        for rel in self.relationships[:]:
            if rel[0] == removed_class or rel[1] == removed_class:
                self.relationships.remove(rel)
                removed = True
        if removed:
            return("Relationship removed.")

    def renamed_class(self, old_name, new_name):
        """
        Updates relationships to reflect a class name change.

        Parameters:
            old_name (str): The current class name.
            new_name (str): The new class name.

        Precondition:
            'old_name' should exist in 'uml_class' and 'new_name' should not already exist in 'uml_class'.

        Postcondition:
            All relationships involving 'old_name' are updated to use 'new_name'.

        Returns:
            None
        """

        renamed = False

        # Update each renamed source or destination class in the relationship list.
        for rel in self.relationships[:]:
            if rel[0] == old_name:
                rel[0] = new_name
                renamed = True
            if rel[1] == old_name:
                rel[1] = new_name
                renamed = True
        if renamed:
            return("Relationship renamed.")

    def update_types(self, src, des, new_type):
        """
        Changes the type of existing relationship.

        Parameters:
            src (str): The source class name.
            des (str): The destination class name.
            new_type (str): The new type of the relationship.

        Precondition:
            A relationship between 'src' and 'des' class must exist, and the 'new_type' must be in
        the 'relationship_types'.

        Postcondition:
            The type of the specified relationship is updated to 'new_type'.

        Returns:
            None
        """

        if new_type not in self.relationship_types:
            raise ValueError("Invalid relationship type!")
        else:
            valid_src_des = False
            for rel in self.relationships[:]:
                if rel[0] == src and rel[1] == des:
                    rel[2] = new_type
                    valid_src_des = True

            if not valid_src_des:
                raise ValueError(f"{src} and {des} do not currently have relationships.")
            else:
                return(f"The relationship type from {src} to {des} have been updated.")

    def list_relationship_types(self):
        """
        Returns all predefined relationship types.

        Precondition:
            None

        Postcondition:
            Returns 'relationships_types'.

        Returns:
            list: A list of all relationships types.
        """
        return self.relationship_types

    # prints list of lists of relationships
    def list_relationships(self):
        """
        Returns a list of all current relationships.

        Precondition:
            None

        Postcondition:
            Returns the current scene of 'relationships'.

        Returns:
            list: A list of all relationships, each formatted as [source, destination, type].
        """
        return self.relationships


if __name__ == "__main__":

    help(UMLRelationship)
    # help(UMLRelationship.add_relationship)
