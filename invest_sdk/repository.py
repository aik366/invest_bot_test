from invest_sdk.models import InstrumentInfo
from invest_sdk.services.instruments import InstrumentService


class InstrumentRepository:
    """
    Репозиторий инструментов.

    Отвечает за кэширование информации об инструментах.
    """

    def __init__(self, client):

        self._service = InstrumentService(client)
        self._cache: dict[str, InstrumentInfo] = {}

    # ---------------------------------------------------------

    def by_uid(self, uid: str) -> InstrumentInfo:
        """
        Возвращает InstrumentInfo по UID.
        """

        if uid not in self._cache:
            self._cache[uid] = self._service.by_uid(uid)

        return self._cache[uid]

    # ---------------------------------------------------------

    def clear(self):

        self._cache.clear()

    # ---------------------------------------------------------

    def __contains__(self, uid: str):

        return uid in self._cache

    # ---------------------------------------------------------

    def __len__(self):

        return len(self._cache)
