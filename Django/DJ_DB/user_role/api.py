from typing import List

from ninja import Router

from .models import UserRole
from .schemas import UserRoleListSchema

router = Router()

@router.get("userroles/" , response=List[UserRoleListSchema])
def list_userrole(request):
    userrole = UserRole.objects.all()

    return userrole