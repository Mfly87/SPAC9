class Book():
    def __init__(self, ISBN: str, title: str, author: str, publishing_year: int) -> None:
        self._ISBN:str = ISBN
        self._title:str = title
        self._author:str = author
        self._publishing_year:int = publishing_year

    @property
    def ISBN(self) -> str:
        return self._ISBN

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def publishing_year(self) -> int:
        return self._publishing_year