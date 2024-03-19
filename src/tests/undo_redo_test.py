from Models.uml_diagram import UML_Diagram
from Models.uml_undo_redo import UML_States
from Models.uml_save_load import diagram_to_json, json_to_diagram

def test_undo_redo():
    diagram = UML_Diagram()
    states = UML_States()
    states.save_state(diagram)
    diagram.add_class('Class1')
    states.save_state(diagram)
    diagram.add_class('Class2')
    states.save_state(diagram)
    diagram.add_class('Class3')
    states.save_state(diagram)
    diagram.add_relation('Class1', 'Class2', 'aggregation')
    states.save_state(diagram)
    diagram.add_relation('Class1', 'Class3', 'composition')
    states.save_state(diagram)
    diagram.add_relation('Class2', 'Class3', 'inheritance')
    states.save_state(diagram)
    diagram.add_relation('Class3', 'Class1', 'association')
    states.save_state(diagram)
    diagram.add_relation('Class3', 'Class2', 'dependency')
    states.save_state(diagram)

    assert diagram == states.undo()



