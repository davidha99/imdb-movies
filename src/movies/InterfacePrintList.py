from abc import ABC, abstractmethod

#Strategy design pattern
class InterfacePrintList(ABC):
    
    @abstractmethod
    def printList(self):
        pass