from Models.uml_diagram import UML_Diagram
from prompt_toolkit import prompt
from Views.cli_view import CLI_View
from prompt_toolkit.completion import NestedCompleter
from Views.relation_completer import RelationCompleter

class CLI_Controller:

    def __init__(self):
        self._view = CLI_View()
    
    def request_update(self):
         self.setup_autocomplete(self._diagram)
         return prompt("Command: ", completer=self._completer).strip()

    def draw(self, diagram: UML_Diagram):
        pass

    def get_diagram(self, diagram: UML_Diagram):
        self._diagram = diagram

#=========================CLI Specific Parseing=========================#  
    def parse_list_cmd(self, d:UML_Diagram, tokens:list[str]):
        """Parses a list command, returning it in a state ready to be called"""
        match len(tokens):
            case 0:
                return [getattr(self._view, 'list'), d]
            case 1 | 2:
                return [getattr(self._view, 'list_' + tokens.pop(0)), d] + tokens
            case _:
                raise ValueError("Invalid use of list.")

    def parse_help_cmd(self, tokens:list[str]):
        """Parses a help command, returning it in a form ready to be run"""
        if len(tokens) == 0:
            return [getattr(self._view, 'help')]
        elif len(tokens) == 1:
            return [getattr(self._view, 'help_' + tokens.pop(0))]
        else:
            raise ValueError("Invalid command.")
        

#========================= Autocomplete Functionality =========================#          
    def setup_autocomplete(self, dia: UML_Diagram):
        """
        Sets up autocomplete functionality using the NestedCompleter.

        Returns:
        NestedCompleter: An instance of NestedCompleter configured with a dictionary representing available commands
        and their respective subcommands or arguments.
        """
        # Set containing all of the classes as strings
        classes = {c.get_name() for c in dia.get_all_classes()}

        # Dictionary containing nest class {classes {relationship types}}
        class_reltype = {key: {"Aggregation", "Composition", "Realization", "Inheritance"} for key in classes}
        class_class_reltype = {key: class_reltype for key in class_reltype}

        # dict containing possible relations to be deleted based on src relation
        #delete_relation = {key: self.suggest_delete_relation(self._diagram, key) for key in classes}

      
        # Method dict add method c1 m1 
        methods = {key: self.get_methods(self._diagram, key) for key in classes}
        


        self._completer = NestedCompleter.from_nested_dict({
        'add': {
            'relation': class_class_reltype,
            'class': None,
            'field': classes,
            'method': classes,
            'param': None #TODO
            
        },
        'delete': {
            'relation': self.suggest_delete_relation(dia, classes),
            'class': classes,
            'field': None, #TODO
            'method': methods, #TODO
            'param': None #TODO
        },
        'rename':{
            'class': classes,
            'field': None, #TODO
            'method': None, #TODO
            'param': None #TODO
        },
        'list':{
            'class': classes,
            'classes': None,
            'relation': None,
            'relations': None
        },
        'help':{
            'class': None,
            'attribute': None,
            'relation': None
        },
        'save': None,
        'load': None,
        'undo': None,
        'redo': None,
        'quit': None
        })  
    
    def suggest_delete_relation(self, dia: UML_Diagram, classes:set[str]) -> dict[str, str]: 
        #delete_relation = {key: self.suggest_delete_relation(self._diagram, key) for key in classes}
        res = dict()
        for uml_class in classes:
            existing_relations = set()
            for rel in dia.get_all_relations():
                if rel.get_src_name() == uml_class:
                    existing_relations.add(rel.get_dst_name())   
            if existing_relations:
                res[uml_class] = existing_relations
        return res
    

    def get_methods(self, dia: UML_Diagram, uml_class: str):
        res = set()
        method_list = dia.get_class(uml_class).get_methods()
        for method in method_list:
            res.add(method.get_name())
        return res


    def get_classes(self, dia: UML_Diagram) -> set[str]:
        res = set()
        class_list = dia.get_all_classes()
        for uml_class in class_list:
            res.add(uml_class.get_name())
        return res
    
