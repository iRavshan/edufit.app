from uuid import UUID
from abc import abstractmethod
from django.shortcuts import get_list_or_404, get_object_or_404
from typing import List
from common.repositories import AbstractBaseRepository
from ..models import Test


class _AbstractTestRepository(AbstractBaseRepository[Test]):
    pass


class TestRepository(_AbstractTestRepository):
    def get_all(self) -> List[Test]:
        return get_list_or_404(Test)
    
    def get_by_id(self, id: int) -> Test:
        return get_object_or_404(Test, id=id)
    
    def create(self, **kwargs) -> Test:
        return super().create(**kwargs)
    
    def update(self, id: int, **kwargs) -> Test:
        return super().update(id, **kwargs)
    
    def delete(self, id: int) -> None:
        return super().delete(id)