import os
import invest_sdk.bootstrap
from t_tech.invest import Client

from config import TOKEN
from invest_sdk.accounts import Accounts
from invest_sdk.portfolio import Portfolio
from invest_sdk.money import Money
from invest_sdk.printer import Printer
from invest_sdk.statistics import Statistics


def main():

    with Client(TOKEN) as client:

        # Выбираем счет
        accounts = Accounts(client)
        accounts.print()

        account = accounts.choose()

        # Загружаем портфель
        portfolio = Portfolio(
            client,
            account.id
        )

        stats = Statistics(client)
        
        printer = Printer(portfolio=portfolio, account=account)
        printer.print_header()

        for position in portfolio.sorted_by_value():
            info = stats.make_position(position)
            printer.print_position(info)

        
        summary = stats.make_summary(portfolio.portfolio)

        printer.print_summary(summary)


if __name__ == "__main__":
    main()
    