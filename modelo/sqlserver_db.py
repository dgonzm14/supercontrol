
import pyodbc
from abc import ABC, ABCMeta


class SingletonMeta(ABCMeta):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseInterface(ABC):
    pass


class SqlServerDatabase(DatabaseInterface, metaclass=SingletonMeta):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = pyodbc.connect(self.connection_string)
            except Exception as e:
                print("Error al conectar a la base de datos:", e)
                self.conn = None

    def get_connection(self):
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute(self, query, params=None):
        if not self.conn:
            raise Exception("No hay conexión establecida")
        cursor = self.conn.cursor()
        cursor.execute(query, params or [])
        return cursor

    def commit(self):
        if self.conn:
            self.conn.commit()

