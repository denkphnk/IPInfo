import urllib.request
import json

getIP = input('[+] Enter IP ---> ')
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen(url)

except:
    print('\n [!] Wrong IP')

infoList = json.load(getInfo)

print('-' * 60)
try:
    print(f'IP: {infoList["ip"]}')
    print(f'Region: {infoList["region"]}')
    print(f'City: {infoList["city"]}')
    print(f'Loc: {infoList["loc"]}')
    print(f'Time Zone: {infoList["timezone"]}')
    print(f'Host: {infoList["hostname"]}')

except:
    print('[!] Too secure IP')