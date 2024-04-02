class User():
    def __init__(self, id, name_first, name_last) -> None:
        self._id = id
        self._name_first = name_first
        self._name_last = name_last

    @property
    def id(self) -> str:
        return self._id

    @property
    def name_first(self) -> str:
        return self._name_first

    @property
    def name_last(self) -> str:
        return self._name_last

    @property
    def name_full(self) -> str:
        return "%s %s" % (self.name_first, self.name_last)