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

    def visit_diagram(self, uml_diagram: UML_Diagram):
        return {
                'classes'      : [self.visit_class(uml_class=clss) for clss in uml_diagram.get_all_classes()],
                'relationships': [self.visit_relation(uml_relation=relation) for relation in uml_diagram.get_all_relations()]
               }
    
    def visit_class(self, uml_class: UML_Class):
        return {
                'name'    : uml_class.get_name(),
                'fields'  : [self.visit_field(uml_field=field) for field in uml_class.get_fields()],
                'methods' : [self.visit_method(uml_method=method) for method in uml_class.get_methods()],
                'position': {'x': 0, 'y': 0} #TODO: position to be defined
               }
    
    def visit_field(self, uml_field: UML_Field):
        return {
                'name': uml_field.get_name(),
                'type': uml_field.get_type()
               }
        
    def visit_method(self, uml_method: UML_Method):
        return {
                'name'       : uml_method.get_name(),
                'return_type': uml_method.get_ret(),
                'params'     : [self.visit_param(uml_param=param) for param in uml_method.get_params()]
               }
    
    def visit_param(self, uml_param: UML_Param):
        return {
                'name': uml_param.get_name(),
                'type': 'undefined' #TODO: 'type' to be defined
               }
    
    def visit_relation(self, uml_relation: UML_Relation):
        return {
                'source'     : uml_relation.get_src_name(),
                'destination': uml_relation.get_dst_name(),
                'type'       : uml_relation.get_type()
               }

################################################################################

def load_field(obj):
    return UML_Field(name=obj['name'], type=obj['type'])

def load_param(obj):
    return UML_Param(name=obj['name']) #TODO: type to be defined

def load_method(obj):
    params = [load_param(param).get_name() for param in obj['params']] #TODO: type to be defined
    return UML_Method(obj['name'], obj['return_type'], *params)

def load_class(obj):
    clss = UML_Class(name=obj['name'])
    for field in obj['fields']:
        clss._fields.append(load_field(field)) #TODO: add checks(add_field)
    for method in obj['methods']:
        clss._methods.append(load_method(method)) #TODO: add checks(add_method)
    #TODO: position to be defined
    return clss

def load_relation(obj, uml_classes: list[UML_Class]):
    src = next(uml_class for uml_class in uml_classes if uml_class.get_name() == obj['source'])
    dst = next(uml_class for uml_class in uml_classes if uml_class.get_name() == obj['destination'])
    return UML_Relation(src=src, dst=dst, type=obj['type'])

def load_diagram(obj):
    diagram = UML_Diagram()
    for clss in obj['classes']:
        diagram._classes.append(load_class(clss)) #TODO: add checks(add_class)
    for relation in obj['relationships']:
        diagram._relations.append(load_relation(relation, diagram.get_all_classes())) #TODO: add checks(add_relation)
    return diagram

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

def diagram_to_json(uml_diagram: UML_Diagram):
    return encode_json(uml_diagram.accept(UML_Save_Visitor()))

def json_to_diagram(content):
    return load_diagram(decode_json(content))