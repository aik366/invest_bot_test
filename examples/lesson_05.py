import os

from t_tech.invest import Client

from config import TOKEN

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():

    with Client(TOKEN) as client:

        accounts = client.users.get_accounts()

        account = accounts.accounts[0]

        portfolio = client.operations.get_portfolio(
            account_id=account.id
        )

        print(portfolio)

        print(type(portfolio.total_amount_shares))

        print(portfolio.total_amount_shares)

        money = portfolio.total_amount_shares

        print(money.currency)

        print(money.units)

        print(money.nano)
        print(portfolio.average_position_price)


if __name__ == "__main__":
    main()