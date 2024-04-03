from .abs_data_type import AbsDataType
from .name import Name

class Book(AbsDataType):
    def __init__(self, ISBN: str, title: str, author: Name, publishing_year: int) -> None:
        self._ISBN:str = ISBN
        self._title:str = title
        self._author:Name = author
        self._publishing_year:int = publishing_year

    @property
    def ISBN(self) -> str:
        return self._ISBN

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> Name:
        return self._author

    @property
    def publishing_year(self) -> int:
        return self._publishing_year
    
    def to_string(self):
        return "\'%s\' by %s (%i) ISBN: %s" % (
            self.title,
            self.author.name_full,
            self.publishing_year,
            self.ISBN
        )