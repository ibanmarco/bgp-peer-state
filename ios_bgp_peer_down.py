import sys
from getpass import getpass
from napalm import get_network_driver

username = sys.argv[1]
password = getpass("Password: ")
file_name = sys.argv[2]
ios_routers = open(file_name, "r")

for device in ios_routers:
    print("\nIOS Device: {}".format(device.strip('\n')))
    driver = get_network_driver('ios')
    core_routers = driver(device.strip('\n'), username, password)
    core_routers.open()
    for k in list(core_routers.get_bgp_neighbors()["global"]["peers"].keys()):
        if core_routers.get_bgp_neighbors()["global"]["peers"][k]["is_up"]:
            print("{0} BGP peer {0} - UP".format(device.strip('\n'), k))
        else:
            print("{0} BGP peer {0} - DOWN".format(device.strip('\n'), k))
    core_routers.close()

ios_routers.close()
