from .dataTypes import AbsObj, NutritionalValueObj, CerealObj

from typing import Callable

class DataFactory():
    
    @staticmethod
    def _create_list_of_valid_objects(_obj: AbsObj) -> list[AbsObj]:
        return [_obj] if _obj.is_valid() else []
    
    @staticmethod
    def create_from_dict(**kwargs) -> list[AbsObj]:

        for _key in kwargs:
            _value = kwargs[_key]
            if not isinstance(_value, dict):
                continue
            
            _obj_list: list[AbsObj] = DataFactory.create_from_dict(**_value)
            _new_value = _obj_list[0] if _obj_list else None
            kwargs |= {_key: _new_value}

        _class_name = kwargs.get("class", "")
        func = DataFactory._get_creation_func(_class_name)

        del kwargs["class"]

        return func(**kwargs)

    @staticmethod
    def _get_creation_func(class_name:str) -> Callable[[dict[str, any]], list[AbsObj]]:
        match class_name:
            case NutritionalValueObj.__name__:
                return DataFactory.create_nutritional_value
            case CerealObj.__name__:
                return DataFactory.create_cereal
            case _:
                return DataFactory.create_null

    @staticmethod
    def create_null(*args, **kwargs) -> list[AbsObj]:
        return []

    @staticmethod
    def create_nutritional_value(*, calories:float, protein:float, fat:float, sodium:float, fiber:float, carbohydrates:float, sugars:float, potassium:float, vitamins:float) -> list[NutritionalValueObj]:
        _obj = NutritionalValueObj(calories, protein, fat, sodium, fiber, carbohydrates, sugars, potassium, vitamins)
        return DataFactory._create_list_of_valid_objects( _obj )
    
    @staticmethod
    def create_cereal(*, name:str, manufacturer:str, serve_type:str, nutritions:NutritionalValueObj, shelf_number:int, weight_per_serving:float, cups_per_serving:float, rating:float) -> list[NutritionalValueObj]:
        _obj = CerealObj(name, manufacturer, serve_type, nutritions, shelf_number, weight_per_serving, cups_per_serving, rating)
        return DataFactory._create_list_of_valid_objects( _obj )
    