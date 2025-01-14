from panos.panorama import Panorama
from panos.device import SystemSettings
import getpass

username = input("Enter username: ")
userPass = getpass.getpass()
panorama_hostname = input("Enter Panorama hostname or IP address: ")

# Create config tree
pano = Panorama(panorama_hostname, username, userPass)

# Refresh firewalls from live Panorama
devices = pano.refresh_devices(expand_vsys=False, include_device_groups=False)

# Print each firewall's serial and management IP
for device in devices:
    system_settings = device.find("", SystemSettings)
    print(f"{device.serial} {system_settings.hostname} {system_settings.ip_address}")