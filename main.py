
from webserver import web_setup
#import webcam
#webcam.run()
from uModBus.serial import Serial
#from uModBus.tcp import TCP
#from network import WLAN
from machine import Pin
from machine import UART

#uart2 = UART(1, baudrate=115200, bits=8, parity=None, stop=1, tx=14, rx=15, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=5000, timeout_char=2)
#print("Sukces tx14 rx15 uart1")


#uart=UART(1, 9600, tx=12, rx=13)
#uart.init(9600,bits=8,parity=None,stop=1,rx=12,tx=13)
####################### TCP MODBUS #########################
#WIFI_SSID = 'your ssid'
#WIFI_PASS = 'your password'

#wlan = WLAN(mode=WLAN.STA)
#wlan.connect(WIFI_SSID, auth=(None, WIFI_PASS), timeout=5000)
#while not wlan.isconnected():
#machine.idle() # save power while waiting
#print('WLAN connection succeeded!')
#slave_ip = '192.168.2.101'
#modbus_obj = TCP(slave_ip)
######################### RTU SERIAL MODBUS #########################
#uart_id = 0x02
#from machine import UART
uart_id = 2
#uart=UART(uart_id, tx=12, rx=13)
#uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=12, rx=14, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=5000, timeout_char=2)
#modbus_obj = Serial(uart_id)
#modbus_obj.read(10)
#modbus_obj.read()
#modbus_obj.readline()
#modbus_obj.write('abc')
#print(modbus_obj.readline())
#print(modbus_obj.read())
#uart=UART(2, baudrate=9600, tx=12, rx=13, timeout=5000)
#uart.write("Hello Hello\n")
#print("COS TAM")
#uart.read(5)
#print(uart.any())
#print("COS tam2")
modbus_obj = Serial(uart_id)
print("Sukces")
#modbus_obj = Serial().__init__(uart,baudrate=9600, data_bits=8, stop_bits=1, parity=None, pins=(12,13), ctrl_pin=None)
#print("COS tam3")
######################### READ COILS #########################
#slave_addr=0x01
#starting_address=0x00
#coil_quantity=10

#coil_status = modbus_obj.read_coils(slave_addr, starting_address, coil_quantity)
#print('Coil status: ' + ' '.join('{:d}'.format(x) for x in coil_status))

###################### READ DISCRETE INPUTS ##################
#slave_addr=0x0A
#starting_address=0x0
#input_quantity=100

#input_status = modbus_obj.read_discrete_inputs(slave_addr, starting_address, input_quantity)
#print('Input status: ' + ' '.join('{:d}'.format(x) for x in input_status))

###################### READ HOLDING REGISTERS ##################
#slave_addr=0x0A
#starting_address=0x00
#register_quantity=100
#signed=True

#register_value = modbus_obj.read_holding_registers(slave_addr, starting_address, register_quantity, signed)
#print('Holding register value: ' + ' '.join('{:d}'.format(x) for x in register_value))

###################### READ INPUT REGISTERS ##################
#slave_addr=0x0A
#starting_address=0x00
#register_quantity=100
#signed=True

#register_value = modbus_obj.read_input_registers(slave_addr, starting_address, register_quantity, signed)
#print('Input register value: ' + ' '.join('{:d}'.format(x) for x in register_value))

###################### WRITE SINGLE COIL ##################
#slave_addr=0x0A
#output_address=0x00
#output_value=0xFF00

#return_flag = modbus_obj.write_single_coil(slave_addr, output_address, output_value)
#return_flag = modbus_obj.write_single_coil(slave_addr, output_address, output_value)
#output_flag = 'Success' if return_flag else 'Failure'
#print('Writing single coil status: ' + output_flag)

###################### WRITE SINGLE REGISTER ################## FUN
slave_addr=0x0001
register_address=0x0001
register_value=0x0001
signed=True

return_flag = modbus_obj.write_single_register(slave_addr, register_address, register_value, signed)
output_flag = 'Success' if return_flag else 'Failure'
print('Writing single coil status: ' + output_flag)

###################### WRITE MULIPLE COILS ##################
#slave_addr=0x0A
#starting_address=0x00
#output_values=[1,1,1,0,0,1,1,1,0,0,1,1,1]

#return_flag = modbus_obj.write_multiple_coils(slave_addr, starting_address, output_values)
#output_flag = 'Success' if return_flag else 'Failure'
#print('Writing multiple coil status: ' + output_flag)

###################### WRITE MULIPLE REGISTERS ##################
#slave_addr=0x0A
#register_address=0x01
#register_values=[2, -4, 6, -256, 1024]
#signed=True

#return_flag = modbus_obj.write_multiple_registers(slave_addr, register_address, register_values, signed)
#output_flag = 'Success' if return_flag else 'Failure'
#print('Writing multiple register status: ' + output_flag)

web_setup()
