import invest_sdk.bootstrap

from t_tech.invest import Client

from config import TOKEN
from invest_sdk.accounts import Accounts
from invest_sdk.portfolio import Portfolio
from invest_sdk.services.instruments import InstrumentService


with Client(TOKEN) as client:

    account = Accounts(client).accounts[0]

    portfolio = Portfolio(client, account.id)

    position = portfolio.positions[0]

    service = InstrumentService(client)

    instrument = service.by_uid(position.instrument_uid)

    print(instrument)