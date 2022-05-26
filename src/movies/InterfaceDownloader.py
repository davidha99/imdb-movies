from abc import ABC, abstractmethod

class InterfaceDownloader(ABC):
    
    @abstractmethod
    def download(self):
        pass