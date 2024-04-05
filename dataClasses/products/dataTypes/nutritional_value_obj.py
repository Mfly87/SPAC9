from .abs_obj import AbsObj
from ..guardFunctions.float_guard import float_is_zero_or_greater

class NutritionalValueObj(AbsObj):
    
    def __init__(self, calories:float, protein:float, fat:float, sodium:float, fiber:float, carbohydrates:float, sugars:float, potassium:float, vitamins:float) -> None:
        self._calories:float = None
        self.calories:float = calories

        self._protein:float = None
        self.protein:float = protein

        self._fat:float = None
        self.fat:float = fat

        self._sodium:float = None
        self.sodium:float = sodium

        self._fiber:float = None
        self.fiber:float = fiber

        self._carbohydrates:float = None
        self.carbohydrates:float = carbohydrates

        self._sugars:float = None
        self.sugars:float = sugars

        self._potassium:float = None
        self.potassium:float = potassium

        self._vitamins:float = None
        self.vitamins:float = vitamins

    @property
    def calories(self) -> float:
        return self._calories
    @calories.setter
    def calories(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._calories = _value

    @property
    def protein(self) -> float:
        return self._protein
    @protein.setter
    def protein(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._protein = _value
            
    @property
    def fat(self) -> float:
        return self._fat
    @fat.setter
    def fat(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._fat = _value

    @property
    def sodium(self) -> float:
        return self._sodium
    @sodium.setter
    def sodium(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._sodium = _value

    @property
    def fiber(self) -> float:
        return self._fiber
    @fiber.setter
    def fiber(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._fiber = _value
            
    @property
    def carbohydrates(self) -> float:
        return self._carbohydrates
    @carbohydrates.setter
    def carbohydrates(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._carbohydrates = _value

    @property
    def sugars(self) -> float:
        return self._sugars
    @sugars.setter
    def sugars(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._sugars = _value

    @property
    def potassium(self) -> float:
        return self._potassium
    @potassium.setter
    def potassium(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._potassium = _value
            
    @property
    def vitamins(self) -> float:
        return self._vitamins
    @vitamins.setter
    def vitamins(self, value) -> None:
        _value = float_is_zero_or_greater(value)
        if _value is not None:
            self._vitamins = _value

    @staticmethod
    def get_headers() -> list[str]:
        return [
            "calories",
            "protein", 
            "fat", 
            "sodium", 
            "fiber",
            "carbohydrates", 
            "sugars", 
            "potassium", 
            "vitamins",
            ]
    
    @staticmethod
    def get_types() -> list[type]:
        return [float, float, float, float, float, float, float, float, float]
    
    def to_list(self) -> list[any]:
        return[
            self.calories,
            self.protein, 
            self.fat, 
            self.sodium, 
            self.fiber,
            self.carbohydrates, 
            self.sugars, 
            self.potassium, 
            self.vitamins,
            ]
        
    def to_string(self) -> str:
        _zip = zip(self.get_headers(), self.to_list())
        _list = ["%s: %s" % (a[0:3], b) for a, b in _zip]
        return " | ".join(_list)