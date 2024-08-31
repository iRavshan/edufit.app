from uuid import UUID
from django.shortcuts import get_object_or_404, get_list_or_404
from abc import abstractmethod
from typing import List
from ..models import Article
from common.repositories import AbstractBaseRepository


class _AbstractArticleRepository(AbstractBaseRepository[Article]):
    @abstractmethod
    def get_by_slug(self, slug: str) -> Article:
        pass


class ArticleRepository(_AbstractArticleRepository):
    def get_all(self) -> List[Article]:
        return get_list_or_404(Article)
    
    def get_by_slug(self, slug: str) -> Article:
        return get_object_or_404(Article, slug=slug)
    
    def get_by_id(self, id: UUID) -> Article:
        return get_object_or_404(Article, id=id)
    
    def create(self, **kwargs) -> None:
        return super().create(**kwargs)
    
    def update(self, id: UUID, **kwargs) -> Article:
        return super().update(id, **kwargs)
    
    def delete(self, id: UUID) -> None:
        return super().delete(id)