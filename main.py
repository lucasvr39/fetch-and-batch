from utils.gspread import read_sheet_to_df
from utils.logging import logger
import pandas as pd
import sys

SPREADSHEET_ID = "your_spreadsheet_id_here"


def read_account_users_database() -> pd.DataFrame:
    try:
        df = read_sheet_to_df(SPREADSHEET_ID)
        if df is None:
            raise Exception("Failed to read data from Google Sheets")
        logger.info(f"Read {len(df)} rows from Google Sheets.")
        print(df.head())
    except Exception as e:
        logger.error(f"Process failed: {str(e)}")
        sys.exit(1)

    return df


def main() -> None: ...


if __name__ == "__main__":
    main()
