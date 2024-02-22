from Models.diagram import Diagram


class Fields:
    def __init__(self, diagram_class):
        self.diagram_class = diagram_class


class Methods:
    def __init__(self, diagram_class):
        self.diagram_class = diagram_class


class Parameters:
    def __init__(self, method):
        self.method = method
