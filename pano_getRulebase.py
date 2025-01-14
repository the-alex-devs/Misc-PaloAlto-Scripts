#Working 20240711
from panos.panorama import Panorama, DeviceGroup
from panos.policies import PreRulebase, SecurityRule
import getpass
import xml.etree.ElementTree as ET

username = input("Enter username: ")
userPass = getpass.getpass()
panorama_hostname = input("Enter Panorama hostname or IP address: ")

# Create config tree
pano = Panorama(panorama_hostname, username, userPass)

#Below assigns the desired devicegroup for the rules you want to look through
dg = DeviceGroup("Sandbox")
rb = PreRulebase()
print(rb)

pano.add(dg)
dg.add(rb)

#This refreshes rules from live devices in the dg
rules = SecurityRule.refreshall(rb)

#Below are some attributes I've tested with, not all of these are being used at once currently.
ruleName = "rulename"
sourceAddr = "source address"
logSetting = "log setting name"
ruleSchedule = None

#Here we search the rules (the entire rulebase for the dg (device group) and can return/print any of the securityrule's properties)
print("\nFor rule in rules:\n")
for rule in rules:
    if rule.schedule != ruleSchedule:
        print(rule.name, rule.fromzone, rule.tozone, rule.schedule)
        # rule.about() will return all attributes from a rule, which can be filtered on like how it is above
        #print(rule.about())
theresponse = str(pano.op("<show><rule-hit-count><device-group><entry name='Sandbox'><pre-rulebase><entry name='security'><rules><all/></rules></entry></pre-rulebase></entry></device-group></rule-hit-count></show>", cmd_xml=False))

