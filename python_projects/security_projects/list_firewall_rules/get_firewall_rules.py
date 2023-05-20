#Security Projects - Eric Lovell - Outputs firewall rules to a file named Firewall_Rules_(Timestamp).txt

import time
import win32com.client

# Create instance of win client
firewall = win32com.client.Dispatch("HNetCfg.FwMgr")

# Get the collection of firewall rules
firewall_rules = firewall.LocalPolicy.CurrentProfile.Rules

#Put each rule and details in dictionary
firewall_rules_attributes = {}
#Count for rule id
index_count = 0
for rule in firewall_rules:
    firewall_rules_attributes["ID"] = "fwxr-3300-11" + str(index_count) 
    firewall_rules_attributes["Name:"] = rule.Name
    firewall_rules_attributes["Description:"] = rule.Description
    firewall_rules_attributes["Application name:"] = rule.ApplicationName
    firewall_rules_attributes["Action:"] = rule.Action
    firewall_rules_attributes["Direction:"] = rule.Direction
    firewall_rules_attributes["Protocol:"] = rule.Protocol
    firewall_rules_attributes["Local ports:"] = rule.LocalPorts
    firewall_rules_attributes["Remote addresses:"] = rule.RemoteAddresses
    index_count += 1

#Text file to write rules too
file_path = "Firewall_Rules_ " + str(time.time()) + ".txt"

#Output to file 
with open(file_path, 'w') as text_file:
    for key, value in firewall_rules_attributes.items():
        text_file.write(key + ": " + value + '\n')
