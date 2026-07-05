from services.client import get_client


class PortfolioService:

    @staticmethod
    def get(account_id):

        with get_client() as client:
            return client.operations.get_portfolio(
                account_id=account_id
            )
            