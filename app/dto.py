from dataclasses import dataclass
from typing import List
import decimal


@dataclass(slots=True)
class CourseDTO:
    course_name: str 
    course_desc: str 
    course_duration: int 
    course_teacher: str 
    course_price: decimal
    course_category: str 
    course_avatar: str 
    





@dataclass(slots=True)
class ModuleDTO:
    module_name: str 
    module_desc: str 



     

@dataclass(slots=True)
class LessonDTO:
    lesson_name: str 
    lesson_desc: str 
    lesson_content: List[str]
