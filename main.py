from fastapi import FastAPI, responses
from fastapi.openapi.docs import get_swagger_ui_html

from app.v1.config.settings import settings
from app.v1.container import Container
from app.v1.routes import routes as v1_routes


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    _app = FastAPI(
        title="TSF API",
        description="Beneficiary management",
        version=settings.API_VERSION,
        redoc_url=None,
        docs_url="/",
        openapi_url="/openapi.json",
    )

    _app.container = container

    return _app


app = create_app()

app.include_router(v1_routes, prefix="/v1")


@app.get("/docs", include_in_schema=False)
async def override_swagger():
    return get_swagger_ui_html(
        title="TSF API",
        openapi_url=app.openapi_url,
    )


@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse(url="/docs")
