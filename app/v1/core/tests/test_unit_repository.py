from unittest import TestCase
from sqlalchemy.orm import Session
from unittest.mock import create_autospec
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy import Column, Integer

from app.v1.core.repository import Repository
from app.v1.database.db import Base


class StubTestModel(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True)


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
