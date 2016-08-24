from netmiko import ConnectHandler

switch = {
    'device_type': 'hp_procurve',
    'ip': '192.168.1.254',
    'username': '',
    'password': '',
    }
3
net_connect = ConnectHandler(**switch)

output = net_connect.send_command('show flash')
value = output.split('\n')
def_value = output.split()
print(value[2])
print(def_value[14])
print("Program Completed")

#file = open('sample.txt','w')
#file.write(output)
#file.close()

