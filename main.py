from faker import Faker
from dataClasses.dataFaker.user_faker import UserFaker

Faker.seed(0)
f = UserFaker()

for _ in range(100):
    for _book in f.generate_data_user():
        print(_book.to_string())