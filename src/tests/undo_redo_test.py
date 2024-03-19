from Models.uml_diagram import UML_Diagram
from Models.uml_undo_redo import UML_States
from Models.uml_save_load import diagram_to_json, json_to_diagram
import pytest

def test_save_state_initial():
    uml_states = UML_States()
    uml_diagram = UML_Diagram()
    uml_diagram.add_class("InitialClass")
    uml_states.save_state(uml_diagram)
    assert len(uml_states._states) == 1

def test_undo():
    uml_states = UML_States()
    uml_diagram = UML_Diagram()
    # Save initial state
    uml_states.save_state(uml_diagram)
    # Make a change and save it
    uml_diagram.add_class("FirstClass")
    uml_states.save_state(uml_diagram)
    # Undo the change
    uml_states.undo()
    assert len(uml_states._states) == 2  # Checking states count after undo
    assert uml_states._current_state == 1  # Checking the current state index