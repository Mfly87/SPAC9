from ..data_factory import DataFactory, Book
from .abs_faker import AbsFaker

class BookFaker(AbsFaker):

    def generate_data_book(self) -> list[Book]:
        return DataFactory.create_book(
            self.get_fake_ISBN13(),
            self.generate_business_sentence(),
            self.generate_full_name(),
            self.generate_int(1990,2020)
        )
