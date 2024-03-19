from prompt_toolkit.completion import NestedCompleter
from Models.uml_diagram import UML_Diagram

class CLI_View:
    
    def __init__(self):
        self._autocompleter = self.setup_autocomplete()  

    def setup_autocomplete(self):
        return NestedCompleter.from_nested_dict({
        'add': {
            'class': None,
            'field': None,
            'method': None,
            'relationship': None
        },
        'delete': {
            'class': None,
            'field': None,
            'method': None,
            'relationship': None
        },
        'rename':{
            'class': None,
            'field': None,
            'method': None
        },
        'list':{
            'class': None,
            'classes': None,
            'relationship': None,
            'relationships': None
        },
        'save': None,
        'load': None,
        'exit': None
        })  
             
    #A list of surface level commands    
    def help(self):
        return (
                "help                                                           Displays this menu\n"
                "help class                                                     Displays commands related to classes\n"
                "help attribute                                                 Displays commands related to attributes\n"
                "help relation                                              Displays commands related to relations\n"
                "save <file_name>                                               Saves your UML diagram as a JSON file\n"
                "load <file_name>                                               Loads a UML diagram from a JSON file\n"
                "exit                                                           Exits the program\n")   
          
    #Commands for classes      
    def help_class(self):
        return (
                "help class                                                     Displays this menu\n"
                "add class <class_name>                                         Adds a class named <class_name>\n"
                "delete class <class_name>                                      Deletes class named <class_name> and all of its attributes/relations\n"
                "rename class <current_name> <new_name>                         Renames class <current_name> to <new_name>\n"
                "list class <class_name>                                        Lists all attributes/relations pertaining to <class_name>\n"
                "list classes                                                   Lists all classes in current UML\n")
    
    #Commands for attributes
    def help_attribute(self):
        return (
                "help attribute                                                 Displays this menu\n"
                "add field <class_name> <field_name>                            Adds field named <field_name>\n" 
                "add method <class_name> <method_name>                          Adds method named <method_name>\n"  
                "add param <class_name> <method_name> <param_name>              Adds param named <param_name> to method <method_name>\n"              
                "delete method <class_name> <method_name>                       Deletes method named <method_name>\n"
                "delete field <class_name> <field_name>                         Deletes field named <field_name>\n"
                "delete parameter <class_name> <method_name> <param_name>       Deletes param named <param_name> from <method_name>\n"
                "rename field <class_name> <current_name> <new_name>            Renames field <current_name> to <new_name>\n"
                "rename method <class_name> <current_name> <new_name>           Renames method <current_name> to <new_name>\n"
                "rename parameter <class_name> <method_name> <current_name> <new_name>          Renames param <current_name> in method\n"
                "   <method_name> to <new_name>\n")
        
    #Commands for relations
    def help_relation(self):
        return (
                "help relations                                         Displays this menu\n"
                "add relation <src_class> <des_class> <relation_type>   Adds a relation between <src_class> and <des_class> of\n"
                "   <relation_type>: (Aggregation, Composition, Generalization, Inheritance)\n"
                "delete relation <src_class> <des_class>                Deletes the relation between <src_class> <des_class>\n"
                "list relations                                         Lists all relations\n"
        )
        
    def list(d:UML_Diagram) -> str:
        return str(d)
    
    def list_classes(d:UML_Diagram) -> str: 
        return ''.join([str(c) for c in d._classes])
    
    def list_relations(d:UML_Diagram) -> str: 
        return ''.join([str(r) for r in d._relations])
    
    def list_class(d:UML_Diagram, c_name:str) -> str:
        cl = d.get_class(c_name)
        relations = ''.join([str(r) for r in d._relations 
                    if r.get_src_name() == c_name or r.get_dst_name() == c_name])
        return str(cl) + '\nRelations:\n' + relations
    