from abc import abstractmethod, ABC

class UML_Named_Object(ABC):

    def __init__ (self, name:str):
        self._name = name
    
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError
    
    @abstractmethod 
    def set_name(self, new_name:str) -> None:
        raise NotImplementedError           
