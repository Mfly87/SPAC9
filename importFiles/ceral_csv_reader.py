from dataClasses.products import AbsObj, NutritionalValueObj, CerealObj, ProductFactory
import csv

_serve_type_dict = {
    "H": "Hot",
    "C": "Cold"
}

_company_dict = {
    "A": "American Home Food Products",
    "G": "General Mills",
    "K": "Kelloggs",
    "N": "Nabisco",
    "P": "Post",
    "Q": "Quaker Oats",
    "R": "Ralston Purina",
}
    
def get_objects_from_Cereal_csv(path:str, *, delimiter = ";", rows_skipped:int = 2) -> list[NutritionalValueObj]:

    _list:list[NutritionalValueObj] = []

    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for _ in range(rows_skipped):
            next(reader)  # Skip the header line
        for row in reader:
            replace_shorthand(row)

            row.insert(0, "")
            row.insert(0, CerealObj.__name__)
            for _obj in ProductFactory.create_from_build_values(row):
                _list.append(_obj)

            #_build_dict = build_factory_dict(row)
            #for _obj in ProductFactory.create_from_dict(**_build_dict):
            #    _list.append(_obj)
    return _list

def replace_shorthand(row:list[str]) -> None:
    replace_dict_index(row, 1, _company_dict)
    replace_dict_index(row, 2, _serve_type_dict)

def replace_dict_index(row:list[str], index:int, replacement_dict:dict[str,str]) -> None:
    _key = row[index]
    row[index] = replacement_dict[_key]

def build_factory_dict(row:list[str]) -> dict[str,any]:
    _nutrition_values = row[3:12]
    _nutrition_build_dict = dict_from_rows(NutritionalValueObj, _nutrition_values)

    _cereal_values = row[:3] + [_nutrition_build_dict] + row[12:]
    _cereal_build_dict = dict_from_rows(CerealObj, _cereal_values)

    return _cereal_build_dict

def dict_from_rows(class_type:AbsObj, values:list[any]):
    _dict = dict(zip(class_type.get_headers(), values))
    _dict |= {"class": class_type.__name__}
    return _dict