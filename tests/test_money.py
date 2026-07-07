import invest_sdk.bootstrap

from t_tech.invest import Client

from config import TOKEN
from invest_sdk.accounts import Accounts
from invest_sdk.portfolio import Portfolio
from invest_sdk.money import Money


with Client(TOKEN) as client:

    account = Accounts(client).accounts[0]

    portfolio = Portfolio(client, account.id)

    position = portfolio.positions[0]

    print("Тикер      :", position.ticker)

    print("Количество :", Money.to_decimal(position.quantity))

    print("Цена       :", Money.to_decimal(position.current_price))

    print("Стоимость  :", Money.position_value(position))
    