from Models.uml_diagram import UML_Diagram
from Models.error_handler import Error_Handler
from Models.uml_parser import parse

class CLI_Controller:

    def __init__(self, diagram:UML_Diagram = UML_Diagram(), saved:bool = False):
        self._diagram = diagram
        #TODO: Figure out a quick way of tracking saved (based on whether or not the last cmd called was save?)
        self._saved = saved
        self._should_quit = False
    
    def update(self, input:str):
        if len(input.strip() > 0):
            data = parse(self._diagram, input)
            if input[0] == 'save':
                self._saved = True
            else:
                self._saved = False
            return data[0](*data[1:])
        
    def quit(self):
        self._should_quit = True
        if not self._saved: 
            #TODO: decide how to route saving
            pass