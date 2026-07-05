from decimal import Decimal
from t_tech.invest.schemas import MoneyValue, Quotation


# ----------------------
# MoneyValue → Decimal
# ----------------------
def money_to_decimal(value: MoneyValue) -> Decimal:
    return Decimal(value.units) + Decimal(value.nano) / Decimal("1000000000")


# ----------------------
# Quotation → Decimal
# (кол-во, проценты)
# ----------------------
def quotation_to_decimal(value: Quotation) -> Decimal:
    return Decimal(value.units) + Decimal(value.nano) / Decimal("1000000000")


def format_money(value: MoneyValue) -> str:
    d = money_to_decimal(value)
    return f"{d:,.2f} ₽".replace(",", " ")


def format_percent(value: Quotation) -> str:
    d = quotation_to_decimal(value)
    sign = "+" if d > 0 else ""
    return f"{sign}{d:.2f}%"