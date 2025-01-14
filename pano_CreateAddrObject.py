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
            print(obj_searched + " found in existing objects: " + str(object.name) + " value= " + str(object.value))
        else:
            print("Object not found. Creating new one: ")
            new_addr_name = input("Object name: ")
            new_addr_value = input("Object vlue: ")
            new_obj = AddressObject()
            new_obj.fqdn = new_addr_value
            print(new_obj.about)
            input("Continue?")
            pano.add(new_obj)
            new_obj.create()
            


searchAddrObjs()
