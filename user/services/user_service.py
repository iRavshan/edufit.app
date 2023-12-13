from typing import Type, List
from uuid import UUID
from .repositories.user_repository import UserRepository
from models import CustomUser

class UserService:

    def __init__(self, repository: Type[UserRepository] = UserRepository):
        self.repository = repository()

    def get_by_id(self, id: UUID) -> CustomUser:
        return self.repository.get(id)
    
    def get_all(self) -> List[CustomUser]:
        return self.repository.all()

    
    

