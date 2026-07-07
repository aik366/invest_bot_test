import os
os.environ["SSL_TBANK_VERIFY"] = "true"
from t_tech.invest import Client
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config import TOKEN
from invest_sdk.accounts import Accounts
from invest_sdk.portfolio import Portfolio


with Client(TOKEN) as client:

    account = Accounts(client).accounts[0]

    portfolio = Portfolio(client, account.id)

    position = portfolio.positions[0]

    print(type(position))

    print()

    for key, value in vars(position).items():

        print(f"{key:<30} {value}")
        