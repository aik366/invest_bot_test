from invest_sdk.client import get_client
from invest_sdk.models import Account

from invest_sdk import cache


class Accounts:

    @staticmethod
    def all():

        if cache._accounts is not None:
            return cache._accounts

        with get_client() as client:

            response = client.users.get_accounts()

            accounts = []

            for item in response.accounts:

                accounts.append(
                    Account(
                        id=item.id,
                        name=item.name,
                        type=item.type.name,
                        access_level=item.access_level.name,
                    )
                )

            cache._accounts = accounts

            return accounts
        