from dataClasses.products import AbsObj

class MySQLQueryGenerator():

    @staticmethod
    def drop_table_for_class(class_type: AbsObj | type) -> str:
        _table_name = MySQLQueryGenerator._get_table_name(class_type)
        return "DROP TABLE IF EXISTS %s" % (_table_name)
    
    @staticmethod
    def generate_table_for_class(class_type: AbsObj | type) -> str:
        _table_name = MySQLQueryGenerator._get_table_name(class_type)
        _column_definitions = MySQLQueryGenerator._get_column_definitions(class_type)
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (_table_name, _column_definitions)
        
    @staticmethod
    def generate_insert_query(class_type: AbsObj | type) -> str:
        _table_name = MySQLQueryGenerator._get_table_name(class_type)
        _column_names = MySQLQueryGenerator._get_column_names(class_type)
        _column_values = MySQLQueryGenerator._get_column_values(class_type)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names, _column_values)
        
    @staticmethod
    def generate_insert_many_query(class_type: AbsObj | type) -> str:
        _table_name = MySQLQueryGenerator._get_table_name(class_type)
        _column_names = MySQLQueryGenerator._get_column_names(class_type)
        _column_symbols = MySQLQueryGenerator._get_column_symbols(class_type)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names, _column_symbols)

    @staticmethod
    def generate_search_query(class_type: AbsObj | type, *, search_term: str = "", output_rows: str = "*") -> str:
        _table_name = MySQLQueryGenerator._get_table_name(class_type)
        _query = "SELECT %s FROM %s %s" % (output_rows, _table_name, search_term)
        return _query.strip()
    
    @staticmethod
    def generate_update_query(unique_data: AbsObj) -> str:
        _table_name = MySQLQueryGenerator._get_table_name(unique_data)
        _unique_data_update_values = MySQLQueryGenerator._unique_data_update_values(unique_data)
        return "UPDATE %s SET %s WHERE id='%s'" % (_table_name, _unique_data_update_values, unique_data.id)



    @staticmethod
    def _get_column_values(unique_data: AbsObj):
        _list = unique_data.to_list()
        return ", ".join(_list)
    
    @staticmethod
    def _unique_data_update_values(unique_data: AbsObj):
        _headers = unique_data.get_headers()
        _sql_value_list = MySQLQueryGenerator._sql_value_list(unique_data)
        _zip = ["%s = %s" % (a, b) for a, b in zip(_headers, _sql_value_list)]
        return ", ".join(_zip)

    @staticmethod
    def _sql_value_list(unique_data: AbsObj) -> list[str]:
        _list = []
        for _item in unique_data.to_list():
            if isinstance(_item, str):
                _list.append("'%s'" % (_item))
            else:
                _list.append("%s" % (_item))
        return _list




    @staticmethod
    def _get_sql_data_type_list(class_type: AbsObj | type) -> str:
        _type_list = class_type.get_types()
        return map(MySQLQueryGenerator._get_sql_data_type, _type_list)

    @staticmethod
    def _get_sql_data_type(var_type: type) -> str:
        if var_type is int:
            return "INT"
        else:
            return "VARCHAR(255)"
        
    @staticmethod
    def _get_table_name(class_type: type | AbsObj) -> str:
        if not isinstance(class_type, str):
            if not isinstance(class_type, type):
                class_type = class_type.__class__
            class_type = class_type.__name__
        return str(class_type)
        
    @staticmethod
    def _get_column_names(class_type: AbsObj):
        _headers = class_type.get_headers()
        return ', '.join(_headers)
        
    @staticmethod
    def _get_column_symbols(class_type: AbsObj):
        _headers = class_type.get_headers()
        _column_symbols = ['%s'] * len(_headers)
        return ', '.join(_column_symbols)





    @staticmethod
    def _get_column_definitions(class_type: AbsObj) -> str:
        _sql_definition_list = MySQLQueryGenerator._get_sql_definition_list(class_type)
        _sql_definition_list[0] = "%s UNIQUE" % (_sql_definition_list[0])
        return ', '.join(_sql_definition_list)
        
    @staticmethod
    def _get_sql_definition_list(class_type: AbsObj) -> str:
        _headers = class_type.get_headers()
        _types = MySQLQueryGenerator._get_sql_data_type_list(class_type)
        return ["%s %s" % (a, b) for a, b in zip(_headers, _types)]
        