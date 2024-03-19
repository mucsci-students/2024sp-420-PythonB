import sys 
import os 
from pathlib import Path 
from Controllers.cli_controller import CLI_Controller
from Controllers.gui_controller import GUI_Controller
from Models.uml_save_load import json_to_diagram, diagram_to_json

class UML_Controller:

    def __init__(self):
        self._controller = self.__pick_controller()
    
    def run(self):
        while not self._controller._should_quit:
            self._controller.update(input=input("Command: ").strip())
    
    def save(self, filename:str):
        """ Saves this controller's diagram to the provided filename 
            NOTE: Overwrites an existing file with the same name
        """
        jsoned = diagram_to_json(self._controller._diagram)
        path = os.path.join(os.path.dirname(__file__), '../', 'save')
        if not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(path, filename + '.json')
        file = open(path, "w")
        file.write(jsoned)
        file.close()
    
    def load(self, filename:str):
        path = os.path.join(os.path.dirname(__file__), '../', 'save')
        if not os.path.exists(path):
           raise ValueError("No file named {0}.json exists in the save folder.".format(filename))
        path = os.path.join(path, filename + '.json')
        self._controller._diagram = json_to_diagram(Path(path).read_text())
    
    def __pick_controller(args:str = sys.argv) -> CLI_Controller | GUI_Controller: 
        if len(args) > 1 and str(args[1]) == 'cli':
            return CLI_Controller()
        return GUI_Controller()
