class InstrumentRepository:

    def __init__(self):

        self._uid = {}
        self._ticker = {}
        self._figi = {}
        self._isin = {}

    def add(self, uid, ticker):

        self._uid[uid] = ticker

        self._ticker[ticker] = uid

    def count(self):

        return len(self._uid)