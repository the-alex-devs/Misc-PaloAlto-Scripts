#Working 20240711
from panos.panorama import Panorama, DeviceGroup
from panos.objects import AddressObject
import getpass

username = input("Enter username: ")
userPass = getpass.getpass()
panorama_hostname = input("Enter Panorama hostname or IP address: ")

# Create config tree
pano = Panorama(panorama_hostname, username, userPass)

def searchAddrObjs():
    #Below assigns the desired devicegroup for the objects you want to look through
    dg = DeviceGroup("Sandbox")
    objs = AddressObject()

    pano.add(dg)
    dg.add(objs)

    obj_searched = input("Enter object to search for (press enter for all): ")

    #This refreshes rules from live devices in the dg
    addrObjects = AddressObject.refreshall(dg)

    #Here we search the addrObjects (the entire list of address objects in the dg (device group) and can return/print any of the AddressObject's properties)
    print("\nFor object in addrObjects:\n")
    for object in addrObjects:
        if object.value in obj_searched or obj_searched in str(object.description):
            print(obj_searched + " found in existing objects: " + str(object.name) + " | " + str(object.value))


searchAddrObjs()
