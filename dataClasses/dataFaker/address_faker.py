from ..data_factory import DataFactory, Address
from .abs_faker import AbsFaker

class AddressFaker(AbsFaker):

    def generate_data_address(self) -> list[Address]:
        return DataFactory.create_address(
            self.generate_street_name(),
            self.generate_int(1,30)
        )
