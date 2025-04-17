from typing import List

from ninja import Router

from .models import SchoolBranch , SchoolBranchArea
from .schemas import SchoolBranchListSchema , SchoolBranchAreaListSchema

router = Router()

@router.get("schoolbranchDatas/",response=List[SchoolBranchListSchema])
def list_schoolbranch_Data(request):
    school_branch = SchoolBranch.objects.all()

    return school_branch

@router.get("schoolbranchareaDatas/",response=List[SchoolBranchAreaListSchema])
def list_schoolbrancharea_Data(request):
    school_branch_area = SchoolBranchArea.objects.all()

    return school_branch_area