from dataclasses import asdict
import os

from t_tech.invest import Client
from config import TOKEN

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():
    with Client(TOKEN) as client:

        response = client.users.get_accounts()

        account = response.accounts[0]

        data = asdict(account)

        print(type(data))
        print(data.keys())
        print(data)


if __name__ == "__main__":
    main()