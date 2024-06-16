from unittest import TestCase
from pydantic import ValidationError

from ..schemas.bank_account_schema import BankAccountBaseSchema


class TestUnitBankAccountBaseSchema(TestCase):
    def test_valid_pix_key_type(self):
        sample_data = [
            {"pix_key_type": "CPF", "pix_key": "111.111.111-11"},
            {"pix_key_type": "CNPJ", "pix_key": "11.111.111/0001-11"},
            {"pix_key_type": "PHONE", "pix_key": "+5511976543210"},
            {"pix_key_type": "EMAIL", "pix_key": "rachel.green@example.com"},
            {
                "pix_key_type": "RANDOM",
                "pix_key": "ede7d3e5-4ee7-4a44-93ff-e06b4d43f6eb",
            },
        ]

        for data in sample_data:
            schema = BankAccountBaseSchema(**data)
            self.assertEqual(schema.pix_key_type, data["pix_key_type"])
            self.assertEqual(schema.pix_key, data["pix_key"])

    def test_invalid_pix_key_type(self):
        with self.assertRaises(ValidationError) as context:
            BankAccountBaseSchema(pix_key_type="INVALID", pix_key="")

        [error_obj] = context.exception.errors()
        self.assertEqual(error_obj.get("msg", ""), "Value error, Invalid pix type")

    def test_invalid_cpf_pix_key(self):
        with self.assertRaises(ValidationError) as context:
            BankAccountBaseSchema(pix_key_type="CPF", pix_key="")

        [error_obj] = context.exception.errors()
        self.assertEqual(error_obj.get("msg", ""), "Value error, Invalid CPF")

    def test_invalid_cnpj_pix_key(self):
        with self.assertRaises(ValidationError) as context:
            BankAccountBaseSchema(pix_key_type="CNPJ", pix_key="")

        [error_obj] = context.exception.errors()
        self.assertEqual(error_obj.get("msg", ""), "Value error, Invalid CNPJ")

    def test_invalid_phone_pix_key(self):
        with self.assertRaises(ValidationError) as context:
            BankAccountBaseSchema(pix_key_type="PHONE", pix_key="")

        [error_obj] = context.exception.errors()
        self.assertEqual(error_obj.get("msg", ""), "Value error, Invalid Phone")

    def test_invalid_email_pix_key(self):
        with self.assertRaises(ValidationError) as context:
            BankAccountBaseSchema(pix_key_type="EMAIL", pix_key="")

        [error_obj] = context.exception.errors()
        self.assertEqual(error_obj.get("msg", ""), "Value error, Invalid Email")

    def test_invalid_random_pix_key(self):
        with self.assertRaises(ValidationError) as context:
            BankAccountBaseSchema(pix_key_type="RANDOM", pix_key="")

        [error_obj] = context.exception.errors()
        self.assertEqual(error_obj.get("msg", ""), "Value error, Invalid Random Key")
