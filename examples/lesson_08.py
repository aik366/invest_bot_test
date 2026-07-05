import os

from t_tech.invest import Client

from config import TOKEN

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():

    with Client(TOKEN) as client:

        account = client.users.get_accounts().accounts[0]

        portfolio = client.operations.get_portfolio(
            account_id=account.id
        )

        position = portfolio.positions[0]



        print(dir(position))


if __name__ == "__main__":
    main()