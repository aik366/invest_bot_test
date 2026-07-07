from t_tech.invest import Client
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import TOKEN

import os

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():

    with Client(TOKEN) as client:

        response = client.users.get_accounts()

        for account in response.accounts:
            print("=" * 50)
            print("ID:", account.id, type(account.id))
            print("Название:", account.name, type(account.name))
            print("Тип:", account.type)
            print("Тип.value:", account.type.value)
            print("Тип.name:", account.type.name)
            print("Статус:", account.status)
            print("Статус.value:", account.status.value)
            print("Дата открытия:", account.opened_date, type(account.opened_date))
            print("Уровень доступа:", account.access_level)


if __name__ == "__main__":
    main()