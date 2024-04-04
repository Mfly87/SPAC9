from ...abs_data_class import AbsDataClass
import abc
from typing import Callable
class AbsObj(AbsDataClass):
    
    @abc.abstractstaticmethod
    def get_headers() -> list[str]:
        pass
    
    @abc.abstractstaticmethod
    def get_types() -> list[type]:
        pass
    
    @abc.abstractmethod
    def to_list(self) -> list[any]:
        pass
    
    def to_dict(self) -> dict[str,any]:
        _list = self.to_list()
        for i, _value in enumerate(_list):
            if _value is None:
                continue
            if issubclass(type(_value), AbsObj):
                _list[i] = _value.to_dict()

        _dict = dict(zip(self.get_headers(), _list))
        _dict |= {"class": self.__class__.__name__}
        return _dict
    

    def get_build_values(self) -> list[any]:
        _list_of_values: list = [self.__class__.__name__]
        for _value, _type in zip(self.to_list(), self.get_types()):
            if issubclass(_type, AbsObj):
                _list_of_values += _value.get_build_values()[1:]
            else:
                _list_of_values.append(_value)
        return _list_of_values

    @staticmethod
    def get_build_headers(_class_type) -> list[any]:
        _list_of_headers: list = ["class"]
        for _value, _type in zip(_class_type.get_headers(), _class_type.get_types()):
            if issubclass(_type, AbsObj):
                _list_of_headers += AbsObj.get_build_headers(_type)[1:]
            else:
                _list_of_headers.append(_value)
        return _list_of_headers



    def is_valid(self):
        '''Returns False if any parameters have not been set'''
        _dict_of_obj = self.to_dict()
        return self._is_dict_of_obj_valid(_dict_of_obj)
    
    def _is_dict_of_obj_valid(self, dict_of_obj: dict) -> bool:
        '''Recursivly checks if the dict of an object is valid'''
        for _value in dict_of_obj.values():
            if _value is None:
                return False
            if isinstance(_value, dict):
                if self._is_dict_of_obj_valid(_value):
                    continue
                return False
        return True

    def __eq__(self, __value: object) -> bool:
        '''Ensures the equal opperator functions based on class content'''

        if not isinstance(__value, type(self)):
            return False
        
        _list_a = self.to_list()
        _list_b = __value.to_list()

        for a, b in zip(_list_a, _list_b):
            if a != b:
                return False
            
        return True