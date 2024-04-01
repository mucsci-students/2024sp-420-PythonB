from Models.uml_named_object import UML_Named_Object
from Models.uml_param import UML_Param
from Models.uml_visitor import UML_Visitable, UML_Visitor
from collections import OrderedDict

class UML_Method (UML_Named_Object, UML_Visitable):

    def __init__ (self, name:str, ret:str, *params:str):
        super().__init__(name)
        self._ret:str = ret
        self._params:list[UML_Param] = []
        self.append_params(*params)

#===================================== Accessors =====================================#
    def get_name (self) -> str:
        """Accessor for this method's name"""
        return self._name
    
    def get_ret (self) -> str:
        """Accessor for this method's return type"""
        return self._ret
    
    def get_param (self, p_name:str) -> UML_Param: 
        """Accessor for a param of this method
            Raises: ValueError if no param with p_name exists
        """
        for p in self._params: 
            if p.get_name() == p_name: 
                return p
        raise ValueError ("No param with name %s exists" % p_name)
    
    def get_params (self) -> list[UML_Param]:
        """Accessor for the full list of this method's params"""
        return self._params
    
    def accept(self, uml_visitor: UML_Visitor):
        return uml_visitor.visit_method(self)

#===================================== Mutators =====================================#   
    def set_name (self, new_name:str) -> None:
        """Mutator for this method's name"""
        self._name = new_name

    def set_ret (self, new_ret:str) -> None:
        """Mutator for this method's return type"""
        self._ret = new_ret
    
    def add_param (self, p_name:str) -> None: 
       """ Adds a param to this methods param list if it doesn't already exist
        Raises: ValueError if p_name already exists. """
       
       if self.__find_param(p_name) is not None: 
        raise ValueError ("Param with name %s already exists" % p_name)
       self._params.append(UML_Param(p_name))

    def delete_param (self, p_name:str) -> None:
        self._params.remove(self.get_param(p_name))
    
    def change_params (self, *p_names) -> None:
        """ Replaces the current parameter list with a new list of params """ 
        self._params.clear()
        self.append_params(*p_names)
    
    def append_params (self, *p_names) -> None:
        """ Appends the supplied params to the param list """
        self._params.extend([UML_Param(p_name) for p_name in p_names])
        self._params = list(OrderedDict.fromkeys(self._params))
#===================================== Helpers =====================================#
        
    def __find_param (self, p_name) -> UML_Param | None:
        """ Private helper. Finds a method with name p_name
            Returns None if the param doesn't exist in this method
        """

        return next((p for p in self._params if p.get_name() == p_name), None)
    
#===================================== Operators =====================================#
    
    def __hash__(self) -> int:
        return hash(self._name)  \
            + hash(self._ret)    \
            + hash(self._params)
    
    def __eq__ (self, o) -> bool:
        if self is o: 
            return True
        
        if not isinstance(o, UML_Method):
            return False
        
        return self._name == o._name \
            and self._ret == o._ret  \
            and self._params == o._params
    
    def __str__ (self) -> str:
        """Strings a method in the following form: 
        
            ret name (param1, param2,..., paramN)
        """
        
        return self._ret + ' ' + self._name + ' (' + ', '.join(str(p) for p in self._params) + ')'
