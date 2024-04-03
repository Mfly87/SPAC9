from .abs_data_type import AbsDataType
from .name import Name
from .address import Address

class User(AbsDataType):
    def __init__(self, id: str, name: Name, address: Address) -> None:
        self._id = id
        self._name = name
        self._address = address

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> Name:
        return self._name

    @property
    def address(self) -> Address:
        return self._address
    
    def to_string(self) -> str:
        return "(%s) %s, %s" % (
            self.id,
            self.name.to_string(),
            self.address.to_string(),
        )