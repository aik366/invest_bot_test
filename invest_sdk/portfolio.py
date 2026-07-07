from invest_sdk.money import Money


class Portfolio:
    """
    Работа с портфелем одного счета.
    """

    def __init__(self, client, account_id):

        self.client = client
        self.account_id = account_id

        # Получаем портфель выбранного счета
        self.portfolio = client.operations.get_portfolio(
            account_id=account_id
        )

    # -----------------------------------------------------

    @property
    def positions(self):
        """
        Все позиции портфеля.
        """
        return self.portfolio.positions

    # -----------------------------------------------------

    @property
    def total_amount(self):
        """
        Общая стоимость портфеля.
        """
        return self.portfolio.total_amount_portfolio

    # -----------------------------------------------------

    @property
    def expected_yield(self):
        """
        Общая прибыль портфеля.
        """
        return self.portfolio.expected_yield

    def sorted_by_value(self, reverse=True):
        """
        Сортировка позиций по стоимости
        """

        def get_value(position):
            qty = Money.to_decimal(position.quantity)
            price = Money.to_decimal(position.current_price)
            return qty * price

        return sorted(self.positions, key=get_value, reverse=reverse)

    def total_value(self):
        """
        Общая стоимость портфеля
        """

        total = 0

        for position in self.positions:
            qty = Money.to_decimal(position.quantity)
            price = Money.to_decimal(position.current_price)

            total += qty * price

        return total

    def total_yield(self):
        """
        Общый доход
        """

        total = 0

        for position in self.positions:
            total += Money.to_decimal(position.expected_yield)

        return total

    def total_daily_yield(self):
        """
        Общый доход за день
        """

        total = 0

        for position in self.positions:
            total += Money.to_decimal(position.daily_yield)

        return total
