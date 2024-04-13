from Models.uml_named_object import UML_Named_Object
from Models.uml_method import UML_Method
from Models.uml_field import UML_Field
from Models.uml_visitor import UML_Visitable, UML_Visitor

class UML_Class(UML_Named_Object, UML_Visitable): 

    def __init__(self, name:str):
        self._name = name
        self._fields:list[UML_Field] = []
        self._methods:list[UML_Method] = []
        self._position = [0] * 2

#===================================== Accessors =====================================#
    
    def get_name(self) -> str: 
        return self._name
    
    def get_field(self, f_name:str) -> UML_Field:
        item = self.__find_name(f_name, self._fields)
        if item is None: 
            raise ValueError(f"Field %s does not exist" % f_name) 
        return item
 
    def get_method(self, m_name:str) -> UML_Method:
        item = self.__find_name(m_name, self._methods)
        if item is None: 
            raise ValueError(f"Method %s does not exist" % m_name)
        return item

    def get_fields(self) -> list[UML_Field]:
        return self._fields
    
    def get_methods(self) -> list[UML_Method]:
        return self._methods
    
    def get_position(self) -> list[int]:
        return self._position
    
    def get_position_x(self) -> list[int]:
        return self._position[0]
    
    def get_position_y(self) -> list[int]:
        return self._position[1]
    
    def accept(self, uml_visitor: UML_Visitor):
        return uml_visitor.visit_class(self)
    
#===================================== Mutators =====================================#   
    
    def set_name(self, new_name:str) -> None:
        self._name = new_name
    
    def add_field(self, new_f_name:str, new_f_type:str) -> None:
        self.__error(new_f_name, self._fields)
        self._fields.append(UML_Field(new_f_name, new_f_type))

    def add_method(self, new_m_name:str, new_m_ret:str, *new_m_params) -> None:
        self.__error(new_m_name, self._methods)
        self._methods.append(UML_Method(new_m_name, new_m_ret, *new_m_params))

    def delete_field(self, f_name:str) -> None:
        item = self.__find_name(f_name, self._fields)
        if item is None: 
            raise ValueError(f"Field %s does not exist" % f_name) 
        self._fields.remove(item)

    def delete_method(self, m_name:str) -> None:
        item = self.__find_name(m_name, self._methods)
        if item is None: 
            raise ValueError(f"Method %s does not exist" % m_name)
        self._methods.remove(item)

    def set_position_with_delta(self, position: list[int]) -> None:
        self._position[0] += position[0]
        self._position[1] += position[1]

#===================================== Helpers =====================================#

    def __error(self, value:str, loc:list) -> None:
        """Iterate through a list and error if value already exists in list"""
        if self.__find_name(value, loc) is not None:
            raise ValueError(f"%s already exists" % value) 
    
    def __find_name(self, name:str, loc:list) -> UML_Field | UML_Method | None:
        return next((v for v in loc if v.get_name() == name), None)
    
#===================================== Operators =====================================#
        
    def __eq__(self, o) -> bool:
        if self is o: 
            return True
        
        if not isinstance(o, UML_Class):
            return False
        
        return self._name == o._name \
        and self._methods == o._methods \
        and self._fields == o._fields
        # position does not need to be equal
    
