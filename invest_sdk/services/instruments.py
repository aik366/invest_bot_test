from t_tech.invest.schemas import InstrumentIdType
from invest_sdk.models import InstrumentInfo


class InstrumentService:
    """
    Работа с API инструментов Т-Банка.
    """

    def __init__(self, client):
        self.client = client

    def by_uid(self, uid: str) -> InstrumentInfo:

        response = self.client.instruments.get_instrument_by(
            id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_UID,
            id=uid,
        )

        instrument = response.instrument

        return InstrumentInfo(
            uid=instrument.uid,
            ticker=instrument.ticker,
            name=instrument.name,
            lot=instrument.lot,
            currency=instrument.currency,
            instrument_type=instrument.instrument_type,
            isin=instrument.isin,
        )