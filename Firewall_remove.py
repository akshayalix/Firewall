import requests, csv, subprocess

rule = "netsh advfirewall firewall delete rule name= 'BadIP'"
subprocess.run(["Powershell", "-Command", rule])