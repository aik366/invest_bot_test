from invest_sdk.models import PositionInfo, PortfolioSummary
from invest_sdk.money import Money


from dataclasses import dataclass
from decimal import Decimal


class Statistics:
    """
    Все вычисления над портфелем.
    """

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def position_value(self, position):
        """
        Стоимость позиции.
        """

        qty = Money.to_decimal(position.quantity)
        price = Money.to_decimal(position.current_price)

        return qty * price
    
    def make_position(self, position):
        """
        Преобразует PortfolioPosition SDK в PositionInfo.
        """

        qty = Money.to_decimal(position.quantity)

        average_price = Money.to_decimal(position.average_position_price)

        current_price = Money.to_decimal(position.current_price)

        value = qty * current_price

        profit = Money.to_decimal(position.expected_yield)

        daily_profit = Money.to_decimal(position.daily_yield)

        cost = qty * average_price

        if cost:
            profit_percent = profit / cost * Decimal("100")
        else:
            profit_percent = Decimal("0")

        return PositionInfo(
            ticker=position.ticker,
            name="",                           # позже заполнит Repository
            instrument_type=position.instrument_type,

            quantity=qty,

            average_price=average_price,
            current_price=current_price,

            value=value,

            profit=profit,
            profit_percent=profit_percent,

            daily_profit=daily_profit,

            currency=position.current_price.currency,
        )
        
    def positions(self):
        """
        Возвращает позиции портфеля в виде PositionInfo,
        отсортированные по стоимости.
        """

        for position in self.portfolio.sorted_by_value():
            yield self.make_position(position)
            
    
    def summary(self) -> PortfolioSummary:
        return PortfolioSummary(
            positions=len(self.portfolio.positions),
            total_value=self.portfolio.total_value(),
            total_profit=self.portfolio.total_yield(),
            daily_profit=self.portfolio.total_daily_yield(),
        )