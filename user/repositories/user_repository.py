from typing import List
from uuid import UUID
from base_repository import BaseRepository
from models import CustomUser

class UserRepository(BaseRepository):

    def get(self, id: UUID) -> CustomUser:
        return CustomUser.objects.get(id=id)

    def all(self) -> List[CustomUser]:
        return CustomUser.objects.all()
    
    def update(self, instance: CustomUser, **kwargs) -> CustomUser:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance
        
    
