from Models.uml_named_object import UML_Named_Object
from Models.uml_visitor import UML_Visitable, UML_Visitor


class UML_Param(UML_Named_Object, UML_Visitable):

    def __init__ (self, name:str):
        super().__init__(name)

    def get_name(self) -> str:
        '''Accessor for name'''
        return self._name
    
    def set_name(self, new_name:str) -> None:
        '''Mutator for name'''
        self._name = new_name

    def accept(self, uml_visitor: UML_Visitor):
        return uml_visitor.visit_param(self)

#===================================== Operators =====================================#

    def __hash__(self) -> int:
        '''Hashes this value by hashing all its fields'''
        return hash(self._name) 
    
    def __eq__(self, o):
        '''Equality operator override for UML_Param'''

        #guard against error where o doesn't have _name as a field
        if not isinstance(o, UML_Param):
            return False 
        
        return self._name == o._name
    
    def __str__(self) -> str:
        '''Returns a string of this param.'''
        return self._name
