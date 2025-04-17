from typing import List

from ninja import Router

from .models import SchoolYear , SchoolQuarter , SchoolLanguage , SchoolSubject , SchoolGrade , SchoolPrice
from .schemas import SchoolYearListSchema , SchoolQuarterListSchema , SchoolLanguageListSchema , SchoolSubjectListSchema , SchoolGradeListSchema , SchoolPriceListSchema

router = Router()

@router.get("schoolyears/",response=List[SchoolYearListSchema])
def list_schoolyear_Data(request):
    school_year = SchoolYear.objects.all()

    return school_year

@router.get("schoolquarters/",response=List[SchoolQuarterListSchema])
def list_schoolquarter_Data(request):
    school_quarter = SchoolQuarter.objects.all()

    return school_quarter

@router.get("schoollanguages/",response=List[SchoolLanguageListSchema])
def list_schoollanguage_Data(request):
    school_language = SchoolLanguage.objects.all()

    return school_language

@router.get("schoolsubjects/",response=List[SchoolSubjectListSchema])
def list_schoolsuject_Data(request):
    school_subject = SchoolSubject.objects.all

    return school_subject

@router.get("schoolgrades/",response=List[SchoolGradeListSchema])
def list_schoolsuject_Data(request):
    school_grade = SchoolGrade.objects.all

    return school_grade

@router.get("schoolprices/",response=List[SchoolPriceListSchema])
def list_schoolsuject_Data(request):
    school_price = SchoolPrice.objects.all

    return school_price
