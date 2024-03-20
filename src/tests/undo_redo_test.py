from ..Models.uml_diagram import UML_Diagram
from ..Models.uml_undo_redo import UML_States
from ..Models.uml_save_load import diagram_to_json, json_to_diagram

def test_undo_redo_on_empty():
    uml_states = UML_States()
    assert uml_states.undo() is None
    assert uml_states.redo() is None

def test_undo_redo_single_operation():
    uml_states = UML_States()
    uml_diagram = UML_Diagram()
    
    # Save initial state (empty diagram)
    uml_states.save_state(uml_diagram)
    
    # Modify the diagram and save the new state
    uml_diagram.add_class('Class1')
    uml_states.save_state(uml_diagram)
    
    # Perform undo to revert to the initial state
    uml_states.undo()
    uml_diagram_after_undo = json_to_diagram(uml_states._states[uml_states._current_state - 1])
    
    # Expecting the initial state, which should be empty
    assert len(uml_diagram_after_undo.get_all_classes()) == 0
    
    # Perform redo to restore the state with 'Class1'
    uml_states.redo()
    uml_diagram_after_redo = json_to_diagram(uml_states._states[uml_states._current_state - 1])
    assert len(uml_diagram_after_redo.get_all_classes()) == 1
    assert uml_diagram_after_redo.get_all_classes()[0].get_name() == 'Class1'

def test_undo_redo_multiple_operations():
    uml_states = UML_States()
    uml_diagram = UML_Diagram()

    # Save initial state (empty diagram)
    uml_states.save_state(uml_diagram)

    # First modification and save
    uml_diagram.add_class('Class1')
    uml_states.save_state(uml_diagram)

    # Second modification and save
    uml_diagram.add_class('Class2')
    uml_states.save_state(uml_diagram)

    # Undo the second modification
    uml_states.undo()
    uml_diagram_after_first_undo = json_to_diagram(uml_states._states[uml_states._current_state - 1])
    assert len(uml_diagram_after_first_undo.get_all_classes()) == 1

    # Undo back to the initial state
    uml_states.undo()
    uml_diagram_after_second_undo = json_to_diagram(uml_states._states[uml_states._current_state - 1])
    assert len(uml_diagram_after_second_undo.get_all_classes()) == 0

    # Redo to 'Class1' state
    uml_states.redo()
    uml_diagram_after_first_redo = json_to_diagram(uml_states._states[uml_states._current_state - 1])
    assert len(uml_diagram_after_first_redo.get_all_classes()) == 1

    # Redo to include 'Class2'
    uml_states.redo()
    uml_diagram_after_second_redo = json_to_diagram(uml_states._states[uml_states._current_state - 1])
    assert len(uml_diagram_after_second_redo.get_all_classes()) == 2
    class_names = [cls.get_name() for cls in uml_diagram_after_second_redo.get_all_classes()]
    assert 'Class1' in class_names and 'Class2' in class_names

def test_save_state():
    uml_states = UML_States()
    uml_diagram = UML_Diagram()
    
    # Save initial state (empty diagram)
    uml_states.save_state(uml_diagram)
    assert len(uml_states._states) == 1
    
    # Modify the diagram (add class) and save the new state
    uml_diagram.add_class('Class1')
    uml_states.save_state(uml_diagram)
    assert len(uml_states._states) == 2
    
    # Modify the diagram and save the new state
    uml_diagram.add_class('Class2')
    uml_states.save_state(uml_diagram)
    assert len(uml_states._states) == 3

    # Check if the states are saved correctly
    initial_state = json_to_diagram(uml_states._states[0])
    modified_state = json_to_diagram(uml_states._states[1])

    assert len(initial_state.get_all_classes()) == 0
    assert len(modified_state.get_all_classes()) == 1
    assert modified_state.get_all_classes()[0].get_name() == 'Class1'