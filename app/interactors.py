from app import interfaces 
from app.dto import CourseDTO, ModuleDTO, LessonDTO 
from ..domain import entities



class GetCourseInteractor:
    def __init__(self, 
                 course_gateway: interfaces.CourseReader) -> None:
        self._course_gateway = course_gateway 


    async def __call__(self, uuid: str) -> entities.CourseDM | None:
        return await self._course_gateway.read_course_by_uuid(uuid)




class GetModuleInteractor:
    def __init__(self, 
                 module_gateway: interfaces.ModuleReader) -> None:
        self._module_gateway = module_gateway 


    async def __call__(self, uuid: str) -> entities.ModuleDM | None:
        return await self._course_gateway.read_module_by_uuid(uuid) 
    

class GetLessonInteractor:
    def __init__(self, 
                 lesson_gateway: interfaces.LessonReader) -> None:
        self._lesson_gateway = lesson_gateway 


    async def __call__(self, uuid: str) -> entities.LessonDM | None:
        return await self._lesson_gateway.read_lesson_by_uuid(uuid) 
    


class NewCourseInteractor:
    def __init__(self, 
                db_session: interfaces.DBSession,  
                course_gateway: interfaces.CourseSaver,  
                uuid_generator: interfaces.UUIDGenerator,) -> None:
        self._db_session = db_session  
        self._course_gateway = course_gateway  
        self._uuid_generator = uuid_generator   


    async def __call__(self, dto: CourseDTO) -> str:
        course_id = str(self._uuid_generator)
        course = entities.CourseDM(
            course_id=course_id,
            course_name=dto.course_name,
            course_desc=dto.course_desc,
            course_duration=dto.course_duration,
            course_teacher=dto.course_teacher,
            course_price=dto.course_price,
            course_category=dto.course_category,
            course_avatar=dto.course_avatar
        )


        await self._course_gateway.save(course)
        await self._db_session.commit()
        return course_id
  
        



class NewModuleInteractor:
    def __init__(self, 
                db_session: interfaces.DBSession,  
                module_gateway: interfaces.ModuleSaver,  
                uuid_generator: interfaces.UUIDGenerator,) -> None:
        self._db_session = db_session  
        self._module_gateway = module_gateway  
        self._uuid_generator = uuid_generator   


    async def __call__(self, dto: ModuleDTO, course_id: str) -> str:
        module_id = str(self._uuid_generator)
        module = entities.ModuleDM(
            module_id=module_id, 
            module_name=dto.module_name, 
            module_desc=dto.module_desc,
            course_id=course_id
        )


        await self._module_gateway.save(module)
        await self._db_session.commit()
        return module_id




class NewLessonInteractor:
    def __init__(self, 
                db_session: interfaces.DBSession,  
                lesson_gateway: interfaces.LessonSaver,  
                uuid_generator: interfaces.UUIDGenerator,) -> None:
        self._db_session = db_session  
        self._lesson_gateway = lesson_gateway  
        self._uuid_generator = uuid_generator   


    async def __call__(self, dto: LessonDTO, module_id: str,) -> str:
        lesson_id = str(self._uuid_generator)
        lesson = entities.LessonDM(
            lesson_id=lesson_id, 
            lesson_name=dto.lesson_name, 
            lesson_desc=dto.lesson_desc,
            lesson_content=dto.lesson_content,
            module_id=module_id
        )


        await self._module_gateway.save(lesson)
        await self._db_session.commit()
        return lesson_id
