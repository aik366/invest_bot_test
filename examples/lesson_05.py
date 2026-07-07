import os


from t_tech.invest import Client
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import TOKEN
from invest_sdk.money import Money

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():

    with Client(TOKEN) as client:

        accounts = client.users.get_accounts()

        account_BRO = accounts.accounts[0]
        account_IIS = accounts.accounts[1]

        portfolio_BRO = client.operations.get_portfolio(account_id=account_BRO.id)
        portfolio_IIS = client.operations.get_portfolio(account_id=account_IIS.id)
        for i in portfolio_IIS.positions:
            print(i)

        # print(type(portfolio.total_amount_shares))

        # print(portfolio_BRO.total_amount_shares)
        # value_BRO = Money.to_decimal(portfolio_BRO.total_amount_shares)
        # value_IIS = Money.to_decimal(portfolio_IIS.total_amount_shares)
        
        # total_volue = value_BRO + value_IIS
        # print(total_volue)
       


if __name__ == "__main__":
    main()