from Models.uml_diagram import UML_Diagram
from Models.error_handler import ErrorHandler

class CLI_Controller:

    def __init__(self, diagram:UML_Diagram = UML_Diagram(), saved:bool = False):
        self._diagram = diagram
        #TODO: Figure out a quick way of tracking saved (based on whether or not the last cmd called was save?)
        self._saved = saved
    
    @ErrorHandler.handle_error
    def run(self, input:str):
        if len(input.strip() > 0):
            data = parse(self._diagram, input)
            return input[0](*input[1:])
        
    def quit(self):
        if not self._saved: 
            #TODO: decide how to route saving
            pass