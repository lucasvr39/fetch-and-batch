import os
from dotenv import load_dotenv
from os.path import join, dirname, abspath


def get_config():
    dotenv_path = join(dirname(dirname(abspath(__file__))), ".env")
    config_loaded = load_dotenv(dotenv_path)
    if config_loaded:
        print("Configuration loaded successfully")
    else:
        print("Failed to load configuration")
    # Return Google API config as dict
    return {
        "private_key_id": os.environ.get("GOOGLE_PRIVATE_KEY_ID"),
        "private_key": os.environ.get("GOOGLE_PRIVATE_KEY"),
        "client_email": os.environ.get("GOOGLE_CLIENT_EMAIL"),
        "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
        "client_x509_cert_url": os.environ.get("GOOGLE_CLIENT_X509_CERT_URL"),
    }
