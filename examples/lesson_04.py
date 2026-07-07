import os

from t_tech.invest import Client
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import TOKEN
from invest_sdk.helpers import account_type_name

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():

    with Client(TOKEN) as client:

        response = client.users.get_accounts()

        for account in response.accounts:
            print("-" * 60)

            print("ID:", account.id)

            print("Название:", account.name)

            print("Тип:", account_type_name(account.type))

            print("Статус:", account.status.name)

            print("Доступ:", account.access_level.name)


if __name__ == "__main__":
    main()