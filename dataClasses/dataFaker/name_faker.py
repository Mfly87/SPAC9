from ..data_factory import DataFactory, Name
from .abs_faker import AbsFaker

class NameFaker(AbsFaker):

    def generate_data_name(self) -> list[Name]:
        return DataFactory.create_name(
            self.generate_first_name(),
            self.generate_last_name()
        )
