from typing import Any

from app.v1.entities.bank_account.bank_account_schemas import BankAccountDataSchema
import random


def _get_random_bank() -> str:
    # This function is just for testing purposes
    banks = [
        "Banco do Brasil",
        "Bradesco",
        "Itaú",
        "Santander",
        "Caixa Econômica",
        "Nubank",
    ]
    random.shuffle(banks)
    return random.choice(banks)


class PixApiService:
    """
    This class is just for testing purposes. It simulates an external API that returns bank account data
    according to a pix key.
    """

    def get_bank_data_by_pix(
        self, pix_type: str, pix_key: Any
    ) -> BankAccountDataSchema:
        return BankAccountDataSchema(
            pix_key=pix_key,
            pix_key_type=pix_type,
            bank_name=_get_random_bank(),
            account_number="1234567890",
            account_type="CC",
            branch_number="0001-X",
        )
