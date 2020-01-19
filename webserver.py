from sensor_dht11 import read_sensor


try:
  import usocket as socket
except:
  import socket

from machine import Pin
led = Pin(4, Pin.OUT)

def web_page(temperatura,humidity):
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  temp=temperatura
  hum=humidity
  html = """
<html>
<head>
<title>Egg Incubator</title>
<meta http-equiv="refresh" content="30" >
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
<style>
html
{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}
</style>
</head>

<body>
<h1><i class="fas fa-egg" style="color:#059e8a;"></i> Egg Incubator</h1>
 <p>
    <i class="fas fa-fire-alt" style="color:#059e8a;"></i>
    <span class="dht-labels">Heating: <strong>""" + gpio_state + """</strong></span>
    <sup class="units">&deg;C</sup>
  <p/>
  <p>
    <a href="/?led=on"><button class="button">ON</button></a>
    <a href="/?led=off"><button class="button button2">OFF</button></a></p>
  </p>

  <p>
    <i class="fas fa-wind" style="color:#059e8a;"></i>
    <span class="dht-labels">Fan: <strong>""" + gpio_state + """</strong></span>
  <p/>

  <p>
    <a href="/?led=on"><button class="button">ON</button></a>
    <a href="/?led=off"><button class="button button2">OFF</button></a></p>
  </p>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i>
    <span class="dht-labels">Current Temperature</span>
    <span>"""+str(temp)+"""</span>
    <sup class="units">&deg;C</sup>
  <p/>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i>
    <span class="dht-labels">Target Temperature</span>
    <span>"""+str(temp)+"""</span>
    <sup class="units">&deg;C</sup>
  <p/>
  <p>
    <a href="/?led=on"><button class="button">Set +0.5</button></a>
    <a href="/?led=off"><button class="button button2">Set -0.5</button></a></p>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i>
    <span class="dht-labels">Humidity</span>
    <span>"""+str(hum)+"""</span>
    <sup class="units">%</sup>
  </p>


  <p>
    <i class="fas fa-video" style="color:#00add6;"></i>
    <span class="dht-labels">Camera view</span>
    <span>"""+str(temp)+"""</span>
  </p>
  <p>
    <a href="/?led=on"><button class="button">ON</button></a>
    <a href="/?led=off"><button class="button button2">OFF</button></a></p>
  </p>

</body>
</html>
  """
  return html
#def web_setup(temperature,humidity):
def web_setup():
    #bind the socket to an address (network interface and port number) using the bind() method. The bind() method accepts a tupple variable with the ip address, and port number:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    #The argument specifies the maximum number of queued connections. The maximum is 5.
    s.listen(5)
    #temp=temperature
    #hum=humidity
    while True:
      current_measure = read_sensor()
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      request = str(request)
      print('Content = %s' % request)
      led_on = request.find('/?led=on')
      led_off = request.find('/?led=off')
      if led_on == 6:
        print('LED ON')
        led.value(1)
      if led_off == 6:
        print('LED OFF')
        led.value(0)
      #if current_measure[0] >= 27:
    #    print('LED OFF')
    #    led.value(0)
     # if current_measure[0] < 27:
    #    print('Ogrzewanie wlaczone')
    #    led.value(1)
      response = web_page(current_measure[0],current_measure[1])
      print("Inside internal loop 3")
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
