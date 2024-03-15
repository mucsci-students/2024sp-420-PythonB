from UML_Class import UML_Class
from UML_Relation import UML_Relation

rel_types = ["aggregation", "composition", "generalization", "inheritance"]

class UML_Diagram: 
    
    def __init__(self):
        self._classes:list[UML_Class] = []
        self._relations:list[UML_Relation] = []

#===================================== Accessors =====================================#
    def get_class(self, c_name:str) -> UML_Relation:
        item = self.__find_name(c_name, self._classes)
        if item is None: 
            raise ValueError("Class %s does not exist" % c_name)
        return item
    
    def get_relation(self, r_src:str, r_dst:str) -> UML_Relation:
        item = next((r for r in self._relations if r.get_src_name() == r_src and r.get_dst_name() == r_dst), None)
        if item is None: 
            raise ValueError("Relation between %s and %s does not exist." % r_src, r_dst)
        return item
        
    def get_classes(self) -> list[UML_Class]:
        return self._classes
    
    def get_relations(self) -> list[UML_Relation]:
        return self._relations

#===================================== Mutators =====================================#
    def add_class(self, c_name:str):
        item = next((v for v in self._classes if v.get_name() == c_name), None)
        if item is not None: 
            raise ValueError("Class %s already exists" % c_name)
        self._classes.append(UML_Class(c_name))

    def add_relation(self, r_src:str, r_dst:str, r_type:str):
        #make sure that r_src -> r_dst and r_dst -> r_src are not relationships already
        item = next((r for r in self._relations if 
                     (r.get_src_name() == r_src and r.get_dst_name() == r_dst) 
                     or (r.get_src_name() == r_dst and r.get_dst_name() == r_src)), None)
        if item is not None: 
            raise ValueError("Relation between %s and %s already exists." % r_src, r_dst)
        if r_type.lower() not in rel_types: 
            raise ValueError("Relation type %s is invalid" % r_type)
        
        self._relations.append(UML_Relation(self.get_class(r_src), self.get_class(r_dst), r_type))
    
    def delete_class(self, c_name:str):
        self._classes.remove(self.get_class(c_name))
    
    def delete_relation(self, r_src:str, r_dst:str):
        self._relations.remove(self.get_relation(r_src, r_dst))
    
    