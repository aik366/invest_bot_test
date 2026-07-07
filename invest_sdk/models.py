from dataclasses import dataclass
from decimal import Decimal


# ======================================================================
# Информация о позиции
# ======================================================================

from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class PositionInfo:
    """
    Полная информация о позиции портфеля.
    """
    uid: str
    ticker: str
    name: str
    isin: str
    instrument_type: str
    currency: str
    quantity: Decimal
    lot: int
    current_price: Decimal
    average_price: Decimal
    value: Decimal
    profit: Decimal
    profit_percent: Decimal
    daily_profit: Decimal


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