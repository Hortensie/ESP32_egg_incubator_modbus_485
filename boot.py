from wifi import connect_wifi
from machine import UART
import os
#uart = UART(2, baudrate=115200, bits=8, parity=None, stop=1, tx=12, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=5000, timeout_char=2)
#uart = UART(2, baudrate=115200, bits=8, parity=None, stop=1, tx=12, rx=13, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=5000, timeout_char=2)
#os.dupterm(uart)
#uart.write("Hello, World!\n")
#print(uart.readline())
#import micropython
#micropython.alloc_emergency_exception_buf(100)

connect_wifi()
