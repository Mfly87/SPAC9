from .abs_obj import AbsSQLObj

from ..guardFunctions.float_guard import float_is_zero_or_greater
from ..guardFunctions.int_guard import int_is_zero_or_greater, int_is_one_or_greater
from ..guardFunctions.string_guard import str_is_not_empty

from .nutritional_value_obj import NutritionalValueObj

class CerealObj(AbsSQLObj):
    def __init__(self, id:str, name:str, manufacturer:str, serve_type:str, nutritions:NutritionalValueObj, shelf_number:int, weight_per_serving:float, cups_per_serving:float, rating:int) -> None:
        
        self._id:str = None
        self.id:str = id

        self._name:str = None
        self.name:str = name

        self._manufacturer:str = None
        self.manufacturer:str = manufacturer

        self._serve_type:str = None
        self.serve_type:str = serve_type

        self._nutritions:NutritionalValueObj = None
        self.nutritions:NutritionalValueObj = nutritions

        self._shelf_number:int = None
        self.shelf_number:int = shelf_number

        self._weight_per_serving:float = None
        self.weight_per_serving:float = weight_per_serving

        self._cups_per_serving:float = None
        self.cups_per_serving:float = cups_per_serving

        self._rating:int = None
        self.rating:int = rating

    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, value) -> None:
        _value = str_is_not_empty(value)
        if _value is not None:
            self._id = _value


    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value) -> None:
        _value = str_is_not_empty(value)
        if _value is not None:
            self._name = _value

    @property
    def manufacturer(self) -> str:
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, value) -> None:
        _value = str_is_not_empty(value)
        if _value is not None:
            self._manufacturer = _value

    @property
    def serve_type(self) -> str:
        return self._serve_type
    @serve_type.setter
    def serve_type(self, value) -> None:
        _value = str_is_not_empty(value)
        if _value is not None:
            self._serve_type = _value

    @property
    def nutritions(self) -> NutritionalValueObj:
        return self._nutritions
    @nutritions.setter
    def nutritions(self, value) -> None:
        if not isinstance(value, NutritionalValueObj):
            return
        if not value.is_valid():
            return
        self._nutritions = value

    @property
    def shelf_number(self) -> int:
        return self._shelf_number
    @shelf_number.setter
    def shelf_number(self, value) -> None:
        _value = int_is_one_or_greater(value)
        if _value is not None:
            self._shelf_number = _value

    @property
    def weight_per_serving(self) -> float:
        return self._weight_per_serving
    @weight_per_serving.setter
    def weight_per_serving(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._weight_per_serving = _value

    @property
    def cups_per_serving(self) -> float:
        return self._cups_per_serving
    @cups_per_serving.setter
    def cups_per_serving(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._cups_per_serving = _value

    @property
    def rating(self) -> int:
        return self._rating
    @rating.setter
    def rating(self, value) -> None:
        _value = int_is_zero_or_greater(value)
        if _value is not None:
            self._rating = _value

    @staticmethod
    def get_headers() -> list[str]:
        return [
            "id", 
            "name", 
            "manufacturer",
            "serve_type", 
            "nutritions", 
            "shelf_number", 
            "weight_per_serving", 
            "cups_per_serving", 
            "rating",
            ]
    
    @staticmethod
    def get_types() -> list[type]:
        return [str, str, str, str, NutritionalValueObj, int, float, float, int]
    
    def to_list(self) -> list[any]:
        return [
            self.id, 
            self.name, 
            self.manufacturer,
            self.serve_type,
            self.nutritions, 
            self.shelf_number, 
            self.weight_per_serving, 
            self.cups_per_serving, 
            self.rating,
            ]
    
    def to_string(self) -> str:
        _zip = zip(self.get_headers(), self.to_list())
        _list = ["%s: %s" % (a.split("_")[0], b) for a, b in _zip]
        del _list[4]
        return " | ".join(_list)