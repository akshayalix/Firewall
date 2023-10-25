import eel
import requests, csv, subprocess
import webbrowser
import sys
from time import sleep

# set folder 
eel.init('source')

# Removing Rules
@eel.expose
def remove_rule():
    print("-> Removing Rules")
    rule = "netsh advfirewall firewall delete rule name='BadIP'"
    subprocess.run(["Powershell", "-Command", rule])
    print("-> Done")

# Adding Inbound Rule 
@eel.expose
def inbound_rule():
    print("-> Adding In-Bound Rules to Firewall")
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
    print("-> Done")

# Adding Outbound Rule 
@eel.expose
def outbound_rule():
    print("-> Adding Out-Bound Rules to Firewall")
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
    print("-> Done")

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


# For lauching in chrome.
#eel.start('index.html', mode='chrome-app', port=8080)  

# For a window app.
#eel.start('index.html', size=(700, 500), position=(750, 300))

if __name__=="__main__":

    print("-> Make sure to run this as admin to work\n")

    #eel.start('index.html', mode='chrome-app', port=8080)
    eel.start('index.html', size=(1000, 700), position=(500, 100))

    


    
    
