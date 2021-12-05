

# Fast API
from fastapi import FastAPI

# Application
from app.salaries.routes import salaries_router


def get_application():
    """
    Get Application
    Get application build our ASGI interface using FastAPI
    :return app: FastAPI -> Fast api application
    """
    app: FastAPI = FastAPI(docs_url="/")
    app.include_router(salaries_router)
    return app


application = get_application()
