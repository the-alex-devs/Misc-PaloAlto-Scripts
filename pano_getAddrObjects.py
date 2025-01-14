#Working 20240711
from panos.panorama import Panorama, DeviceGroup
from panos.objects import AddressObject
import getpass

username = input("Enter username: ")
userPass = getpass.getpass()
panorama_hostname = input("Enter Panorama hostname or IP address: ")

# Create config tree
pano = Panorama(panorama_hostname, username, userPass)

#Below assigns the desired devicegroup for the objects you want to look through
dg = DeviceGroup("Sandbox")
objs = AddressObject()

pano.add(dg)
dg.add(objs)

#This refreshes rules from live devices in the dg
addrObjects = AddressObject.refreshall(dg)
#print(addrObjects)

#Here we search the addrObjects (the entire list of address objects in the dg (device group) and can return/print any of the AddressObject's properties)
print("\nFor object in addrObjects:\n")
obj_count = 0
for object in addrObjects:
    print(object.name)
    obj_count = obj_count + 1
print("Number of objects found = " + str(obj_count))
