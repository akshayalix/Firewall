import eel
import requests, csv, subprocess
import webbrowser

# set folder 
eel.init('source')

# Removing Rules
@eel.expose
def remove_rule():
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


eel.browsers.set_path('chrome', r'C:\Users\alix\AppData\Local\Thorium\Application\thorium.exe')
eel.start('index.html', size=(800, 960), position=(550, 50))