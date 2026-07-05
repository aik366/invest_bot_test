# invest_sdk/instrument_cache.py

class InstrumentCache:
    """
    Кэш инструментов по FIGI
    """

    def __init__(self, client):
        self.client = client
        self._cache = {}

    def get(self, figi: str):
        """
        Возвращает информацию об инструменте.
        Сначала ищет в кэше, потом в API.
        """

        if figi in self._cache:
            return self._cache[figi]

        response = self.client.instruments.get_instrument_by(
            id_type=1,  # FIGI
            id=figi
        )

        instrument = response.instrument

        self._cache[figi] = instrument

        return instrument
