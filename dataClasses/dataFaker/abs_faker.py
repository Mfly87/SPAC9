from faker import Faker
import abc

class AbsFaker(abc.ABC):
    
    _generation_counter: int = 0

    def __init__(self) -> None:
        self._faker: Faker = Faker()

    @property
    def faker(self) -> Faker:
        return self._faker
    
    def get_generation_counter(self) -> int:
        self._generation_counter += 1
        return self._generation_counter

    def generate_first_name(self) -> str:
        return self.faker.first_name()
    
    def generate_first_name_male(self) -> str:
        return self.faker.first_name_male()
    
    def generate_first_name_female(self) -> str:
        return self.faker.first_name_female()
        
    def generate_last_name(self) -> str:
        return self.faker.last_name()
    
    def generate_street_name(self) -> str:
        return self.faker.street_name()

    def generate_int(self, min : int, max : int) -> int:
        return self.faker.pyint(min_value = min, max_value = max)
    
    def generate_business_sentence(self) -> str:
        return self.faker.bs()
    
    def get_fake_ISBN13(self) -> str:
        return self.faker.isbn13()