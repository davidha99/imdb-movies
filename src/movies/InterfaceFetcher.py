from abc import ABC, abstractmethod

class InterfaceFetcher(ABC):
    
    @abstractmethod
    def fetch_movies(self):
        pass