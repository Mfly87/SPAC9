from .dataTypes import AbsSQLObj, NutritionalValueObj, CerealObj
from faker import Faker
from typing import Callable

class ProductFactory():

    _id_length = 4
    _faker = Faker()
    
    @staticmethod
    def _create_list_of_valid_objects(_obj: AbsSQLObj) -> list[AbsSQLObj]:
        #if not _obj.is_valid():
            #print(_obj.to_string())
        return [_obj] if _obj.is_valid() else []
    

    @staticmethod
    def create_from_build_dict(build_dict: dict[str,any]) -> list[AbsSQLObj]:
        if "class" not in build_dict:
            return []
        _class_name = build_dict["class"]
        _func, _class_type = ProductFactory._get_creation_func(_class_name)
        
        _list_of_headers = _class_type.get_build_headers(_class_type)
        _build_list = []
        for _key in _list_of_headers:
            if _key not in build_dict:
                return []
            _value = build_dict[_key]
            _build_list.append(_value)
        
        return ProductFactory.create_from_build_values(_build_list)
        



    @staticmethod
    def create_from_build_values(build_list: list[any]) -> list[AbsSQLObj]:
        _class_name = build_list[0]
        _func, _class_type = ProductFactory._get_creation_func(_class_name)

        _list_len = len(_class_type.get_build_headers(_class_type))
        if _list_len != len(build_list):
            return []
        build_list = build_list[1:]

        _obj_build_list = []

        for _value_type in _class_type.get_types():
            if not issubclass(_value_type, AbsSQLObj):
                _obj_build_list.append( build_list.pop(0) )
            else:
                _sub_list_len = len(_value_type.get_build_headers(_value_type)) - 1
                
                _sub_list = [_value_type.__name__] + build_list[:_sub_list_len]
                build_list = build_list[_sub_list_len:]
                
                _product_list = ProductFactory.create_from_build_values(_sub_list)
                _product = _product_list[0] if _product_list else None
                _obj_build_list.append( _product )
        
        return _func(*_obj_build_list)


            


    @staticmethod
    def create_from_nested_dict(**kwargs) -> list[AbsSQLObj]:

        for _key in kwargs:
            _value = kwargs[_key]
            if not isinstance(_value, dict):
                continue
            
            _obj_list: list[AbsSQLObj] = ProductFactory.create_from_nested_dict(**_value)
            _new_value = _obj_list[0] if _obj_list else None
            kwargs |= {_key: _new_value}

        _class_name = kwargs.get("class", "")
        _func, _type = ProductFactory._get_creation_func(_class_name)

        del kwargs["class"]

        return _func(**kwargs)

    @staticmethod
    def _get_creation_func(class_name:str) -> tuple[Callable[[dict[str, any]],list[AbsSQLObj]], AbsSQLObj]:
        match class_name:
            case NutritionalValueObj.__name__:
                return ProductFactory.create_nutritional_value, NutritionalValueObj
            case CerealObj.__name__:
                return ProductFactory.create_cereal, CerealObj
            case _:
                return ProductFactory.create_null, None

    @staticmethod
    def create_null(*args, **kwargs) -> list[AbsSQLObj]:
        return []

    @staticmethod
    def create_nutritional_value(calories:float, protein:float, fat:float, sodium:float, fiber:float, carbohydrates:float, sugars:float, potassium:float, vitamins:float) -> list[NutritionalValueObj]:
        _obj = NutritionalValueObj(calories, protein, fat, sodium, fiber, carbohydrates, sugars, potassium, vitamins)
        return ProductFactory._create_list_of_valid_objects( _obj )
    
    @staticmethod
    def create_cereal(id:str, name:str, manufacturer:str, serve_type:str, nutritions:NutritionalValueObj, shelf_number:int, weight_per_serving:float, cups_per_serving:float, rating:float) -> list[NutritionalValueObj]:
        id = ProductFactory._generate_id(id)
        _obj = CerealObj(id, name, manufacturer, serve_type, nutritions, shelf_number, weight_per_serving, cups_per_serving, rating)
        return ProductFactory._create_list_of_valid_objects( _obj )
    
    @staticmethod
    def _generate_id(id:str) -> str:
        if id:
            return id
        _len = ProductFactory._id_length
        return ProductFactory._faker.pystr(min_chars=_len, max_chars=_len).lower()
