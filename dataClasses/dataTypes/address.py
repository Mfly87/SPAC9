from .abs_data_type import AbsDataType

class Address(AbsDataType):
    def __init__(self, street:str, number:int) -> None:
        self._street = street
        self._number = number

    @property
    def street(self) -> str:
        return self._street

    @property
    def number(self) -> int:
        return self._number
    
    def to_string(self):
        return "%s %i" % (
            self.street,
            self.number
        )