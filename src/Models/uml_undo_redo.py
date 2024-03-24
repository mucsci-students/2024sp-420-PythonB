from Models.uml_diagram import UML_Diagram
from Models.uml_save_load import diagram_to_json, json_to_diagram

class UML_States:
    def __init__(self, initial_diagram: UML_Diagram):
        """
        Initialize the UML_States with an initial state.
        """
        self._states = []
        self._current_state = -1
        self.save_state(initial_diagram)

    def save_state(self, diagram: UML_Diagram):
        """
        Save the current state of the diagram.
        """
        # remove all states after the current state
        self._states = self._states[:self._current_state + 1]
        self._states.append(diagram_to_json(diagram))
        self._current_state += 1

    def undo(self):
        """
        Undo the last change in the diagram, reverting to the previous state.
        """
        # The current state is after the first state
        if self._current_state > 0:
            self._current_state -= 1
        return self.get_current_state()

    def redo(self):
        """
        Redoes the last undone change in the diagram, if any.
        """
        # The current state is before the last state
        if self._current_state < len(self._states) - 1:
            self._current_state += 1
        return self.get_current_state()
    
    def get_current_state(self):
        """
        Return the current state
        """
        return json_to_diagram(self._states[self._current_state])