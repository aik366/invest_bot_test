from decimal import Decimal

from t_tech.invest.schemas import MoneyValue, Quotation


class Money:
    """
    Универсальная работа с денежными значениями.

    Поддерживает:
        - MoneyValue
        - Quotation
        - Decimal
        - int
        - float
    """

    # ---------------------------------------------------------

    @staticmethod
    def to_decimal(value) -> Decimal:
        """
        Преобразует MoneyValue, Quotation, Decimal,
        int или float в Decimal.
        """

        if isinstance(value, Decimal):
            return value

        if isinstance(value, int):
            return Decimal(value)

        if isinstance(value, float):
            return Decimal(str(value))

        if isinstance(value, (MoneyValue, Quotation)):
            return (
                Decimal(value.units)
                + Decimal(value.nano) / Decimal("1000000000")
            )

        raise TypeError(
            f"Unsupported type: {type(value).__name__}"
        )

    # ---------------------------------------------------------

    @staticmethod
    def format(value, currency: str = "₽") -> str:
        """
        Красивый вывод денежных значений.

        Примеры:
            12345.6 -> 12 345.60 ₽
            12345.6, "" -> 12 345.60
            12345.6, "$" -> 12 345.60 $
        """

        amount = Money.to_decimal(value)

        text = f"{amount:,.2f}".replace(",", " ")

        if currency:
            return f"{text} {currency}"

        return text

    # ---------------------------------------------------------

    @staticmethod
    def percent(value) -> str:
        """
        Красивый вывод процентов.

        Примеры:
            +15.23%
            -4.81%
        """

        amount = Money.to_decimal(value)

        sign = "+" if amount > 0 else ""

        return f"{sign}{amount:.2f}%"

    # ---------------------------------------------------------

    @staticmethod
    def multiply(left, right) -> Decimal:
        """
        Универсальное умножение денежных значений.

        Можно передавать:
            MoneyValue
            Quotation
            Decimal
            int
            float
        """

        return (
            Money.to_decimal(left)
            * Money.to_decimal(right)
        )