from Controllers.cli_controller import CLI_Controller
from Controllers.gui_controller import GUI_Controller

class UML_Controller:

    def __init__(self, type:str):
        self._prompt = False
        if type == 'cli':
            self._prompt = True
            self._controller = CLI_Controller()
        else: 
            self._controller = GUI_Controller()
    
    def run(self):
        while not self._controller._should_quit:
            self._controller.update(input("Command: ").strip())
    
