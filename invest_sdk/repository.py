from invest_sdk.models import InstrumentInfo
from t_tech.invest.schemas import InstrumentIdType


class InstrumentRepository:
    """
    Репозиторий инструментов.

    Единственная точка получения информации
    об инструментах через API Т-Банка.

    В дальнейшем здесь появится кэш.
    """

    def __init__(self, client):

        self.client = client

        # Пока обычный словарь.
        # Позже сделаем полноценный Cache.
        self._cache = {}

    # ---------------------------------------------------------

    def get(self, instrument_uid: str) -> InstrumentInfo:
        """
        Возвращает InstrumentInfo по UID.

        Если инструмент уже загружен,
        используется кэш.
        """

        if instrument_uid in self._cache:
            return self._cache[instrument_uid]

        instrument = self.client.instruments.get_instrument_by(
            id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_UID,
            id=instrument_uid,
            ).instrument

        info = InstrumentInfo(
            uid=instrument.uid,
            ticker=instrument.ticker,
            name=instrument.name,
            lot=instrument.lot,
            currency=instrument.currency,
            instrument_type=instrument.instrument_type,
            isin=instrument.isin,
        )

        self._cache[instrument_uid] = info

        return info