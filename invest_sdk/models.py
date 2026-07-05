from dataclasses import dataclass


@dataclass(slots=True)
class Instrument:
    uid: str
    ticker: str
    figi: str
    isin: str
    name: str
    currency: str
    exchange: str
    lot: int
    instrument_type: str
    