from Models.uml_diagram import UML_Diagram
from prompt_toolkit import prompt
from Views.cli_view import CLI_View
from prompt_toolkit.completion import NestedCompleter


class CLI_Controller:

    def __init__(self):
        self._view = CLI_View()

    def request_update(self):
        self.setup_autocomplete()
        return prompt("Command: ", completer=self._completer).strip()

    def get_diagram(self, diagram: UML_Diagram):
        self._diagram = diagram

# =========================CLI Specific Parseing=========================#
    def parse_list_cmd(self, d: UML_Diagram, tokens: list[str]):
        """Parses a list command, returning it in a state ready to be called"""
        match len(tokens):
            case 0:
                return [getattr(self._view, 'list'), d]
            case 1 | 2:
                return [getattr(self._view, 'list_' + tokens.pop(0)), d] + tokens
            case _:
                raise ValueError("Invalid use of list.")

    def parse_help_cmd(self, tokens: list[str]):
        """Parses a help command, returning it in a form ready to be run"""
        if len(tokens) == 0:
            return [getattr(self._view, 'help')]
        elif len(tokens) == 1:
            return [getattr(self._view, 'help_' + tokens.pop(0))]
        else:
            raise ValueError("Invalid command.")


# ========================= Autocomplete Functionality =========================#


    def setup_autocomplete(self):
        """
        Sets up autocomplete functionality using the NestedCompleter.

        """

        self._completer = NestedCompleter.from_nested_dict({
            'add': {
                'relation': self.get_add_relation(),
                'class': None,
                'field': self.get_classes(),
                'method': self.get_classes(),
                'param': self.get_methods()

            },
            'delete': {
                'relation': self.get_delete_relation(),
                'class': self.get_classes(),
                'field': self.get_fields(),
                'method': self.get_methods(),
                'param': self.get_params()
            },
            'rename': {
                'class': self.get_classes(),
                'field': self.get_fields(),
                'method': self.get_methods(),
                'param': self.get_params()
            },
            'list': {
                'class': self.get_classes(),
                'classes': None,
                'relation': self.get_classes(),
                'relations': None
            },
            'help': {
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

    def get_delete_relation(self) -> dict[str, set[str]]:
        """
        Get a dictionary of relations to be deleted between classes.

        Returns:
            dict[str, set[str]]: A dictionary where keys are class names (str) and values are sets
                                containing names of classes (str) with existing relations to be deleted.
        """
        res = dict()
        for uml_class in self.get_classes():
            existing_relations = set()
            for rel in self._diagram.get_all_relations():
                if rel.get_src_name() == uml_class:
                    existing_relations.add(rel.get_dst_name())
            if existing_relations:
                res[uml_class] = existing_relations
        return res

    def get_add_relation(self) -> dict[str, dict[str, str]]:
        """
        Suggests class, class, relationship type 

        Returns:
        dict[str, dict[str, str]]: A dictionary where keys are class names (str)
                                                 and values are dictionaries of class names (str) and
                                                 corresponding relationship types (str).
        """
        rel_types = dict([
            ("Aggregation", None),
            ("Composition", None),
            ("Realization", None),
            ("Inheritance", None)
        ])
        class_reltype = dict((key, rel_types) for key in self.get_classes())
        return dict((key, class_reltype) for key in self.get_classes())

    def get_classes(self) -> dict[str, None]:
        """
        Get a dictionary of class names.

        Returns:
            dict[str, None]: An dictionary where keys are class names (str) and values are None.
        """
        return dict((c.get_name(), None) for c in self._diagram.get_all_classes())

    def get_methods(self) -> dict[str, set[str]]:
        """
        Get a dictionary of methods for each class.

        Returns:
            dict[str, set[str]]: A dictionary where keys are class names (str) and
                                        values are sets containing names of methods (str) for each class.
        """
        res = dict()
        for uml_class in self._diagram.get_all_classes():
            methods = set()
            for method in uml_class.get_methods():
                methods.add(method.get_name())
            if methods:
                res[uml_class.get_name()] = methods
        return res

    def get_fields(self) -> dict[str, set[str]]:
        """
        Get a dictionary of fields for each class.

        Returns:
            dict[str, set[str]]: A dictionary where keys are class names (str) and
                                        values are sets containing names of fields (str) for each class.
        """
        res = dict()
        for uml_class in self._diagram.get_all_classes():
            fields = set()
            for field in uml_class.get_fields():
                fields.add(field.get_name())
            if fields:
                res[uml_class.get_name()] = fields
        return res

    def get_params(self) -> dict[str, dict[str, set[str]]]:
        """
        Retrieve parameters of methods in each class.

        Returns:
            dict[str, dict[str, set[str]]]: A dictionary where keys are class names and values
            are dictionaries containing method names as keys and sets of parameter names as values.
        """
        res = dict()
        for uml_class in self._diagram.get_all_classes():
            nested_dict = None
            for method in uml_class.get_methods():
                params = set()
                for param in method.get_params():
                    params.add(param.get_name())
                if params:
                    nested_dict = {method.get_name(): params}
            if nested_dict:
                res[uml_class.get_name()] = nested_dict
        return res
