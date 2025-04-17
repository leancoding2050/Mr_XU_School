from ninja import Schema

class SchoolBranchListSchema(Schema):
    id: int
    school_branch : str


class SchoolBranchAreaListSchema(Schema):
    id: int
    school_branch_Area : str