from abc import abstractmethod  
from typing import Protocol  
from uuid import UUID  

from ..domain.entities import CourseDM, ModuleDM, LessonDM 


class CourseSaver(Protocol): 
    @abstractmethod
    def save(self, course: CourseDM) -> None:
        pass 



class CourseReader(Protocol): 
    @abstractmethod
    def read(self, uuid: str) -> CourseDM | None:
        pass 



class UUIDGenerator(Protocol):  
    def __call__(self) -> UUID:  
        pass 



class DBSession(Protocol):  
    @abstractmethod  
    async def commit(self) -> None:  
        pass 
  
    @abstractmethod  
    async def flush(self) -> None: 
        pass