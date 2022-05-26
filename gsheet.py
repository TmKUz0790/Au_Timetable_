from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1z20YDk7qpRijn3jkCGQx65u_1OsFB43Fn2iJaCtfjcY'
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def timetable ():

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                     range="Sheet3!A1:B10").execute()
    values = result.get('values',[])
    aoa = [["1/1/2022",4000],["4/4/2022",3000],["7/12/2022",7000]]
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheets2!B2",
                                    valueInputOption="USER_ENTERED" , body={"values":aoa})

    result2 = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet3!B1:B3").execute()
    rows2 = result2.get('values', [])

def monday() :
    result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet3!A1:A3").execute()
    rows = result.get('values', [])
    return rows

def thursday():
    t_result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet3!D1:D3").execute()
    t_rows = t_result.get('values', [])
    return t_rows

def wednesday():
    w_result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet3!C1:C3").execute()
    w_rows = w_result.get('values', [])
    return w_rows
def friday() :
        f_result = service.spreadsheets().values().get(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet3!E1:E3").execute()
        f_rows = f_result.get('values', [])
        return f_rows
def tuesday() :
    result2 = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet3!B1:B3").execute()
    rows2 = result2.get('values', [])
    return rows2

