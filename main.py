import os

from t_tech.invest import Client

from config import TOKEN
from invest_sdk.portfolio import Portfolio

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():

    with Client(TOKEN) as client:

        portfolio = Portfolio(client)

        portfolio.print_table()

        portfolio.print_summary()


if __name__ == "__main__":
    main()