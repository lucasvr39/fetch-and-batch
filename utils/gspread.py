import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from utils.logging import logger
from config.config import get_config

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]


def get_google_creds_dict():
    config = get_config()
    creds_dict = {
        "type": "service_account",
        "project_id": "hardy-lightning-445314-c5",
        "private_key_id": config["private_key_id"],
        "private_key": config["private_key"],
        "client_email": config["client_email"],
        "client_id": config["client_id"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": config["client_x509_cert_url"],
        "universe_domain": "googleapis.com",
    }
    # if scopes is None:
    #     scopes = SCOPES
    try:
        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        logger.info("Google credentials loaded from .env successfully")
        return creds
    except Exception as e:
        logger.error(f"Error loading Google credentials from .env: {str(e)}")
        return None


# Read sheet to DataFrame using dict creds
def read_sheet_to_df(spreadsheet_id, account=None):
    """Reads a Google Sheet and returns its contents as a DataFrame."""
    creds = get_google_creds_dict()
    if creds is None:
        raise Exception("Failed to load Google credentials")

    try:
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.get_worksheet(0)
        data = worksheet.get_all_values()
        df = pd.DataFrame(data[1:], columns=data[0])
        logger.info(f"Successfully read sheet with {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Error reading Google Sheet: {str(e)}")
        return None
