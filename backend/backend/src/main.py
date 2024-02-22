from starlette.middleware.cors import CORSMiddleware

from src.endpoints.http.v1 import routers as v1_routers
from src.core.config import configs
from src.core.container import Container
from src.util.class_object import singleton


@singleton
class srcCreator:
    def __init__(self):
        # set src default
        self.src = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=f"{configs.API}/openapi.json",
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()
        # self.db.create_database()

        # set cors
        if configs.BACKEND_CORS_ORIGINS:
            self.src.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.src.get("/")
        def root():
            return "service is working"

        self.src.include_router(v1_routers, prefix=configs.API_V1_STR)
        self.src.include_router(v2_routers, prefix=configs.API_V2_STR)


src_creator = srcCreator()
src = src_creator.src
db = src_creator.db
container = src_creator.container
