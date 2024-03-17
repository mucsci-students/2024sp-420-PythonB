from uml_class import UML_Class
from uml_relation import UML_Relation
import re

rel_types = ["aggregation", "composition", "generalization", "inheritance"]

class UML_Diagram: 
    
    def __init__(self):
        self._classes:list[UML_Class] = []
        self._relations:list[UML_Relation] = []

#===================================== Accessors =====================================#
    def get_class(self, c_name:str) -> UML_Relation:
        item = next((c for c in self._classes if c.get_name() == c_name), None)
        if item is None: 
            raise ValueError("Class %s does not exist" % c_name)
        return item
    
    def get_relation(self, r_src:str, r_dst:str) -> UML_Relation:
        #A relation between r_src and r_dst is the same as one between r_dst and r_src
        item = next((r for r in self._relations if 
                     r.get_src_name() == r_src and r.get_dst_name() == r_dst
                     or r.get_src_name() == r_dst and r.get_dst_name() == r_src), None)
        if item is None: 
            raise ValueError("Relation between %s and %s does not exist." % r_src, r_dst)
        return item
        
    def get_all_classes(self) -> list[UML_Class]:
        return self._classes
    
    def get_all_relations(self) -> list[UML_Relation]:
        return self._relations

#===================================== Mutators =====================================#
    def add_class(self, c_name:str) -> None:
        item = None
        try:
            #if this doesn't error, the class already exists
            item = self.get_class(c_name)
        except ValueError:
            self._classes.append(UML_Class(c_name))
        
        if item is not None: 
            raise ValueError("Class %s already exists" % c_name)        

    def add_relation(self, r_src:str, r_dst:str, r_type:str) -> None:
        item = None
        try:
            #if this doesn't error, the relation already exists
            item = self.get_relation(r_src, r_dst)
        except ValueError: 
            if r_type not in rel_types: 
                raise ValueError("Relation type %s is invalid" % r_type)
            self._relations.append(UML_Relation(self.get_class(r_src), self.get_class(r_dst), r_type))

        if item is not None: 
            raise ValueError("Relation between %s and %s already exists." % r_src, r_dst)
        
        
    def delete_class(self, c_name:str) -> None:
        self._classes.remove(self.get_class(c_name))
    
    def delete_relation(self, r_src:str, r_dst:str) -> None:
        self._relations.remove(self.get_relation(r_src, r_dst))
    
    def delete_relations_containing(self, c_name:str) -> None:
        '''Remove all relations that have c_name from self._relations'''
        self._relations = list(filter(lambda rel: rel.get_src_name() != c_name and rel.get_dst_name() != c_name, self._relations))

#===================================== Operators =====================================#

    #TODO: Remove this function if we make diagram Singleton            
    def __eq__(self, o):
        if self is o: 
            return True
        
        if not isinstance(o, UML_Diagram):
            return False
        
        return self._classes == o._classes and self._relations == o._relations
    
    def __str__(self):
        '''Strings a diagram in the following format: 
            
            Classes:
                class1
                class2
            Relationships:
                relation 1
                relation 2
        '''
        return 'Classes:' + '\n\t'.join(str(c) for c in self._classes) + '\n' \
                + 'Relationships:' + '\n\t'.join(str(r) for r in self._relations)


def __check_args (*args:str):
    '''Makes sure every string in *args is valid'''
    regex = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
    for arg in [*args]: 
        if not regex.match(arg):
            raise ValueError("%s is not a valid name, please try again." % arg)
    





    
