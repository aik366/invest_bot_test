import os

from t_tech.invest import Client

from config import TOKEN
from invest_sdk.money import money_to_decimal

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():

    with Client(TOKEN) as client:

        account = client.users.get_accounts().accounts[0]

        portfolio = client.operations.get_portfolio(
            account_id=account.id
        )

        value = money_to_decimal(
            portfolio.total_amount_shares
        )

        print(value)
        print(type(value))


if __name__ == "__main__":
    main()