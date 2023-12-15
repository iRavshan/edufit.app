from abc import ABC, abstractmethod
from typing import List, Type, TypeVar

T = TypeVar('T')

class BaseRepository(ABC):
    @abstractmethod
    def get(self, pk) -> T:
        pass

    @abstractmethod
    def all(self) -> List[T]:
        pass

    @abstractmethod
    def create(self, **kwargs) -> T:
        pass

    @abstractmethod
    def update(self, instance: T, **kwargs) -> T:
        pass

    @abstractmethod
    def delete(self, instance: T) -> None:
        pass