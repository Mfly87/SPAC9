from ...abs_data_class import AbsDataClass
import abc

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
        _dict = dict(zip(self.get_headers(), self.to_list()))
        _dict |= {"class": self.__class__.__name__}
        return _dict
    
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