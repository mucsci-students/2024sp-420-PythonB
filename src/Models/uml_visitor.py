from abc import abstractmethod, ABC

class UML_Visitor(ABC):

    @abstractmethod
    def visit_diagram(self, uml_diagram):
        raise NotImplementedError
    
    @abstractmethod
    def visit_class(self, uml_class):
        raise NotImplementedError
    
    @abstractmethod
    def visit_field(self, uml_field):
        raise NotImplementedError
    
    @abstractmethod
    def visit_method(self, uml_method):
        raise NotImplementedError
    
    @abstractmethod
    def visit_param(self, uml_param):
        raise NotImplementedError
    
    @abstractmethod
    def visit_relation(self, uml_relation):
        raise NotImplementedError

################################################################################

class UML_Visitable(ABC):

    @abstractmethod
    def accept(self, uml_visitor: UML_Visitor):
        raise NotImplementedError