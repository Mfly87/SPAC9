import abc

class AbsDataType(abc.ABC):
    
    '''Base class for all data types.'''


    @abc.abstractmethod
    def to_string(self) -> str:
        '''Prints a string of the object that's easily readable in the terminal.'''
        pass