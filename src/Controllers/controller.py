import sys
from Controllers.cli_controller import CLI_Controller
from Controllers.gui_controller import GUI_Controller
class UML_Controller:

    def __init__(self):
        """
        Initializes the instance with either a CLI_Controller or GUI_Controller based on user choice, 
        and sets up autocomplete functionality.
        """
        self._controller:CLI_Controller | GUI_Controller = self.__pick_controller()

        
    
    def run(self):
        """Executes the main loop of the program, utilizing the prompt_toolkit prompt for autocomplete."""
        while not self._controller._should_quit:
            self._controller.update()

    def __pick_controller(self, args:str = sys.argv) -> CLI_Controller | GUI_Controller: 
        if len(args) > 1 and str(args[1]).strip().lower() == 'cli':
            return CLI_Controller()
        return GUI_Controller()
    