
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def fetchone(self):
        pass

    @abstractmethod
    def fetchall(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def close(self):
        pass
