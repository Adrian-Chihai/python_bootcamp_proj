import sqlite3
class SQLiteConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def __init__(self):
        self._connection = None

    @property
    def connection(self):
        if self._connection is None:
            self.connect()
        return self._connection

    def connect(self, db_name=":memory:"):
        try:
            self._connection = sqlite3.connect(db_name)
            print("Connection successfully established")
        except sqlite3.Error as e:
            print(f"Error while connecting to the database: {e}")

    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None
            print("Disconnected from the database")