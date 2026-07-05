INSTRUMENT_TYPES = {
    "share": "Акция",
    "bond": "Облигация",
    "etf": "Фонд",
    "currency": "Валюта",
    "future": "Фьючерс",
    "option": "Опцион",
}


def instrument_name(value: str) -> str:
    return INSTRUMENT_TYPES.get(value, value)
