from uuid import UUID
from abc import abstractmethod
from django.shortcuts import get_list_or_404, get_object_or_404
from typing import List
from common.repositories import AbstractBaseRepository
from ..models import UserAttempt, QuestionAttempt


class _AbstractUserAttemptRepository(AbstractBaseRepository[UserAttempt]):
    pass


class UserAttemptRepository(_AbstractUserAttemptRepository):
    def get_all(self) -> List[UserAttempt]:
        return get_list_or_404(UserAttempt)
    
    def get_by_id(self, id: UUID) -> UserAttempt:
        return get_object_or_404(UserAttempt, id=id)
    
    def create(self, **kwargs) -> UserAttempt:
        return super().create(**kwargs)
    
    def update(self, id: UUID, **kwargs) -> UserAttempt:
        return super().update(id, **kwargs)
    
    def delete(self, id: UUID) -> None:
        return super().delete(id)