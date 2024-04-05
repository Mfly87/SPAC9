from dataClasses.products import CerealObj, AbsSQLObj, ProductFactory
from importFiles.ceral_csv_reader import get_objects_from_Cereal_csv

from database import MySQLServerCredentials, MySQLServerConnection, MySQLHandler, MySQLQueryGenerator

from faker import Faker
from app import app

print("\n\n")

Faker.seed(0)
cereal_csv_path = "importFiles/Cereal.csv"

_database_name = "spac9"

_credentials = MySQLServerCredentials(
    "localhost",
    "root",
    "Kom12345",
    3306
)

_list:list[CerealObj] = get_objects_from_Cereal_csv(cereal_csv_path)

mysql_server: MySQLServerConnection = MySQLServerConnection()
mysql_server.connect_to_server(_credentials)

#sql_handler = MySQLHandler(mysql_server.mysql_connection)
sql_handler:MySQLHandler = MySQLHandler()
sql_handler.connect_to_server(mysql_server.mysql_connection)

sql_handler.connect_to_database(_database_name)
sql_handler.drop_table(CerealObj)
sql_handler.create_table(CerealObj)
_ret = sql_handler.insert_many_querty(_list)

#app.run(debug=True)

print(len(sql_handler.search(CerealObj)))

_obj = _list[0]
abc = "abcdefghijklemnopqrs"
for i in range(10):
    _obj.id = abc[i:i+4]
    sql_handler.insert_many_querty([_obj])



print(len(sql_handler.search(CerealObj)))