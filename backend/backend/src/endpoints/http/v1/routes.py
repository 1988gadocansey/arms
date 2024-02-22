from fastapi import APIRouter

from src.endpoints.http.v1.user import router as user_router
from src.endpoints.http.v1.post import router as post_router
from src.endpoints.http.v1.tag import router as tag_router
from src.endpoints.http.v1.auth import router as auth_router
routers = APIRouter()
router_list = [auth_router, post_router, tag_router, user_router]

for router in router_list:
    router.tags = routers.tags.srcend("v1")
    routers.include_router(router)
