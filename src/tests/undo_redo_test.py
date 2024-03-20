from ..Models.uml_diagram import UML_Diagram
from ..Models.uml_undo_redo import UML_States
from ..Models.uml_save_load import diagram_to_json, json_to_diagram

def test_initial_state():
    uml_diagram = UML_Diagram()
    uml_states = UML_States(uml_diagram)

    # The initial state should be empty
    uml_diagram_afer_undo = uml_states.undo()
    assert len(uml_diagram_afer_undo.get_all_classes()) == 0

def test_save_and_undo():
    uml_diagram = UML_Diagram()
    uml_states = UML_States(uml_diagram)

    initial_state = uml_states.undo()
    assert len(initial_state.get_all_classes()) == 0

    # Add a class and save the state
    uml_diagram.add_class("Class1")
    uml_states.save_state(uml_diagram)

    # Undo to revert back to the initial state
    uml_diagram_afer_undo = uml_states.undo()
    assert len(uml_diagram_afer_undo.get_all_classes()) == 0

def test_save_and_redo():
    uml_diagram = UML_Diagram()
    uml_states = UML_States(uml_diagram)

   # Add a class and save the state
    uml_diagram.add_class("Class1")
    uml_states.save_state(uml_diagram)
    
    # Undo to revert back to the initial state
    uml_states.undo()

    # Redo to revert back to the state after the save
    uml_diagram_after_redo = uml_states.redo()
    assert len(uml_diagram_after_redo.get_all_classes()) == 1
    assert uml_diagram_after_redo.get_all_classes()[0].get_name() == "Class1"