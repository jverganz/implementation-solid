from abc import ABC, abstractmethod

# Connection Interface
class ConnectionInterface(ABC):

    @abstractmethod
    def get_data(self):
        raise NoImplementedError
    
    @abstractmethod
    def set_data(self):
        raise NoImplementedError