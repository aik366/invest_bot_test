import os
import certifi

os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = certifi.where()
os.environ["SSL_TBANK_VERIFY"] = "true"
