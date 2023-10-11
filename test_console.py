import eel
import requests, csv, subprocess
import webbrowser
import sys

# set folder 
eel.init('source')

# Removing Rules
@eel.expose
def elevation_remove_rule():
    subprocess.run(['python', 'elevation.py'])

    rule = "netsh advfirewall firewall delete rule name='BadIP'"
    subprocess.run(["Powershell", "-Command", rule])


# Adding Inbound Rule 
@eel.expose
def inbound_rule():
    response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text

    rule = "netsh advfirewall firewall delete rule name= 'BadIP'"
    subprocess.run(["Powershell", "-Command", rule])

    mycsv = csv.reader(filter(lambda x: not x.startswith("#"), response.splitlines()))
    for row in mycsv:
        ip = row[1]
        if(ip)!=("dst_ip"):
            print("Added Rule to block:", ip)
            rule = "netsh advfirewall firewall add rule name='BadIP' Dir=In Action=Block RemoteIP=" + ip  # Fill Dir= with (Out or In)
            subprocess.run(["Powershell", "-Command", rule])

# Adding Outbound Rule 
@eel.expose
def outbound_rule():
    response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text

    rule = "netsh advfirewall firewall delete rule name= 'BadIP'"
    subprocess.run(["Powershell", "-Command", rule])

    mycsv = csv.reader(filter(lambda x: not x.startswith("#"), response.splitlines()))
    for row in mycsv:
        ip = row[1]
        if(ip)!=("dst_ip"):
            print("Added Rule to block:", ip)
            rule = "netsh advfirewall firewall add rule name='BadIP' Dir=Out Action=Block RemoteIP=" + ip  # Fill Dir= with (Out or In)
            subprocess.run(["Powershell", "-Command", rule])

# Opening Github in external tab.
@eel.expose
def open_github():
    webbrowser.open("https://www.github.com/akshayalix/Firewall")


class ConsoleOutput:
    def __init__(self):
        self.buffer = []

    def write(self, text):
        self.buffer.append(text)
        # Send the text to JavaScript using Eel
        eel.updateConsole(" ".join(self.buffer))

sys.stdout = ConsoleOutput()
sys.stderr = ConsoleOutput()

@eel.expose
def send_to_js(text):
    eel.updateConsole(text)



eel.start('index.html', mode='chrome-app', port=8080)