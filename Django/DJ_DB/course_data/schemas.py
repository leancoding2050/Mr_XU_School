from ninja import Schema

class CourseTimeListSchema(Schema):
    id: int
    course_time : str

class CourseRoomListSchema(Schema):
    id: int
    course_room : str

class CourseLevelListSchema(Schema):
    id: int
    course_level : str

class CourseLessonListSchema(Schema):
    id: int
    course_lesson : str