import os
from dotenv import load_dotenv
from os.path import join, dirname, abspath

# Load environment variables
ENV_PATH = join(dirname(dirname(abspath(__file__))), ".env")
load_dotenv(ENV_PATH)

# Google API settings
google_settings = {
    "private_key_id": os.environ.get("GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.environ.get("GOOGLE_PRIVATE_KEY"),
    "client_email": os.environ.get("GOOGLE_CLIENT_EMAIL"),
    "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
    "client_x509_cert_url": os.environ.get("GOOGLE_CLIENT_X509_CERT_URL"),
    "project_id": "hardy-lightning-445314-c5",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "universe_domain": "googleapis.com",
}

# Snowflake settings
snowflake_settings = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "account": os.environ.get("DB_ACCOUNT"),
    "warehouse": os.environ.get("DB_WAREHOUSE"),
    "database": os.environ.get("DB_DATABASE"),
    "schema": os.environ.get("DB_SCHEMA"),
    "role": os.environ.get("DB_ROLE"),
}
