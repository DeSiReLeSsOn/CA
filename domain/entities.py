from dataclasses import dataclass 

from typing import List
import decimal


@dataclass(slots=True)
class CourseDM:
    uuid: str
    course_name: str 
    course_desc: str 
    course_duration: int 
    course_teacher: str 
    cpurse_price: decimal
    course_category: str 
    course_avatar: str 




@dataclass(slots=True)
class ModuleDM:
    module_name: str 
    module_desc: str 
    module_couse: CourseDM 


     

@dataclass(slots=True)
class LessonDM:
    lesson_name: str 
    lesson_desc: str 
    lesson_content: List[str]
    lesson_module: ModuleDM