from .abs_obj import AbsObj

from ..guardFunctions.float_guard import float_is_zero_or_greater, float_is_between_one_and_one_hundred
from ..guardFunctions.int_guard import int_is_one_or_greater
from ..guardFunctions.string_guard import str_is_not_empty

from .nutritional_value_obj import NutritionalValueObj

class CerealObj(AbsObj):
    def __init__(self, name:str, manufacturer:str, nutritions:NutritionalValueObj, shelf_number:int, weight_per_serving:float, cups_per_serving:float, rating:float) -> None:
        
        self._name:str = None
        self.name:str = name

        self._manufacturer:str = None
        self.manufacturer:str = manufacturer

        self._nutritions:NutritionalValueObj = None
        self.nutritions:NutritionalValueObj = nutritions

        self._shelf_number:int = None
        self.shelf_number:int = shelf_number

        self._weight_per_serving:float = None
        self.weight_per_serving:float = weight_per_serving

        self._cups_per_serving:float = None
        self.cups_per_serving:float = cups_per_serving

        self._rating:float = None
        self.rating:float = rating

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value) -> None:
        _value = str_is_not_empty(value)
        if _value is not None:
            self._name = value

    @property
    def manufacturer(self) -> str:
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, value) -> None:
        _value = str_is_not_empty(value)
        if _value is not None:
            self._manufacturer = value

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
            self._shelf_number = value

    @property
    def weight_per_serving(self) -> float:
        return self._weight_per_serving
    @weight_per_serving.setter
    def weight_per_serving(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._weight_per_serving = value

    @property
    def cups_per_serving(self) -> float:
        return self._cups_per_serving
    @cups_per_serving.setter
    def cups_per_serving(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._cups_per_serving = value

    @property
    def rating(self) -> float:
        return self._rating
    @rating.setter
    def rating(self, value) -> None:
        _value = float_is_between_one_and_one_hundred(value)
        if _value is not None:
            self._rating = value

    @staticmethod
    def get_headers() -> list[str]:
        return [
            "name", 
            "manufacturer", 
            "nutritions", 
            "shelf_number", 
            "weight_per_serving", 
            "cups_per_serving", 
            "rating",
            ]
    
    @staticmethod
    def get_types() -> list[type]:
        return [str, str, NutritionalValueObj, int, float, float, float]
    
    def to_list(self) -> list[any]:
        return [
            self.name, 
            self.manufacturer, 
            None if self.nutritions is None else self.nutritions.to_dict(), 
            self.shelf_number, 
            self.weight_per_serving, 
            self.cups_per_serving, 
            self.rating,
            ]