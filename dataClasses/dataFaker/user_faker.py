from ..data_factory import DataFactory, User
from .abs_faker import AbsFaker

from .address_faker import AddressFaker
from .name_faker import NameFaker

class UserFaker(AbsFaker):

    _address_faker = AddressFaker()
    _name_faker = NameFaker()

    @property
    def address_faker(self) -> AddressFaker:
        return self._address_faker
    @property
    def name_faker(self) -> NameFaker:
        return self._name_faker

    def generate_data_user(self) -> list[User]:

        return DataFactory.create_user(
            str(self.get_generation_counter()).zfill(4),
            self.name_faker.generate_data_name()[0],
            self.address_faker.generate_data_address()[0],
        )