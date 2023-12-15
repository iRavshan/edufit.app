from typing import List, Type
from uuid import UUID
from .repositories.question_repository import QuestionRepository

class QuestionService:

    def __init__(self, repository: Type[QuestionRepository] = QuestionRepository):
        self.repository = repository()
    
    def get(self, id: UUID):
        questions = self.repository.get()

