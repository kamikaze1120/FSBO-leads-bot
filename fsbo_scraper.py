import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Setup Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet (make sure the title matches!)
sheet = client.open("FSBO Leads").sheet1

# Example: Add one fake row to test it
sheet.append_row(["123 Main St", "Austin", "TX", "512-555-1234", "test@example.com"])
print("Test lead added to Google Sheet!")
