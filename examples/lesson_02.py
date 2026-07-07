from t_tech.invest import Client
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import TOKEN
import os

os.environ["SSL_TBANK_VERIFY"] = "true"

with Client(TOKEN) as client:

    response = client.users.get_accounts()

    account = response.accounts[0]

    from dataclasses import fields

    for field in fields(account):
        print(f"{field.name:15} -> {field.type}")
