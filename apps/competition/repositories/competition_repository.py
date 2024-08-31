from uuid import UUID
from abc import abstractmethod
from django.shortcuts import get_list_or_404, get_object_or_404
from typing import List
from common.repositories import AbstractBaseRepository
from ..models import Competition


class _AbstractCompetitionRepository(AbstractBaseRepository[Competition]):
    @abstractmethod
    def get_by_slug(self, slug: str) -> Competition:
        pass


class CompetitionRepository(_AbstractCompetitionRepository):
    def get_all(self) -> List[Competition]:
        return get_list_or_404(Competition)
    
    def get_by_id(self, id: int) -> Competition:
        return get_object_or_404(Competition, id=id)
    
    def get_by_slug(self, slug: str) -> Competition:
        return get_object_or_404(Competition, slug=slug)
    
    def create(self, **kwargs) -> Competition:
        return super().create(**kwargs)
    
    def update(self, id: int, **kwargs) -> Competition:
        return super().update(id, **kwargs)
    
    def delete(self, id: int) -> None:
        return super().delete(id)