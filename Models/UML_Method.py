from Models.UML_Named_Object import UML_Named_Object
from Models.UML_Param import UML_Param

class UML_Method (UML_Named_Object):

    def __init__ (self, name:str, ret:str = "void", *params:str):
        super().__init__(name)
        self._ret:str = ret
        self._params:list[UML_Param] = []
        self.append_params(*params)

#===================================== Accessors =====================================#
    def get_name (self) -> str:
        '''Accessor for this method's name'''
        return self._name
    
    def get_ret (self) -> str:
        '''Accessor for this method's return type'''
        return self._ret
    
    def get_param (self, p_name:str) -> UML_Param: 
        '''Accessor for a param of this method
            Raises: ValueError if no param with p_name exists
        '''
        for p in self._params: 
            if p.get_name() == p_name: 
                return p
        raise ValueError ("No param with name %s exists" % p_name)
    
    def get_params (self) -> list[UML_Param]:
        '''Accessor for the full list of this method's params'''
        return self._params

#===================================== Mutators =====================================#   
    def set_name (self, new_name:str) -> None:
        '''Mutator for this method's name'''
        self._name = new_name

    def set_ret (self, new_ret:str) -> None:
        '''Mutator for this method's return type'''
        self._ret = new_ret
    
    def add_param (self, p_name:str) -> None: 
       ''' Adds a param to this methods param list if it doesn't already exist
        Raises: ValueError if p_name already exists. '''
       
       p = self.__find_param(p_name)
       if p != None: 
        raise ValueError ("Param with name %s already exists" % p_name)
       self._params.append(UML_Param(p_name))

    def delete_param (self, p_name:str) -> None:
        ''' Deletes a param if it exists
            Raises: ValueError if p_name is not a parameter of this method
        '''

        p = self.__find_param(p_name)
        if p == None:
            raise ValueError ("No param named %s exists" % p_name)
        self._params.remove(p)
    
    def change_params (self, *p_names) -> None:
        ''' Replaces the current parameter list with a new list of params '''
        self._params.clear()
        self.append_params(*p_names)
    
    def append_params (self, *p_names) -> None:
        ''' Appends the supplied params to the param list '''
        for p_name in p_names: 
            self._params.append(UML_Param(p_name))
        self._params = list(set(self._params))
        
#===================================== Helpers =====================================#
    def __find_param (self, p_name) -> UML_Param | None:
        ''' Private helper. Finds a method with name p_name
            Returns None if the param doesn't exist in this method
        '''

        for p in self._params:
            if p.get_name() == p_name:
                return p
        return None
    
#===================================== Operators =====================================#
    def __eq__ (self, o) -> bool:
        if self is o: 
            return True
        
        if not isinstance(o, UML_Method):
            return False
        
        if self._name != o._name: 
            return False
        
        if self._ret != o._ret: 
            return False
        
        if self._params != o._params: 
            return False
        
        return True
    
    def __str__ (self) -> str:
        '''Strings a method in the following form: 
            ret
            name (param1, param2,..., paramN)
        '''
        
        return self._ret + '\n' + self._name + ' (' + ', '.join(str(p) for p in self._params) + ')'