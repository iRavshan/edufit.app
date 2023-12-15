from uuid import UUID
from base_repository import BaseRepository
from .models import Question

class QuestionRepository(BaseRepository):
    def get(self, id: UUID) -> Question:
        return Question.objects.get(id=id)

    def all(self) -> List[Question]:
        return Question.objects.all()
    
    def update(self, instance: Question, **kwargs) -> Question:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance