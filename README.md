# Fetch and Batch

A minimal Python tool to fetch user list from different sources. Logs actions and errors for reliability.

## Features
- Reads user data from a specified Google Sheet
- Outputs data as a pandas DataFrame
- Simple logging and error handling

## Usage
1. Set your Google Spreadsheet ID in `main.py`.
2. Run:
   ```bash
   python main.py
   ```

## Requirements
- pandas
- Google Sheets API credentials (see `utils/gspread.py`)