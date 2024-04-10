from Models.uml_named_object import UML_Named_Object
from Models.uml_visitor import UML_Visitable, UML_Visitor

class UML_Field (UML_Named_Object, UML_Visitable):
    
    def __init__(self, name:str, type:str = "void"):
        super().__init__(name)
        self._type:str = type

#===================================== Accessors =====================================#
    def get_name (self) -> str:
        """Accessor for this field's name"""
        return self._name
    
    def get_type (self) -> str:
        """Accessor for this field's return type"""
        return self._type
    
    def accept(self, uml_visitor: UML_Visitor):
        return uml_visitor.visit_field(self)
    
#===================================== Mutators =====================================#
    def set_name(self, new_name:str) -> None:
        """Mutator for this field's name"""
        self._name = new_name

    def set_type(self, new_name:str) -> None:
        """Mutator for this field's return type"""
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
    
