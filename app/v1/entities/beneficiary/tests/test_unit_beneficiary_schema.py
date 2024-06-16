from unittest import TestCase
from pydantic import ValidationError

from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryBaseSchema,
)


class TestBeneficiarySchema(TestCase):
    def test_beneficiary_schema(self):
        beneficiary = BeneficiaryBaseSchema(
            name="Test Name",
            email="EXAMPLE123@DOMAIN.COM",
            cpf_cnpj="123.456.789-00",
        )

        self.assertIsNotNone(beneficiary)
        self.assertIsNotNone(beneficiary.name)
        self.assertIsInstance(beneficiary.name, str)
        self.assertIsNotNone(beneficiary.email)
        self.assertIsInstance(beneficiary.email, str)
        self.assertIsNotNone(beneficiary.cpf_cnpj)
        self.assertIsInstance(beneficiary.cpf_cnpj, str)

    def test_beneficiary_schema_invalid_email(self):
        with self.assertRaises(ValidationError) as context:
            BeneficiaryBaseSchema(
                name="Test Name",
                email="INVALID_EMAIL",
                cpf_cnpj="123.456.789-00",
            )

        [error_obj] = context.exception.errors()
        self.assertEqual(
            error_obj.get("msg", None),
            "String should match pattern '^[A-Z0-9+_.-]+@[A-Z0-9.-]+$'",
        )

    def test_beneficiary_schema_invalid_cpf_cnpj(self):
        validations = [
            {
                "input": "1234567890",
                "expected_output": "String should have at least 11 characters",
            },
            {
                "input": "123456789012345",
                "expected_output": "String should have at most 14 characters",
            },
            {
                "input": "12345678901",
                "expected_output": "String should match pattern '^[0-9]{3}[\\.]?[0-9]{3}[\\.]?[0-9]{3}[-]?[0-9]{2}$'",
            },
        ]

        with self.assertRaises(ValidationError) as context:
            for validation in validations:
                BeneficiaryBaseSchema(
                    name="Test Name",
                    email="EXAMPLE123@DOMAIN.COM",
                    cpf_cnpj=validation["input"],
                )

        for error_obj, validation in zip(context.exception.errors(), validations):
            self.assertEqual(
                error_obj.get("msg", None),
                validation["expected_output"],
            )
