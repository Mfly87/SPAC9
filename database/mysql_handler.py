from .mysql_query_generator import MySQLQueryGenerator
from mysql.connector import MySQLConnection, Error

from designPatterns import Singleton

from dataClasses.products import AbsSQLObj


class MySQLHandler(Singleton):

    _current_database: str = ""
    _database_connector: MySQLConnection = None

    _table_classes: dict[str, AbsSQLObj | type] = dict()
    '''
    def __init__(self, database_connector: MySQLConnection) -> None:
        self._database_connector: MySQLConnection = database_connector
    '''

    def connect_to_server(self, database_connector: MySQLConnection) -> None:
        self._database_connector: MySQLConnection = database_connector


        '''self._update_table_classes()
    
    def _update_table_classes(self):
        self._table_classes.clear()
        classes = getmembers(dataTypes, lambda m: isclass(m) and not isabstract(m) )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbsObj):
                _table_name = MySQLQueryGenerator._get_table_name(_type)
                self._table_classes.update([[_table_name, _type]])'''

    @property
    def database_connector(self) -> MySQLConnection:
        return self._database_connector
    
    @property
    def current_database(self):
        return self._current_database
    
    @property
    def table_classes(self) -> dict[str, AbsSQLObj | type]:
        return self._table_classes
    





    def get_table_types(self) -> list[AbsSQLObj | type]:
        _name_list = self.get_table_names()
        _type_list = []
        for _name in _name_list:
            if _name in self.table_classes.keys():
                _type_list.append(self.table_classes[_name])
        return _type_list

    def get_table_names(self) -> list[str]:
        _query = "SHOW TABLES"
        _result: list[dict[str,str]] = self.execute_fetch_querty(_query)
        _name_list: list[str] = []
        for _dict in _result:
            for _value in _dict.values():
                _name_list.append(_value)
        return _name_list
    
    def connect_to_database(self, database_name: str):
        _creation_query = "CREATE DATABASE IF NOT EXISTS %s" % (database_name)
        self.execute_querty(_creation_query)

        _connection_query = "USE %s" % (database_name)
        self.execute_querty(_connection_query)

        self._current_database = database_name

    # This function should likely stored somewhere else, simply because of the danger
    def drop_table(self, class_type: AbsSQLObj | type) -> None:
        _query = MySQLQueryGenerator.drop_table_for_class(class_type)
        self.execute_querty(_query)


    def create_table(self, class_type: AbsSQLObj) -> None:
        _create_table_query = MySQLQueryGenerator.generate_table_for_class(class_type)
        self.execute_querty(_create_table_query)

    def search(self, class_type: AbsSQLObj | type,*, search_term: str = "") -> list[dict[str,any]]:
        if search_term:
            search_term = " WHERE " + search_term
        _query = MySQLQueryGenerator().generate_search_query(class_type, search_term = search_term)
        _dict_list = self.execute_fetch_querty(_query)
        for _dict in _dict_list:
            _dict |= {"class": class_type.__name__}
        return _dict_list
        
    def update_item(self, unique_data: AbsSQLObj):
        _query = MySQLQueryGenerator.generate_update_query(unique_data)
        self.execute_querty(_query)
        
    def add_item(self, unique_data: AbsSQLObj):
        _query = MySQLQueryGenerator.generate_insert_query(unique_data)
        self.execute_querty(_query)








    def insert_many_querty(self, _unique_data_list: list[AbsSQLObj]) -> bool:
        if not _unique_data_list:
            return
        
        class_type = type(_unique_data_list[0])
        _fill_table_query = MySQLQueryGenerator.generate_insert_many_query(class_type)

        try:
            with self.database_connector.cursor() as cursor:
                library_data = []
                for _unique_data in _unique_data_list:
                    _values = MySQLQueryGenerator._get_values(_unique_data)
                    library_data.append(tuple(_values))
                cursor.executemany(_fill_table_query, library_data)
                self.database_connector.commit()
                return True
        except Error as e:
            print(f"An error occured during an executemany query {e}")
            return False
        
    def execute_querty(self, _query: str) -> bool:
        try:
            with self.database_connector.cursor() as cursor:
                cursor.execute(_query)
                self.database_connector.commit()
                return True
        except Error as e:
            print(f"An error occured during an execute query {e}")
            return False
        
    def execute_fetch_querty(self, _query: str) -> list[dict]:
        try:
            with self.database_connector.cursor(dictionary=True) as cursor:
                cursor.execute(_query)
                return cursor.fetchall()
        except Error as e:
            print(f"An error occured during a fetch query {e}")
            return []
