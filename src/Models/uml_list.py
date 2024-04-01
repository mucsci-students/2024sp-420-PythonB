from uml_visitor import UML_Visitor
from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method
from Models.uml_param import UML_Param
from Models.uml_relation import UML_Relation

class UML_List_Visitor(UML_Visitor):
    def __init__(self) -> None: 
        pass

    def visit_diagram(self, uml_diagram: UML_Diagram, tab_depth: int = 0) -> str:
        """Visitor to list a diagram. Lists in the form: 
                Diagram:
                  Classes: 
                    Class1
                    ClassN
                  Relations:
                    Relation1
                    RelationN
        """
        classes = ''.join([self.visit_class(c, tab_depth + 2) for c in uml_diagram.get_all_classes()])
        relations = ''.join([self.visit_relation(r, tab_depth + 2) for r in uml_diagram.get_all_relations()])

        out = "Diagram:\n"
        #only print classes and relations headers if at least one class or relation exists
        out += self.__tabs(tab_depth + 1) + "Classes:\n" + classes if len(classes) > 0 else ''
        out += self.__tabs(tab_depth + 1) + "Relations:\n" + relations if len(relations) > 0 else ''

        return out
    
    
    def visit_class(self, uml_class: UML_Class, tab_depth: int = 0) -> str:
        """Visitor to list a class. Lists in the form: 
                Class Name:
                  Fields:  
                    Field1
                    FieldN
                  Methods:
                    Method1
                    MethodN
        """
        fields = ''.join([self.visit_field(f, tab_depth + 2) for f in uml_class.get_fields()])
        methods = ''.join([self.visit_method(m, tab_depth + 2) for m in uml_class.get_methods()])
        out = self.__tabs(tab_depth) + uml_class.get_name() + '\n'

        #only print fields and methods if the class has them
        out += self.__tabs(tab_depth + 1) + 'Fields:\n' + fields if len(fields) > 0 else ''
        out += self.__tabs(tab_depth + 1) + 'Methods:\n' + methods if len(methods) > 0 else ''
        return out

    
   
    def visit_field(self, uml_field: UML_Field, tab_depth: int = 0) -> str:
        """Visitor to list a field. Lists in the form: 
                type name
        """
        return self.__tabs(tab_depth) + uml_field.get_type() + ' ' + uml_field.get_name() + '\n'
    
    
    def visit_method(self, uml_method: UML_Method, tab_depth: int = 0) -> str:
        """Visitor to list a method. Lists in the form: 
                ret
                name (param1, paramN)
        """
        return self.__tabs(tab_depth) + uml_method.get_ret() \
        + ' ' + uml_method.get_name() + ' (' \
        + ', '.join([self.visit_param(p) for p in uml_method.get_params()]) \
        + ')\n'
    
   
    def visit_param(self, uml_param: UML_Param) -> str:
        """Visitor to list a param. Lists in the form:
                name
        """
        return uml_param.get_name()
    
    
    def visit_relation(self, uml_relation: UML_Relation, tab_depth: int = 0) -> str:
        """Visitor to list a relation. Lists in the form: 
                src <--- type ---> dst
        """
        return self.__tabs(tab_depth) + str(uml_relation) + '\n'
    
    def __tabs(self, tab_depth:int = 0):
        return '  ' * tab_depth
