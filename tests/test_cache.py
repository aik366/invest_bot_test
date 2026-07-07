import invest_sdk.bootstrap

from t_tech.invest import Client

from config import TOKEN
from invest_sdk.accounts import Accounts
from invest_sdk.portfolio import Portfolio
from invest_sdk.repository import InstrumentRepository


with Client(TOKEN) as client:

    account = Accounts(client).accounts[0]

    portfolio = Portfolio(client, account.id)

    repo = InstrumentRepository(client)

    uid = portfolio.positions[0].instrument_uid

    print(len(repo))

    instrument = repo.by_uid(uid)

    print(instrument.name)

    print(len(repo))

    instrument = repo.by_uid(uid)

    print(instrument.name)

    print(len(repo))
