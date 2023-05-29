import requests, csv, subprocess

# Source = Abuse CH
response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text
print(response)