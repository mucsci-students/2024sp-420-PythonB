from Models.uml_named_object import UML_Named_Object
from Models.uml_method import UML_Method
from Models.uml_field import UML_Field

class UML_Class(UML_Named_Object): 

    def __init__(self, name:str):
        super().__init__(name)
        self._fields:list[UML_Field] = []
        self._methods:list[UML_Method] = []

#===================================== Accessors =====================================#
    
    def get_name(self) -> str: 
        return self._name
    
    def get_field(self, f_name:str) -> UML_Field:
        item = self.__find_name(f_name, self._fields)
        if item is None: 
            raise ValueError("Field %s does not exist" % f_name) 
        return item
 
    def get_method(self, m_name:str) -> UML_Method:
        item = self.__find_name(m_name, self._methods)
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
    
    def add_field(self, new_f_name:str, new_f_type:str) -> None:
        self.__error(new_f_name, self._fields)
        self._fields.append(UML_Field(new_f_name, new_f_type))

    def add_method(self, new_m_name:str, new_m_ret:str, *new_m_params) -> None:
        self.__error(new_m_name, self._methods)
        self._methods.append(UML_Method(new_m_name, new_m_ret, *new_m_params))

    def delete_field(self, f_name:str) -> None:
        item = self.__find_name(f_name, self._fields)
        if item is None: 
            raise ValueError("Field %s does not exist" % f_name) 
        self._fields.remove(item)

    def delete_method(self, m_name:str) -> None:
        item = self.__find_name(m_name, self._methods)
        if item is None: 
            raise ValueError("Method %s does not exist" % m_name)
        self._fields.remove(item)

#===================================== Helpers =====================================#

    def __error(self, value:str, loc:list) -> None:
        '''Iterate through a list and error if value already exists in list'''
        if self.__find_name(value, loc) is not None:
            raise ValueError("%s already exists" % value) 
    
    def __find_name(self, name:str, loc:list) -> UML_Field | UML_Method | None:
        return next((v for v in loc if v.get_name() == name), None)
    
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
        ''' Strings a class in the following format: 

        Class:
            Fields:
                field1
                field2
            Methods:
                method1
                method2
        '''
        return '%s:' % self._name + '\n\tFields:' + '\n\t\t'.join(str(f) for f in self._fields) \
                + '\n\tMethods:' + '\n\t\t'.join(str(m) for m in self._methods)
