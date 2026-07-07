from dataclasses import dataclass
from decimal import Decimal


# ======================================================================
# Информация о позиции
# ======================================================================

@dataclass(slots=True)
class PositionInfo:
    """
    Подготовленная информация о позиции портфеля.

    Все значения уже преобразованы к Decimal и готовы
    для вывода, экспорта и анализа.
    """

    ticker: str
    name: str
    instrument_type: str

    quantity: Decimal
    average_price: Decimal
    current_price: Decimal
    value: Decimal
    profit: Decimal
    profit_percent: Decimal
    daily_profit: Decimal
    currency: str


# ======================================================================
# Общая информация о портфеле
# ======================================================================

@dataclass(slots=True)
class PortfolioSummary:
    """
    Сводная информация по портфелю.
    """
    positions: int
    total_value: Decimal
    total_profit: Decimal
    daily_profit: Decimal
    
    
@dataclass(slots=True)
class InstrumentInfo:
    uid: str
    ticker: str
    name: str
    lot: int
    currency: str
    instrument_type: str
    isin: str