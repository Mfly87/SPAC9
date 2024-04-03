from .abs_data_type import AbsDataType

class Name(AbsDataType):
    def __init__(self, name_first:str, name_last:str) -> None:
        self._name_first = name_first
        self._name_last = name_last

    @property
    def name_first(self) -> str:
        return self._name_first

    @property
    def name_last(self) -> str:
        return self._name_last

    @property
    def name_full(self) -> str:
        return "%s %s" % (self.name_first, self.name_last)
    
    def to_string(self):
        return self.name_full