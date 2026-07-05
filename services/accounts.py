from services.client import get_client


class AccountsService:

    @staticmethod
    def get_accounts():
        with get_client() as client:
            accounts = client.users.get_accounts()
            return accounts.accounts[0]
        