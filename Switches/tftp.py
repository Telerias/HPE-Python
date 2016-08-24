#from netmiko import ConnectHandler
from device_list import all_devices
from datetime import datetime
from functions import *
import time

# Get the current time and show the start of the program
start_time = datetime.now()
print ("Start Time = {}".format(start_time))

#copy_tftp()
tftp_flash()

end_time = datetime.now()
total_time = end_time - start_time
print("Total time = {}".format(total_time))