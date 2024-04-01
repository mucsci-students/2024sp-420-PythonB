from prompt_toolkit.completion import NestedCompleter
from Models.uml_diagram import UML_Diagram
from Models.uml_list import UML_List_Visitor
from Views.relation_completer import RelationCompleter

class CLI_View:
    
    def __init__(self):
        self._lister = UML_List_Visitor() 
        self._completer = self.setup_autocomplete() 
             
    #A list of surface level commands    
    def help(self):
        return (
                "help                                                           Displays this menu\n"
                "help class                                                     Displays commands related to classes\n"
                "help attribute                                                 Displays commands related to attributes\n"
                "help relation                                                  Displays commands related to relations\n"
                "save <file_name>                                               Saves your UML diagram as a JSON file\n"
                "load <file_name>                                               Loads a UML diagram from a JSON file\n"
                "quit                                                           Exits the program\n")   
          
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
                "add field <class_name> <field_name> <field_type>               Adds field named <field_name> with type <field_type>\n" 
                "add method <class_name> <method_name> <return_type>            Adds method named <method_name> with return type <return_type>\n"  
                "add param <class_name> <method_name> <param_name>              Adds param named <param_name> to method <method_name>\n"              
                "delete method <class_name> <method_name>                       Deletes method named <method_name>\n"
                "delete field <class_name> <field_name>                         Deletes field named <field_name>\n"
                "delete param <class_name> <method_name> <param_name>           Deletes param named <param_name> from <method_name>\n"
                "rename field <class_name> <current_name> <new_name>            Renames field <current_name> to <new_name>\n"
                "rename method <class_name> <current_name> <new_name>           Renames method <current_name> to <new_name>\n"
                "rename param <class_name> <method_name> <current_name> <new_name>          Renames param <current_name> in method\n"
                "   <method_name> to <new_name>\n")
        
    #Commands for relations
    def help_relation(self):
        return (
                "help relations                                         Displays this menu\n"
                "add relation <src_class> <des_class> <relation_type>   Adds a relation between <src_class> and <des_class> of\n"
                "   <relation_type>: (Aggregation, Composition, Realization, Inheritance)\n"
                "delete relation <src_class> <des_class>                Deletes the relation between <src_class> <des_class>\n"
                "list relations                                         Lists all relations\n"
                "list relation <class>                                  Lists all relations <class> is a part of"
        )
        
    def list(self, d:UML_Diagram) -> str:
        """Lists the whole diagram"""
        return d.accept(self._lister)
    
    def list_classes(self, d:UML_Diagram) -> str:
        """Lists all the classes in the provided diagram""" 
        return ''.join(c.accept(self._lister) for c in d.get_all_classes())
    
    def list_relations(self, d:UML_Diagram) -> str: 
        """Lists all the relations in the provided diagram"""
        return ''.join(r.accept(self._lister) for r in d.get_all_relations())
    
    def list_class(self, d:UML_Diagram, c_name:str) -> str:
        """Lists all the data about class c_name"""
        return d.get_class(c_name).accept(self._lister)
    
    def list_relation(self, d:UML_Diagram, r_name:str) -> str: 
        """Lists all relations that r_name is a part of in d"""
        return ''.join(r.accept(self._lister) for r in d.get_all_relations() 
                       if r.get_dst_name() == r_name or r.get_src_name() == r_name)
    

    def setup_autocomplete(self):
        """
        Sets up autocomplete functionality using the NestedCompleter.

        Returns:
        NestedCompleter: An instance of NestedCompleter configured with a dictionary representing available commands
        and their respective subcommands or arguments.
        """
        return NestedCompleter.from_nested_dict({
        'add': {
            'relation': RelationCompleter(),
            'class': None,
            'field': None,
            'method': None,
            'param': None
            
        },
        'delete': {
            'relation': None,
            'class': None,
            'field': None,
            'method': None,
            'param': None
            
        },
        'rename':{
            'class': None,
            'field': None,
            'method': None,
            'param': None
        },
        'list':{
            'class': None,
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