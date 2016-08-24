from netmiko import ConnectHandler
from device_list import all_devices, test_devices
import time

def copy_tftp():
    for a_device in all_devices:
        try:
            net_connect = ConnectHandler(**a_device)
        except:
            print("##########################ERROR##########################")
            print(">>> net_connect to {0}".format(a_device['ip']))
            print(">>> Something went wrong trying to perform copy_tftp <<<")
            print("##########################ERROR##########################")
        else:
            print("--------------------------BEGIN--------------------------")
            print(">>>>> net_connect to {0}".format(a_device['ip']))
            print(">>>>> Copying Startup-Config from Device to TFTP Server <<<<<")
            tftpcopy = net_connect.send_command("copy running-config tftp 172.16.10.200 disk3/sdp/config_files/{0}.txt".format(a_device['ip']))
            print(">>>>> Flash has been set {0} <<<<<".format(a_device['ip']))
            print(tftpcopy)
            print("---------------------------END---------------------------")

def tftp_flash():
    for a_device in test_devices:
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command("copy tftp flash 172.16.10.200 YA pri")
        time.sleep(1)
        output += net_connect.send_command("y")
        time.sleep(60)
        shflash = net_connect.send_command("show flash")
        time.sleep(1)
        print("\n")
        print(shflash)
