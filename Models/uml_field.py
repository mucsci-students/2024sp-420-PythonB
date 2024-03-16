from Models.uml_named_object import UML_Named_Object

class UML_Field (UML_Named_Object):
    
    def __init__(self, name:str, type:str = "void"):
        self._name:str = name
        self._type:str = type

#===================================== Accessors =====================================#
    def get_name (self) -> str:
        '''Accessor for this field's name'''
        return self._name
    
    def get_type (self) -> str:
        '''Accessor for this field's return type'''
        return self._type
    
#===================================== Mutators =====================================#
    def set_name(self, new_name:str) -> None:
        '''Mutator for this field's name'''
        self._name = new_name

    def set_type(self, new_name:str) -> None:
        '''Mutator for this field's return type'''
        self._type = new_name

#===================================== Operators =====================================#
    def __eq__(self, o) -> bool:
        if self is o:
            return True

        if not isinstance(o, UML_Field):
            return False

        if self._name != o._name:
            return False

        if self._type != o._type:
            return False

        return True
    
    def __hash__(self):
        return hash(self._name) \
            + hash(self._type)
    
    def __str__(self) -> str:
        '''Strings a field in the following form:
            type name
        '''
        return self._type + ' ' + self._name