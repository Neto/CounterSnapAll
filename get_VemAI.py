import os
import serial
import time
import unidecode
from datetime import datetime
from google.auth import exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admob.readonly']


def find_ports():
    out = os.popen('ls /dev/tty.usb*').read()
    out1 = out.splitlines()

    find_ports.port1a = out1[0]
    find_ports.port2a = out1[1]
    find_ports.port3a = out1[2]


find_ports()

os.system("fuser " + find_ports.port1a)
os.system("fuser " + find_ports.port2a)
os.system("fuser " + find_ports.port3a)


def send(stringFinal):
    arduino = serial.Serial(find_ports.port2a, 9600)
    time.sleep(5)
    arduino.write(stringFinal + b'>')
    time.sleep(1)
    arduino.flushInput()
    time.sleep(1)
    arduino.flushOutput()
    time.sleep(1)
    arduino.close()


def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the AdMob API
        service = build('admob', 'v1', credentials=creds)

        # Get the account
        accounts = service.accounts().list().execute()

        # Get today's date
        today = datetime.today()

        report_body = {
            'reportSpec': {
                'dateRange': {
                    'startDate': {'year': 2023, 'month': 5, 'day': 1},
                    'endDate': {'year': today.year, 'month': today.month, 'day': today.day}
                },
                'metrics': ['ESTIMATED_EARNINGS'],
                'dimensionFilters': [],
                'dimensions': ['DATE'],
                'localizationSettings': {
                    'currencyCode': 'USD',
                    'languageCode': 'en-US'
                }
            }
        }

        totalEarnings = 0
        account = accounts['account'][0]['name']
        report_data = service.accounts().mediationReport().generate(parent=account, body=report_body).execute()
        for row in report_data:
            if 'row' in row:
                # assuming date is in 'YYYYMMDD' format
                date = row['row']['dimensionValues']['DATE']['value']
                # convert string to datetime object
                datetime_object = datetime.strptime(date, '%Y%m%d')
                # format datetime object to 'DD/MM/YYYY'
                formatted_date = datetime_object.strftime('%d/%m/%Y')
                earnings_micros = int(row['row']['metricValues']['ESTIMATED_EARNINGS']['microsValue'])
                earnings = earnings_micros / 1e6  # Convert from micro dollars to dollars
                stringFinal = f'\nDate:\n{formatted_date}\n\nEarnings:\n${earnings:.6f}'
                stringFinal = unidecode.unidecode(stringFinal)
                stringFinal = stringFinal.encode("utf-8")

                totalEarnings = totalEarnings + earnings

                print (totalEarnings)

        current_time = datetime.now().strftime("%H:%M:%S")
        stringFinal = f'\nLAST SELL:\n{formatted_date}-{current_time}\n\nEarnings:\n${totalEarnings:.2f}'
        stringFinal = unidecode.unidecode(stringFinal)
        stringFinal = stringFinal.encode("utf-8")       
        print(stringFinal)      
        send(stringFinal)


    except exceptions.GoogleAuthError as e:
        print('An authentication error occurred.', e)
    except Exception as e:
        print('An error occurred.', e)


if __name__ == '__main__':
    main()
