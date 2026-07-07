from decimal import Decimal

from invest_sdk.models import PositionInfo, PortfolioSummary
from invest_sdk.money import Money
from invest_sdk.repository import InstrumentRepository


class Statistics:
    """
    Выполняет вычисления и преобразует объекты SDK
    в модели библиотеки.
    """

    def __init__(self, client):

        self._repository = InstrumentRepository(client)

    # ------------------------------------------------------------------

    def make_position(self, position) -> PositionInfo:

        instrument = self._repository.by_uid(position.instrument_uid)

        quantity = Money.to_decimal(position.quantity)
        price = Money.to_decimal(position.current_price)
        average = Money.to_decimal(position.average_position_price)
        value = quantity * price

        profit = Money.to_decimal(position.expected_yield)
        daily = Money.to_decimal(position.daily_yield)

        if quantity and average:
            invested = quantity * average
            profit_percent = (
                profit / invested * Decimal("100")
            )
        else:
            profit_percent = Decimal("0")

        return PositionInfo(
            uid=instrument.uid,
            ticker=instrument.ticker,
            name=instrument.name,
            isin=instrument.isin,
            instrument_type=instrument.instrument_type,
            currency=instrument.currency,
            lot=instrument.lot,
            quantity=quantity,
            current_price=price,
            average_price=average,
            value=value,
            profit=profit,
            profit_percent=profit_percent,
            daily_profit=daily,
        )

    # ------------------------------------------------------------------

    def make_summary(self, portfolio):

        total_profit = sum(
            Money.to_decimal(position.expected_yield)
            for position in portfolio.positions
        )

        total_value = sum(
            Money.to_decimal(position.quantity) *
            Money.to_decimal(position.current_price)
            for position in portfolio.positions
        )

        daily_profit = sum(
            Money.to_decimal(position.daily_yield)
            for position in portfolio.positions
        )

        return PortfolioSummary(
            positions=len(portfolio.positions),
            total_value=total_value,
            total_profit=total_profit,
            daily_profit=daily_profit,
        )