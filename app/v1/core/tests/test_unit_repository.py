from unittest import TestCase
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session
from unittest.mock import create_autospec, patch
from contextlib import AbstractContextManager
from typing import Callable
from pydantic import BaseModel

from app.v1.core.repository import Repository
from app.v1.database.db import Base


class StubTestModel(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True)


class StubTestModelUpdateSchema(BaseModel):
    id: int


class TestUnitRepository(TestCase):
    def setUp(self):
        self.mock_session_factory = create_autospec(
            Callable[..., AbstractContextManager[Session]], instance=True
        )

        self.model = StubTestModel
        self.repository = Repository(
            model=self.model, session_factory=self.mock_session_factory
        )

    def test_repository_constructor(self):
        self.assertEqual(self.repository.model, self.model)
        self.assertEqual(self.repository.session_factory, self.mock_session_factory)

    def test_repository_get_by_id(self):
        self.repository.get_by_id(1)
        self.mock_session_factory.assert_called_once()

        # self.assertIsInstance(test_model_data, StubTestModel)

    def test_get(self):
        self.repository.get({"id": 1})
        self.mock_session_factory.assert_called_once()

    def test_create(self):
        self.repository.create({"id": 1})
        self.mock_session_factory.assert_called_once()

    def test_delete_by_id(self):
        self.repository.delete_by_id(1)
        self.mock_session_factory.assert_called_once()

    @patch("app.v1.core.repository.Repository.get_by_id")
    def test_update_by_id(self, get_by_id_mock):
        # Mock setup
        get_by_id_mock.return_value = StubTestModel(id=1)

        self.repository.update_by_id(1, StubTestModelUpdateSchema(id=1))
        self.mock_session_factory.assert_called()
