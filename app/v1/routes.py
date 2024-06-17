from fastapi import APIRouter

from app.v1.entities.beneficiary.beneficiary_endpoints import (
    router as beneficiary_router,
)

routes = APIRouter(tags=["Beneficiary"])

routes.include_router(beneficiary_router)
