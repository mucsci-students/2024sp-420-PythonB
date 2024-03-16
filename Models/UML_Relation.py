from uml_class import UML_Class
from uml_diagram import rel_types

class UML_Relation: 

    def __init__ (self, src:UML_Class, dst:UML_Class, type:str):
        self._src = src
        self._dst = dst      
        self._type = self.__valid_type(type)
        

    #===================================== Accessors =====================================#

    def get_src(self) -> UML_Class:
        return self._src
    
    def get_dst(self) -> UML_Class:
        return self._dst
    
    def get_type(self) -> str:
        return self._type
    
    def get_src_name(self) -> str: 
        return self._src.get_name()
    
    def get_dst_name(self) -> str: 
        return self._dst.get_name()
    
    #===================================== Mutators =====================================#   

    def set_src(self, new_src:UML_Class) -> None:
        self._src = new_src
    
    def set_dst(self, new_dst:UML_Class) -> None:
        self._dst = new_dst

    def set_type(self, new_type:str) -> None:
        self._type = self.__valid_type(new_type)

    #===================================== Helpers =====================================#
        
    def __valid_type(self, type:str) -> str:
        '''Helper to validate types before changes are made to self._type'''
        if type.lower() not in rel_types: 
            raise TypeError("%s is not a valid relation type" % type) 
        
        return type

    #===================================== Operators =====================================#

    def __hash__(self):
        #exclude type from this hash because it can be only one of four values
        return hash(self._src) \
        + hash(self._dst)
    
    def __eq__(self, o):
        #exclude type from equality check b/c two classes have at most one relation
        return self._src == o._src \
        and self._dst == o._dst
    
    def __str__(self):
        return "Realtion of %s between %s and %s" \
            % self._type, self._src.get_name(), self._dst.get_name()
