import network
import esp

def connect_wifi():
    #The following lines turn off vendor OS debugging messages:
    esp.osdebug(None)

    #Then, we run a garbage collector
    import gc
    gc.collect()

    ssid = "linksys"
    password = "litewska666"

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print('Connection successful')
    print(station.ifconfig())
