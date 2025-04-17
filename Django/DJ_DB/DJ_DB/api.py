from ninja import Schema

from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()
api.add_router("/course_data/","course_data.api.router")
api.add_router("/school_branch_campus/","school_branch_campus.api.router")
api.add_router("/School_data/","School_data.api.router")
api.add_router("/user_role/","user_role.api.router")