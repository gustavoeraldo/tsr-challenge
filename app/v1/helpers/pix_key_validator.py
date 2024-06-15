from typing import Any
import re


class PixKeyValidator:
    def __init__(self, key: Any):
        self.key = key

    def is_valid_cnpj(self) -> bool:
        _is_valid = re.match(
            r"^\d{2}[\.]?\d{3}[\.]?\d{3}[\/]?\d{4}[-]?\d{2}$", self.key
        )
        return bool(_is_valid)

    def is_valid_cpf(self) -> bool:
        _is_valid = re.match(r"^\d{3}[\.]?\d{3}[\.]?\d{3}[-]?\d{2}$", self.key)
        return bool(_is_valid)

    def is_valid_email(self) -> bool:
        _is_valid = re.match(r"^[a-z0-9+_.-]+@[a-z0-9.-]+$", self.key)
        return bool(_is_valid)

    def is_valid_phone(self) -> bool:
        _is_valid = re.match(r"^((?:\+?55)?)([1-9]\d)(9\d{8})$", self.key)
        return bool(_is_valid)

    def is_valid_random_key(self) -> bool:
        _is_valid = re.match(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
            self.key,
        )
        return bool(_is_valid)
