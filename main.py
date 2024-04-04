from dataClasses.products import CerealObj
from importFiles.ceral_csv_reader import get_objects_from_Cereal_csv

from app import app

print("\n\n")


cereal_csv_path = "importFiles/Cereal.csv"

_list:list[CerealObj] = get_objects_from_Cereal_csv(cereal_csv_path)
for _item in _list:
    print(_item.to_string())

#app.run(debug=True)