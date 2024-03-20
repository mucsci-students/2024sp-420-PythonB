from Models.uml_diagram import UML_Diagram
from Models.uml_save_load import diagram_to_json, json_to_diagram

class UML_States:
    def __init__(self, initial_diagram: UML_Diagram):
        self._states = [diagram_to_json(initial_diagram)]
        self._current_state = 0

    def save_state(self, diagram: UML_Diagram):
        """
        Save the current state of the diagram.
        """
        self._states = self._states[:self._current_state + 1]
        self._states.append (diagram_to_json(diagram))
        self._current_state += 1

    def undo(self):
        """
        Undo the last change in the diagram, reverting to the previous state.
        """
        if self._current_state >= 1:
            self._current_state -= 1
        return json_to_diagram(self._states[self._current_state])

    def redo(self):
        """
        Redoes the last undone change in the diagram, if any.
        """
        if self._current_state < len(self._states) - 1:
            self._current_state += 1
        return json_to_diagram(self._states[self._current_state])