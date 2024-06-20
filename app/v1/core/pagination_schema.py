from pydantic import BaseModel, Field


class Pagination(BaseModel):
    total_pages: int
    page: int = Field(1, ge=1)
    per_page: int = Field(10, ge=1)
