

# Fast API
from fastapi import FastAPI

# Application
from starlette.middleware.cors import CORSMiddleware

from app.salaries.routes import salaries_router
from app.salaries.routes import technologies_router
from app.salaries.routes import titles_router
from app.salaries.routes import seniority_router

from app.exchanges.routes import exchanges_router
from app.exchanges.routes import currencies_router


def get_application():
    """
    Get Application
    Get application build our ASGI interface using FastAPI
    :return app: FastAPI -> Fast api application
    """
    app: FastAPI = FastAPI(docs_url="/")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(salaries_router)
    app.include_router(technologies_router)
    app.include_router(titles_router)
    app.include_router(seniority_router)

    app.include_router(exchanges_router)
    app.include_router(currencies_router)
    return app


application = get_application()
