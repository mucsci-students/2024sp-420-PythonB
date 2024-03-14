from UML_Named_Object import UML_Named_Object


class UML_Param(UML_Named_Object):

    def __init__ (self, name:str):
        self._name:str = name

    def get_name(self) -> str:
        '''Accessor for name'''
        return self._name
    
    def set_name(self, new_name:str) -> None:
        '''Mutator for name'''
        self._name = new_name

    def __eq__(self, o):
        '''Equality operator override for UML_Param'''

        #guard against error where o doesn't have _name as a field
        if not isinstance(o, self):
            return False 
        
        return self._name == o._name
    
    def __str__(self) -> str:
        '''Returns a string of this param.'''
        return self._name