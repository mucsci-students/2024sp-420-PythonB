from UML_Named_Object import UML_Named_Object
from UML_Method import UML_Method
from UML_Field import UML_Field

class UML_Class(UML_Named_Object): 

    def __init__(self, name:str):
        super.__init__(name)
        self._fields = []
        self._methods = []

#===================================== Accessors =====================================#
    
    def get_name(self) -> str: 
        return self._name
    
    def get_field(self, f_name:str) -> UML_Field:
        item = self.__find_name(f_name, "field")
        if item is None: 
            raise ValueError("Field %s does not exist" % f_name) 
        return item
 
    def get_method(self, m_name:str) -> UML_Method:
        item = self.__find_name(m_name, "method")
        if item is None: 
            raise ValueError("Method %s does not exist" % m_name)
        return item

    def get_fields(self) -> list[UML_Field]:
        return self._fields
    
    def get_methods(self) -> list[UML_Method]:
        return self._methods
    
#===================================== Mutators =====================================#   
    
    def set_name(self, new_name:str) -> None:
        self._name == new_name
    
    def add_field(self, new_field_name:str, new_field_type:str) -> None:
        self.__error(new_field_name, "field")
        self._fields.append(UML_Field(new_field_name, new_field_type))

    def add_method(self, new_method_name:str, new_method_ret:str, *new_method_params):
        self.__error(new_method_name, "method")
        self._methods.append(UML_Method(new_method_name, new_method_ret, *new_method_params))

#===================================== Helpers =====================================#

    def __error(self, value:str, loc:str) -> None:
        '''Iterate through a list and error if value already exists in list'''
        if self.__find_name(value, loc) is not None:
            raise ValueError("%s %s already exists" % loc, value) 
    
    def __find_name(self, name:str, loc:str) -> UML_Field | UML_Method | None:
        attr = getattr(self, '_' + loc + 's')
        return next((v for v in attr if v.get_name() == name), None)
    
#===================================== Operators =====================================#
    
    def __hash__(self) -> int:
        return hash(self._name) \
        + hash(self._fields) \
        + hash(self._methods)
    
    def __eq__(self, o) -> bool:
        if self is o: 
            return True
        
        if not isinstance(o, UML_Class):
            return False
        
        return self._name == o._name \
        and self._methods == o._methods \
        and self._fields == o._fields
    
    def __str__ (self):
        pass