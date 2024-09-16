from dataclasses import dataclass
from typing import List

import decimal


@dataclass(slots=True)
class CourseDM:
    course_id: str
    course_name: str 
    course_desc: str 
    course_duration: int 
    course_teacher: str 
    course_price: decimal
    course_category: str 
    course_avatar: str 
    





@dataclass(slots=True)
class ModuleDM:
    module_id: str 
    module_name: str 
    module_desc: str 
    course_id: str


     

@dataclass(slots=True)
class LessonDM:
    lesson_id: str 
    lesson_name: str 
    lesson_desc: str 
    lesson_content: List[str]
    module_id: str