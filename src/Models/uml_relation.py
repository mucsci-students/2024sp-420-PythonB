from Models.uml_class import UML_Class
from Models.uml_visitor import UML_Visitable, UML_Visitor

rel_types = ["Aggregation", "Composition", "Inheritance", "Realization"]

class UML_Relation(UML_Visitable): 

    def __init__ (self, src:UML_Class, dst:UML_Class, rel_type:str):
        self._src = src
        self._dst = dst      
        self._type = self.__valid_type(rel_type)
        

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
    
    def accept(self, uml_visitor: UML_Visitor):
        return uml_visitor.visit_relation(self)
    
    #===================================== Mutators =====================================#   

    def set_src(self, new_src:UML_Class) -> None:
        self._src = new_src
    
    def set_dst(self, new_dst:UML_Class) -> None:
        self._dst = new_dst

    def set_type(self, new_type:str) -> None:
        self._type = self.__valid_type(new_type)

    #===================================== Helpers =====================================#
        
    def __valid_type(self, type:str) -> str:
        """Helper to validate types before changes are made to self._type"""
        # convert to capitalized format(start with upper, remain are lower)
        if type.title() not in rel_types:
            raise ValueError(f"%s is not a valid relation type" % type)
        return type.title()

    #===================================== Operators =====================================#
    
    def __eq__(self, o) -> bool:
        if self is o: 
            return True
        
        if not isinstance(o, UML_Relation):
            return False
        #exclude type from equality check b/c two classes have at most one relation
        return self._src == o._src and self._dst == o._dst
    
    def __str__(self) -> str:
        """Strings a relation in the following form: 
        
            Relation of type between src and dst
        """
        return f"{0} <--- {1} ---> {2}".format(
            self._src.get_name(), self._type, self._dst.get_name())
