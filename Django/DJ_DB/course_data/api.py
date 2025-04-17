from typing import List

from ninja import Router

from .models import CourseTime ,CourseLevel ,CourseRoom ,CourseLesson
from .schemas import CourseTimeListSchema ,CourseLevelListSchema ,CourseRoomListSchema ,CourseLessonListSchema

router = Router()

@router.get("coursetimes/", response=List[CourseTimeListSchema])
def list_coursetime_Data(request):
    coursetime = CourseTime.objects.all()

    return coursetime

@router.get("courselevels/",response=List[CourseLevelListSchema])
def list_courselevel_Data(request):
    courselevel = CourseLevel.objects.all()

    return courselevel

@router.get("courserooms/",response=List[CourseRoomListSchema])
def list_courseroom_Data(request):
    courseroom = CourseRoom.objects.all()

    return courseroom

@router.get("courselessons/",response=List[CourseLessonListSchema])
def list_courselesson_Data(request):
    courselesson = CourseLesson.objects.all()

    return courselesson