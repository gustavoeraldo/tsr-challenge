from typing import Any, Generic, Type, TypeVar, Callable
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from contextlib import AbstractContextManager

from app.v1.database.db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")


class Repository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        model: Type[ModelType],
        session_factory: Callable[..., AbstractContextManager[Session]],
    ):
        self.model = model
        self.session_factory = session_factory

    def get_by_id(self, entity_id: Any) -> ModelType:
        with self.session_factory() as db:
            obj = db.query(self.model).get(entity_id)
            if obj is None:
                raise NotFoundError(entity_id)
            return obj

    def create(self, data: CreateSchemaType) -> ModelType:
        with self.session_factory() as db:
            obj_in_data = jsonable_encoder(data)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj

    def delete_by_id(self, entity_id: Any) -> ModelType:
        with self.session_factory() as db:
            obj = self.get_by_id(entity_id)
            db.delete(obj)
            db.commit()
            return obj

    def update_by_id(self, entity_id: Any, data: UpdateSchemaType) -> ModelType:
        with self.session_factory() as db:
            current_obj = self.get_by_id(entity_id)
            obj_data = jsonable_encoder(current_obj)
            updated_data = data.dict(exclude_unset=True)

            for field in obj_data:
                if field in updated_data:
                    setattr(current_obj, field, updated_data[field])

            db.commit()
            db.refresh(current_obj)

            return current_obj


class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id: Any):
        super().__init__(f"{self.entity_name} not found with id {entity_id}")
