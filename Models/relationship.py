from classadd import UMLClass


class Relationship:

    # Zhang: Referring to the UMLClass
    # Zhang: Create relationship.
    # Zhang: Note that the data structure of relationship is a list of tuples:
    # [("source1","destination1","relationship type"),("source2","destination2","relationship type"),... ]
    def __init__(self, classes):
        self.classes = classes
        self.relationships = []

    # Zhang: add_relationship function takes source, destination and type of relationship as arguments.
    def add_relationship(self, src, des, type_rel):

        # Zhang: Check and see if source is in the classes' dictionary
        if src not in self.classes.classes:
            print(f"Source class '{src}' does not exist.")

        # Zhang: Check and see if destination is in the classes' dictionary.
        elif des not in self.classes.classes:
            print(f"Destination class '{des}' does not exist.")

        # Zhang: Check and see if the relationship tuple already exist in the list.
        found = False
        for rel in self.relationships:
            if rel[0] == src and rel[1] == des:
                found = True
        if found:
            print(f"Relationship from '{src}' to '{des}' already exists.")

        # Zhang: Append to the new relationship to the list.
        else:
            self.relationships.append((src, des, type_rel))
            print("relationship added!")

    # Zhang: delete_relationship function takes source, destination as arguments.
    def delete_relationship(self, src, des):
        
        removed = False

        # Zhang: For each relationship tuple in the list, if relationship exist, remove it.
        for rel in self.relationships[:]:
            if rel[0] == src and rel[1] == des:
                self.relationships.remove(rel)
                removed = True

        # Zhang: Show error message if relationship exists.
        if not removed:
            print(f"No relationship from '{src}' to '{des}' exists.")
        else:
            print("Relationship deleted!")


some_class = UMLClass()
relationship = Relationship(some_class)

some_class.add_class("123")
some_class.add_class("321")

relationship.add_relationship(src="123", des="321", type_rel="Relationship")
relationship.delete_relationship(src="123", des="321")
