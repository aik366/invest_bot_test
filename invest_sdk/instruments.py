# invest_sdk/instruments.py

def get_instrument_info(client, figi: str):
    """
    Получает информацию об инструменте по FIGI
    """

    response = client.instruments.get_instrument_by(
        id_type=1,  # FIGI
        id=figi
    )

    return response.instrument