import os 
from Models.uml_visitor import UML_Visitor
from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method
from Models.uml_param import UML_Param
from Models.uml_relation import UML_Relation

import json
import jsonschema

class UML_Save_Visitor(UML_Visitor):
    def __init__(self) -> None:
        pass

    def visit_diagram(self, uml_diagram: UML_Diagram):
        """
        Convert diagram to json format object.

        Return:
        (dict): the json format object
        """
        return {
                'classes'      : [self.visit_class(uml_class=clss) for clss in uml_diagram.get_all_classes()],
                'relationships': [self.visit_relation(uml_relation=relation) for relation in uml_diagram.get_all_relations()]
               }
    
    def visit_class(self, uml_class: UML_Class):
        """
        Convert class to json format object.

        Return:
        (dict): the json format object
        """
        return {
                'name'    : uml_class.get_name(),
                'fields'  : [self.visit_field(uml_field=field) for field in uml_class.get_fields()],
                'methods' : [self.visit_method(uml_method=method) for method in uml_class.get_methods()],
                'position': {'x': uml_class.get_position_x(), 'y': uml_class.get_position_y()}
               }
    
    def visit_field(self, uml_field: UML_Field):
        """
        Convert field to json format object.

        Return:
        (dict): the json format object
        """
        return {
                'name': uml_field.get_name(),
                'type': uml_field.get_type()
               }
        
    def visit_method(self, uml_method: UML_Method):
        """
        Convert method to json format object.

        Return:
        (dict): the json format object
        """
        return {
                'name'       : uml_method.get_name(),
                'return_type': uml_method.get_ret(),
                'params'     : [self.visit_param(uml_param=param) for param in uml_method.get_params()]
               }
    
    def visit_param(self, uml_param: UML_Param):
        """
        Convert param to json format object.

        Return:
        (dict): the json format object
        """
        return {
                'name': uml_param.get_name(),
                'type': 'undefined' #TODO: 'type' to be defined
               }
    
    def visit_relation(self, uml_relation: UML_Relation):
        """
        Convert relation to json format object.

        Return:
        (dict): the json format object
        """
        return {
                'source'     : uml_relation.get_src_name(),
                'destination': uml_relation.get_dst_name(),
                'type'       : uml_relation.get_type()
               }

################################################################################

def load_field(obj):
    """
    Convert json format object to field.

    Return:
    (UML_Field): the field object
    """
    return UML_Field(name=obj['name'], type=obj['type'])

def load_param(obj):
    """
    Convert json format object to field.

    Return:
    (UML_Param): the field object
    """
    return UML_Param(name=obj['name']) #TODO: type to be defined

def load_method(obj):
    """
    Convert json format object to field.

    Return:
    (UML_Method): the field object
    """
    params = [load_param(param).get_name() for param in obj['params']] #TODO: type to be defined
    return UML_Method(obj['name'], obj['return_type'], *params)

def load_class(obj):
    """
    Convert json format object to field.

    Return:
    (UML_Class): the field object
    """
    clss = UML_Class(name=obj['name'])
    for field in obj['fields']:
        clss._fields.append(load_field(field)) #TODO: add checks(add_field)
    for method in obj['methods']:
        clss._methods.append(load_method(method)) #TODO: add checks(add_method)
    # position attribute is optional
    if 'position' in obj:
        position = obj['position']
        clss._position[0] = position['x']
        clss._position[1] = position['y']
    return clss

def load_relation(obj, uml_classes: list[UML_Class]):
    """
    Convert json format object to field.

    Return:
    (UML_Relation): the field object
    """
    src = next(uml_class for uml_class in uml_classes if uml_class.get_name() == obj['source'])
    dst = next(uml_class for uml_class in uml_classes if uml_class.get_name() == obj['destination'])
    return UML_Relation(src=src, dst=dst, type=obj['type'])

def load_diagram(obj):
    """
    Convert json format object to field.

    Return:
    (UML_Diagram): the field object
    """
    diagram = UML_Diagram()
    for clss in obj['classes']:
        diagram._classes.append(load_class(clss)) #TODO: add checks(add_class)
    for relation in obj['relationships']:
        diagram._relations.append(load_relation(relation, diagram.get_all_classes())) #TODO: add checks(add_relation)
    return diagram

################################################################################

def load_schema(filename: str = 'uml_schema.json'):
    """
    Load schema file
    Error if schema file not found
    """
    path = os.path.join(os.path.dirname(__file__), '../', 'schema', filename)
    if not os.path.exists(path):
        raise ValueError("Schema file not found.")
    with open(path, 'r') as file:
        return json.load(file)
    
def load_metaschema(filename: str):
    """
    Load metaschema file
    Error if schema file not found
    """
    path = os.path.join(os.path.dirname(__file__), '../', 'schema', filename)
    if not os.path.exists(path):
        raise ValueError("Schema file not found.")
    with open(path, 'r') as file:
        return json.load(file)
    
def get_draft07_validator():
    """
    Create a draft07 validator
    """
    validator = jsonschema.Draft7Validator
    validator.META_SCHEMA = load_metaschema(filename='draft07.json')
    return validator

################################################################################

def encode_json(obj):
    """
    Encode json format object to json str.

    Return:
    (str): the json str
    """
    try:
        jsonschema.validate(instance=obj, schema=load_schema(), cls=get_draft07_validator())
        content = json.dumps(obj=obj)
    except Exception as e:
        raise e
    return content

def encode_json_without_validate(obj):
    """
    Encode json format object to json str.
    (No schema validate! For test use only!)

    Return:
    (str): the json str
    """
    try:
        content = json.dumps(obj=obj)
    except Exception as e:
        raise e
    return content

def decode_json(content):
    """
    Decode json str to json format object.

    Return:
    (Any): the json format object
    """
    obj = json.loads(content)
    jsonschema.validate(instance=obj, schema=load_schema(), cls=get_draft07_validator())
    return obj

def decode_json_without_validate(content):
    """
    Decode json str to json format object.
    (No schema validate! For test use only!)

    Return:
    (Any): the json format object
    """
    obj = json.loads(content)
    return obj

################################################################################

def diagram_to_json(uml_diagram: UML_Diagram) -> str:
    """
    Simple function to convert diagram to json str.

    Parameter:
    (UML_Diagram): the diagram object

    Return:
    (str): the json str
    """
    return encode_json(uml_diagram.accept(UML_Save_Visitor()))

def json_to_diagram(content) -> UML_Diagram:
    """
    Simple function to convert json str to diagram.

    Parameter:
    (str): the json str

    Return:
    (UML_Diagram): the diagram object
    """
    return load_diagram(decode_json(content))


