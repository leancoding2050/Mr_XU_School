from ninja import Schema

class SchoolYearListSchema(Schema):
    id: int
    school_year : str

class SchoolQuarterListSchema(Schema):
    id: int
    school_quarter : str

class SchoolLanguageListSchema(Schema):
    id: int
    school_language: str

class SchoolSubjectListSchema(Schema):
    id: int
    school_subject: str

class SchoolGradeListSchema(Schema):
    id: int
    school_grade: int

class SchoolPriceListSchema(Schema):
    id: int
    primary_school_price: float
    middle_school_price :float
    hight_school_price : float