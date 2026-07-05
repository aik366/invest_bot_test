from invest_sdk.instrument_cache import InstrumentCache
from invest_sdk.utils import instrument_name
from invest_sdk.money import money_to_decimal, quotation_to_decimal, format_percent, format_money


class Portfolio:

    def __init__(self, client):
        self.client = client
        self.cache = InstrumentCache(client)

        account = client.users.get_accounts().accounts[0]
        self.account_id = account.id

        self._portfolio = client.operations.get_portfolio(
            account_id=self.account_id
        )

    # -------------------------
    # базовые данные
    # -------------------------

    def positions(self):
        return self._portfolio.positions

    # -------------------------
    # печать портфеля
    # -------------------------

    def print(self):

        for position in self._portfolio.positions:
            self._print_position(position)

    # -------------------------
    # внутренняя логика
    # -------------------------

    def _print_position(self, position):

        info = self.cache.get(position.figi)

        print("=" * 60)
        print(f"Компания:   {info.name}")
        print(f"Тикер:      {position.ticker}")
        print(f"Тип:        {instrument_name(position.instrument_type)}")

        qty = money_to_decimal(position.quantity)
        price = money_to_decimal(position.current_price)
        pnl = money_to_decimal(position.expected_yield)

        print(f"Количество: {qty}")
        print(f"Цена:       {price}")
        print(f"Прибыль:    {pnl}")

    # -------------------------
    # ОБЩАЯ СТОИМОСТЬ ПОРТФЕЛЯ
    # -------------------------

    def total_value(self):

        total = 0

        for position in self._portfolio.positions:
            qty = quotation_to_decimal(position.quantity)
            price = money_to_decimal(position.current_price)

            total += qty * price

        return total

    # -------------------------
    # ОБЩАЯ ПРИБЫЛЬ
    # -------------------------

    def total_profit(self):

        total = 0

        for position in self._portfolio.positions:
            total += money_to_decimal(position.expected_yield)

        return total

    # -------------------------
    # СОРТИРОВКА ПО ПРИБЫЛИ
    # -------------------------

    def top_positions(self, reverse=True):

        return sorted(
            self._portfolio.positions,
            key=lambda p: money_to_decimal(p.expected_yield),
            reverse=reverse
        )

    def print_summary(self):

        print("\n" + "=" * 60)
        print("📊 ПОРТФЕЛЬ")
        print("=" * 60)

        print(f"Общая стоимость: {self.total_value()}")
        print(f"Общая прибыль:   {self.total_profit()}")

        print("\nТОП по прибыли:\n")

        for position in self.top_positions()[:5]:
            info = self.cache.get(position.figi)
            if position.ticker == "RUB000UTSTOM":
                continue
            print(
                f"{position.ticker} → "
                f"{money_to_decimal(position.expected_yield)}"
            )

    def print_table(self):

        print("\n" + "=" * 90)
        print("📊 ПОРТФЕЛЬ (PRO)")
        print("=" * 90)

        header = f"{'Ticker':<8} {'Qty':<10} {'Price':<15} {'average':<15} {'Value':<15} {'Profit':<15}"
        print(header)
        print("-" * 90)

        for position in self._portfolio.positions:
            info = self.cache.get(position.figi)

            ticker = position.ticker
            if ticker == "RUB000UTSTOM":
                continue

            qty = quotation_to_decimal(position.quantity)
            price = money_to_decimal(position.current_price)
            price_average = money_to_decimal(position.average_position_price_fifo)

            value = qty * price
            profit = format_money(position.expected_yield)

            row = f"{ticker:<8} {qty:<10} {price:<15} {price_average:<15} {value:<15} {profit:<15}"

            print(row)
