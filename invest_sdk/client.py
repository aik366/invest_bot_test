import os
from contextlib import contextmanager

from t_tech.invest import Client

from config import TOKEN

os.environ["SSL_TBANK_VERIFY"] = "true"


@contextmanager
def get_client():
    with Client(TOKEN) as client:
        yield client
        