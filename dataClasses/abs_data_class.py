import abc

class AbsDataClass(abc.ABC):

    @abc.abstractmethod
    def to_string(self) -> str:
        pass