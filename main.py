from dataClasses.products import CerealObj, AbsObj, ProductFactory
from importFiles.ceral_csv_reader import get_objects_from_Cereal_csv

from database import MySQLServerCredentials, MySQLServerConnection, MySQLHandler

from app import app

print("\n\n")


cereal_csv_path = "importFiles/Cereal.csv"

_database_name = "spac9"

_credentials = MySQLServerCredentials(
    "localhost",
    "root",
    "Kom12345",
    3306
)

mysql_server: MySQLServerConnection = MySQLServerConnection()
mysql_server.connect_to_server(_credentials)

_list:list[CerealObj] = get_objects_from_Cereal_csv(cereal_csv_path)


print(len(_list))
_obj = _list[0]

#print(_obj.get_build_headers(type(_obj)))
print(_obj.to_string())

_out = ProductFactory.create_from_build_values(_obj.get_build_values())
for _o in _out:
    print(_o.to_string())




_o_list: list[AbsObj] = ProductFactory.create_from_nested_dict(**_obj.to_nested_dict())
for _o in _o_list:
    print(_o.to_string())


_o_list: list[AbsObj] = ProductFactory.create_from_build_dict(_obj.to_build_dict())
for _o in _o_list:
    print(_o.to_string())
'''
print(_obj.get_build_values())

'''
'''
sql_handler = MySQLHandler(mysql_server.mysql_connection)
sql_handler.connect_to_database(_database_name)
_ret = sql_handler.get_table_names()

print(_ret)
'''
#app.run(debug=True)