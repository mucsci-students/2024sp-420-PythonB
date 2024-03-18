from Models.uml_visitor import UML_Visitor
from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method
from Models.uml_param import UML_Param
from Models.uml_relation import UML_Relation

import json

class UML_Save_Visitor(UML_Visitor):
    def __init__(self) -> None:
        pass

    def visit_diagram(self, uml_diagram):
        raise NotImplementedError
    
    def visit_class(self, uml_class):
        raise NotImplementedError
    
    def visit_field(self, uml_field: UML_Field):
        return {'name': uml_field.get_name(), 'type': uml_field.get_type()}
        
    def visit_method(self, uml_method: UML_Method):
        return {'name'       : uml_method.get_name(),\
                'return_type': uml_method.get_ret(), \
                'params'     : [self.visit_param(uml_param=param) for param in uml_method.get_params()]}
    
    def visit_param(self, uml_param: UML_Param):
        return {'name': uml_param.get_name(), 'type': 'undefined'} #TODO: 'type' to be defined
        
    
    def visit_relation(self, uml_relation):
        raise NotImplementedError

################################################################################

def encode_json(obj):
    try:
        content = json.dumps(obj=obj)
    except Exception as e:
        raise e
    return content

def decode_json(content):
    return json.loads(content)

################################################################################

def load_field(obj):
    return UML_Field(name=obj['name'], type=obj['type'])

def load_param(obj):
    return UML_Param(name=obj['name']) #TODO: type to be defined

def load_method(obj):
    params = [load_param(param).get_name() for param in obj['params']] #TODO: type to be defined
    return UML_Method(obj['name'], obj['return_type'], *params)