# Zhang
# Feb 22,2024
from Models.diagram import Diagram
from Models.relationship import UMLRelationship
from Models.classadd import UMLClass
import pytest


@pytest.fixture
def setup():
    diagram = Diagram()
    classes = UMLClass(diagram)
    classes.add_class('Source')
    classes.add_class('Destination')
    relationships = UMLRelationship(classes)
    return relationships


def test_valid_inputs(setup):
    setup.add_relationship('Source', 'Destination', 'Aggregation')
    assert ['Source', 'Destination', 'Aggregation'] in setup.relationships


def test_invalid_source_destination(setup):
    with pytest.raises(ValueError):
        setup.add_relationship('InvalidSource', 'Destination', 'Aggregation')

    with pytest.raises(ValueError):
        setup.add_relationship('Source', 'InvalidDestination', 'Aggregation')

    with pytest.raises(ValueError):
        setup.add_relationship('Source', 'Source', 'Aggregation')


def test_invalid_relationship_type(setup):
    with pytest.raises(ValueError):
        setup.add_relationship('Source', 'Destination', 'InvalidType')


def test_duplicate_relationship(setup):
    setup.add_relationship('Source', 'Destination', 'Aggregation')
    with pytest.raises(ValueError):
        setup.add_relationship('Source', 'Destination', 'Aggregation')


def test_delete_relationship(setup):
    setup.add_relationship('Source', 'Destination', 'Aggregation')
    setup.delete_relationship('Source', 'Destination')
    assert ['Source', 'Destination', 'Aggregation'] not in setup.relationships


def test_delete_non_existing_relationship(setup):
    with pytest.raises(ValueError):
        setup.delete_relationship('Source', 'Destination')


def test_delete_all_relationships_for_removed_classes(setup):
    setup.add_relationship('Source', 'Destination', 'Aggregation')
    setup.removed_class('Source')
    assert ['Source', 'Destination', 'Aggregation'] not in setup.relationships


def test_update_class_names_in_relationship_list(setup):
    setup.add_relationship('Source', 'Destination', 'Aggregation')
    setup.renamed_class('Source', 'SourceNew')
    assert ['SourceNew', 'Destination', 'Aggregation'] in setup.relationships


def test_update_types(setup):
    setup.add_relationship("Source", "Destination", "Aggregation")
    setup.update_types("Source", "Destination", "Composition")
    assert ["Source", "Destination", "Composition"] in setup.relationships

    with pytest.raises(ValueError):
        setup.update_types("Source", "Destination", "InvalidType")
