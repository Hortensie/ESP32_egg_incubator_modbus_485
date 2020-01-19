import dht
from machine import Pin
from time import sleep
#print("Inside read sensor x")

def read_sensor():
      #print("Inside read sensor y")
      sensor = dht.DHT11(Pin(15))
      global temp, hum
      temp = hum = 0
      #while True:
      try:
        #print("Inside read sensor z")
        #DHT11 maximum sampling rate is 1 seconds
        sleep(1)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        #temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        #print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
        return (temp,hum)
      except OSError as e:
        print('Failed to read sensor.')
     # return (temp,hum)
