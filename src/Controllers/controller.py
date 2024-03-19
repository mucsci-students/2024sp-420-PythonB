import sys
from Controllers.cli_controller import CLI_Controller
from Controllers.gui_controller import GUI_Controller
from Views.cli_view import CLI_View
class UML_Controller:

    def __init__(self):
        self._controller:CLI_Controller | GUI_Controller = self.__pick_controller()
        self._tab_complete = CLI_View()
    
    def run(self):
        while not self._controller._should_quit:
            self._controller.update()
    
    def __pick_controller(self, args:str = sys.argv) -> CLI_Controller | GUI_Controller: 
        if len(args) > 1 and str(args[1]).strip().lower() == 'cli':
            return CLI_Controller()
        return GUI_Controller()
    