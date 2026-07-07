from invest_sdk.models import PortfolioSummary, PositionInfo
from invest_sdk.money import Money


class Printer:
    """
    Красивый вывод информации в консоль.
    """

    def __init__(self, portfolio, account):
        self.portfolio = portfolio
        self.account = account

    # -----------------------------------------------------

    def print_header(self):

        print()
        print("=" * 90)
        print("📊 ПОРТФЕЛЬ")
        print("=" * 90)

        print(
            f"{'Ticker':<10}"
            f"{'Кол.':>8}"
            f"{'Цена':>14}"
            f"{'Стоимость':>18}"
            f"{'Прибыль':>15}"
            f"{'%':>10}"
        )

        print("-" * 90)

    # -----------------------------------------------------

    def print_position(self, info: PositionInfo):

        print(
            f"{info.ticker:<10}"
            f"{info.quantity:>8.0f}"
            f"{Money.format(info.current_price, ''):>14}"
            f"{Money.format(info.value, ''):>18}"
            f"{Money.format(info.profit, ''):>15}"
            f"{Money.percent(info.profit_percent):>10}"
        )

    # -----------------------------------------------------

    def print_summary(self, summary: PortfolioSummary):

        print("-" * 90)

        print(f"Всего позиций : {summary.positions}")
        print(f"Стоимость     : {Money.format(summary.total_value)}")
        print(f"Прибыль       : {Money.format(summary.total_profit)}")
        print(f"За день       : {Money.format(summary.daily_profit)}")

        print("=" * 90)