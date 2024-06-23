from pydantic import BaseModel, Field


class Pagination(BaseModel):
    total_pages: int = Field(..., ge=0)
    page: int = Field(1, ge=1)
    per_page: int = Field(10, ge=1)
