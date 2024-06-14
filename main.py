from fastapi import FastAPI, responses
from fastapi.openapi.docs import get_swagger_ui_html

from app.v1.config.settings import settings

app = FastAPI(
    title="TSF API",
    description="Beneficiary management",
    version=settings.API_VERSION,
    redoc_url=None,
    docs_url="/",
    openapi_url="/openapi.json",
)


@app.get("/docs", include_in_schema=False)
async def override_swagger():
    return get_swagger_ui_html(
        title="TSF API",
        openapi_url=app.openapi_url,
    )


@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse(url="/docs")
