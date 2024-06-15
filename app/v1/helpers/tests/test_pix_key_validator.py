from unittest import TestCase
import uuid

from app.v1.helpers.pix_key_validator import PixKeyValidator


class TestPixKeyValidator(TestCase):
    def test_is_valid_cnpj(self):
        cnpj = "11.111.111/0001-11"
        validator = PixKeyValidator(cnpj)
        self.assertTrue(validator.is_valid_cnpj())

    def test_is_valid_cpf(self):
        cpf = "111.111.111-11"
        validator = PixKeyValidator(cpf)
        self.assertTrue(validator.is_valid_cpf())

    def test_is_valid_email(self):
        email = "megan.hall@example.com"
        validator = PixKeyValidator(email)
        self.assertTrue(validator.is_valid_email())

    def test_is_valid_phone(self):
        phone = "+5511976543210"
        validator = PixKeyValidator(phone)
        self.assertTrue(validator.is_valid_phone())

    def test_is_valid_random_key(self):

        random_key = str(uuid.uuid4())
        validator = PixKeyValidator(random_key)
        self.assertTrue(validator.is_valid_random_key())

    def test_is_invalid_cnpj(self):
        cnpj = "11.111.111/0001-122"
        validator = PixKeyValidator(cnpj)
        self.assertFalse(validator.is_valid_cnpj())

    def test_is_invalid_cpf(self):
        cpf = "111.111.111-112"
        validator = PixKeyValidator(cpf)
        self.assertFalse(validator.is_valid_cpf())

    def test_is_invalid_email(self):
        email = "GRACE.LEE@EXAMPLE"
        validator = PixKeyValidator(email)
        self.assertFalse(validator.is_valid_email())

    def test_is_invalid_phone(self):
        phone = "432423"
        validator = PixKeyValidator(phone)
        self.assertFalse(validator.is_valid_phone())

    def test_is_invalid_random_key(self):
        random_key = "123"
        validator = PixKeyValidator(random_key)
        self.assertFalse(validator.is_valid_random_key())
