from uuid import UUID
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class AbstractBaseRepository(ABC, Generic[T]):

    @abstractmethod
    def get_by_id(self, id: int | UUID) -> T:
        pass


    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    
    @abstractmethod
    def create(self, **kwargs) -> T:
        pass


    @abstractmethod
    def update(self, id: int | UUID, **kwargs) -> T:
        pass


    @abstractmethod
    def delete(self, id: int | UUID) -> None:
        pass