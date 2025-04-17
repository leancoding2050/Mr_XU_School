from ninja import Schema

class UserRoleListSchema(Schema):
    id: int
    user_role : str