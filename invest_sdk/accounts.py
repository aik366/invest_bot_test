from t_tech.invest.schemas import Account


class Accounts:
    """
    Работа со счетами пользователя.
    """

    def __init__(self, client):

        self.client = client

        # Получаем список счетов один раз
        self.accounts = client.users.get_accounts().accounts

    # -----------------------------------------------------

    def print(self):

        print()
        print("=" * 60)
        print("ДОСТУПНЫЕ СЧЕТА")
        print("=" * 60)

        for i, account in enumerate(self.accounts, start=1):

            print(f"{i}. {account.name}")

        print()

    # -----------------------------------------------------

    def choose(self) -> Account:

        while True:

            try:

                number = int(input("Введите номер счета: "))

                if 1 <= number <= len(self.accounts):

                    return self.accounts[number - 1]

                print("Такого номера нет.\n")

            except ValueError:

                print("Введите число.\n")
                