from design_patterns import Singleton
from mysql.connector import MySQLConnection, Error
from mysql import connector

from .mysql_server_credentials import MySQLServerCredentials


class MySQLServerConnection(Singleton):

    _mysql_connection: MySQLConnection = None

    def connect_to_server(self, credentials: MySQLServerCredentials) -> MySQLConnection:
        self.close_connection()

        try:
            mysql_connection = connector.connect(**credentials.get_credentials_dict())
            self._mysql_connection = mysql_connection
        except Error as e:
            print(f"Error connecting to the server: {e}")
            raise

    def close_connection(self) -> None:
        if self.mysql_connection is None:
            return
        try:
            self.mysql_connection.close()
            self._mysql_connection = None
        except Error as e:
            print(f"An error occoured whilst closing the server connection: {e}")
            raise

    @property
    def mysql_connection(self):
        return self._mysql_connection