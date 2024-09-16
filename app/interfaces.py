from abc import abstractmethod  
from typing import Protocol  
from uuid import UUID  

from dto import CourseDTO, ModuleDTO, LessonDTO


class CourseSaver(Protocol): 
    @abstractmethod
    def save(self, course: CourseDTO) -> None:
        pass 



class CourseReader(Protocol): 
    @abstractmethod
    def read(self, uuid: str) -> CourseDTO | None:
        pass 



class UUIDGenerator(Protocol):  
    def __call__(self) -> UUID:  
        pass  



class ModuleSaver(Protocol): 
    @abstractmethod
    def save(self, course: ModuleDTO) -> None:
        pass  


class ModuleReader(Protocol): 
    @abstractmethod
    def read(self, uuid: str) -> ModuleDTO | None:
        pass 


class LessonSaver(Protocol): 
    @abstractmethod
    def save(self, course: LessonDTO) -> None:
        pass  


class LessonReader(Protocol): 
    @abstractmethod
    def read(self, uuid: str) -> LessonDTO | None:
        pass 




class DBSession(Protocol):  
    @abstractmethod  
    async def commit(self) -> None:  
        pass 
  
    @abstractmethod  
    async def flush(self) -> None: 
        pass