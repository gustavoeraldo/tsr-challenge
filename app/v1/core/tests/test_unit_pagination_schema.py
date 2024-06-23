from unittest import TestCase
from pydantic import ValidationError

from app.v1.core.pagination_schema import Pagination


class TestUnitPaginationSchema(TestCase):
    def test_pagination_schema(self):
        schema = Pagination(total_pages=1)
        self.assertIsInstance(schema, Pagination)
        self.assertIsInstance(schema.page, int)
        self.assertIsInstance(schema.per_page, int)
        self.assertIsInstance(schema.total_pages, int)

        # Assert default values
        self.assertEqual(schema.page, 1)
        self.assertEqual(schema.per_page, 10)
        self.assertEqual(schema.total_pages, 1)

        self.assertEqual(
            schema.model_dump(), {"page": 1, "per_page": 10, "total_pages": 1}
        )

    def test_invalid_page(self):
        with self.assertRaises(ValidationError) as context:
            Pagination(page=-1, total_pages=1)

        error_obj = context.exception.errors()[0]

        self.assertEqual(
            error_obj.get("msg", ""), "Input should be greater than or equal to 1"
        )

    def test_invalid_per_page(self):
        with self.assertRaises(ValidationError) as context:
            Pagination(per_page=-1, total_pages=1)

        error_obj = context.exception.errors()[0]

        self.assertEqual(
            error_obj.get("msg", ""), "Input should be greater than or equal to 1"
        )

    def test_invalid_total_pages(self):
        with self.assertRaises(ValidationError) as context:
            Pagination(total_pages=-1)

        error_obj = context.exception.errors()[0]

        self.assertEqual(
            error_obj.get("msg", ""), "Input should be greater than or equal to 0"
        )
