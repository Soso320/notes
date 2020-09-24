# Connect to the IPInfo API
import requests
import json

APIKEY = ""

url = f"http://ipinfo.io/IPADDRESS?token={APIKEY}"
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

r = requests.get(url, headers=headers)
s = r.json()

ip = (s['ip'])
city = (s['city'])
region = (s['region'])
country = (s['country'])
coords = (s['loc'])
organization = (s['org'])
postcode = (s['postal'])
timezone = (s['timezone'])

print(f"{ip}\n{city}\n{region}\n{country}\n{coords}\n{organization}\n{postcode}\n{timezone}")

r.raise_for_status()
