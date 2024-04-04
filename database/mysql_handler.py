from dataClasses.products import AbsObj
from .mysql_query_generator import MySQLQueryGenerator

from inspect import getmembers, isclass, isabstract
from mysql.connector import MySQLConnection, Error


class MySQLHandler:

    _current_database: str = ""
    _table_classes: dict[str, AbsObj | type] = dict()

    def __init__(self, database_connector: MySQLConnection) -> None:
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
    def table_classes(self) -> dict[str, AbsObj | type]:
        return self._table_classes
    





    def get_table_types(self) -> list[AbsObj | type]:
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
    def drop_table(self, class_type: AbsObj | type) -> None:
        _query = MySQLQueryGenerator.drop_table_for_class(class_type)
        self.execute_querty(_query)


    def create_table(self, unique_data_list: list[AbsObj]) -> None:
        if not unique_data_list:
            return
        
        class_type = type(unique_data_list[0])

        _create_table_query = MySQLQueryGenerator.generate_table_for_class(class_type)
        self.execute_querty(_create_table_query)

        _fill_table_query = MySQLQueryGenerator.generate_insert_many_query(class_type)
        self.execute_many_querty(_fill_table_query, unique_data_list)

    def search(self, class_type: AbsObj | type,*, search_term: str = ""):
        _query = MySQLQueryGenerator().generate_search_query(class_type, search_term = search_term)
        return self.execute_fetch_querty(_query)
        
    def update_item(self, unique_data: AbsObj):
        _query = MySQLQueryGenerator.generate_update_query(unique_data)
        self.execute_querty(_query)
        
    def add_item(self, unique_data: AbsObj):
        _query = MySQLQueryGenerator.generate_insert_query(unique_data)
        print(_query)
        self.execute_querty(_query)








    def execute_many_querty(self, _query: str, _unique_data_list: list[AbsObj]) -> bool:
        try:
            with self.database_connector.cursor() as cursor:
                library_data = []
                for _unique_data in _unique_data_list:
                    library_data.append(tuple(_unique_data.to_list()))
                cursor.executemany(_query, library_data)
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
