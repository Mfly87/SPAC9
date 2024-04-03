from .dataTypes import Book, User, Name, Address

class DataFactory():

    @staticmethod
    def create_book(ISBN: str, title: str, author: Name, publishing_year: int) -> list[Book]:
        return [Book(ISBN, title, author, publishing_year)]

    @staticmethod
    def create_user(id: str, name: Name, address: Address) -> list[User]:
        return [User(id, name, address)]

    @staticmethod
    def create_name(name_first: str, name_last: str) -> list[Name]:
        return [Name(name_first, name_last)]

    @staticmethod
    def create_address(street: str, number: int) -> list[Name]:
        return [Name(street, number)]
