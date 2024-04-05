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

sql_handler = MySQLHandler(mysql_server.mysql_connection)
sql_handler.connect_to_database(_database_name)
sql_handler.drop_table(CerealObj)
sql_handler.create_table(CerealObj)

_ret = sql_handler.execute_insert_many_querty(_list)
print(_ret)

'''
_obj = _list[0]

_zip = zip(_obj.get_build_headers(type(_obj)), _obj.get_build_types(type(_obj)), _obj.get_build_values())

for _a, _b, _c in _zip:
    print(_a)
    print(_b)
    print(_c)

    print("")
'''

#app.run(debug=True)