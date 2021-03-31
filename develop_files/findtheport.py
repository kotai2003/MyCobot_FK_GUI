import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())
for item in port_list:
    print(item[0])