import requests
import urllib3

urllib3.disable_warnings()
url = f'https://{str(input("Enter the site you want to check: "))}'
try:
    requests.get(url, verify=False)
    print(f'\033[32mSUCESS: The website {url.replace("https://", "")} is available.\033[m')
except requests.exceptions.ConnectionError:
    print(f'\033[31mERRO: The website {url.replace("https://", "")} is unavailable.\033[m')