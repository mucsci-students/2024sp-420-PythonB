import sys
from Controllers.cli_controller import CLI_Controller
from Controllers.gui_controller import GUI_Controller

class UML_Controller:

    def __init__(self, type:list[str] = sys.argv):
        if len(type) > 1 and str(type[1]) == 'cli':
            self._controller = CLI_Controller()
        else: 
            self._controller = GUI_Controller()
    
    def run(self):
        while not self._controller._should_quit:
            self._controller.update(input=input("Command: ").strip())
    
