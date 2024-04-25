from machine import Pin, PWM, UART

class Relay():
    def __init__(self):
        ## Public Variables ##
        self.RelayNum   : int = 6                   #Number of Relaychannels available
        # Define pins
        self.Relay1 = Pin(1, Pin.OUT)
        self.Relay2 = Pin(2, Pin.OUT)
        self.Relay3 = Pin(41, Pin.OUT)
        self.Relay4 = Pin(42, Pin.OUT)
        self.Relay5 = Pin(45, Pin.OUT)
        self.Relay6 = Pin(46, Pin.OUT)

        self.Channel = [self.Relay1, self.Relay2, self.Relay3, self.Relay4, self.Relay5, self.Relay6]

class RS485():
    def __init__(self):
        ## Public Variables ##
        # Define pins
        self.TX = 17
        self.RX = 18
    
        # RS485 Settings (8n1 Default)
        self.uart       : int = 1
        self.deviceID   : int = 2
        self.baudrate   : int = 19200
        self.Bits       : int = 8
        self.Parity           = None
        self.Stopbit    : int = 1

class SensorPins():
    def __init__(self):
        ## Public Variables ##
        self.Timing     : int = 200               # check sensor pins ever 'x' ms
        self.SensorNum  : int = 8                 # Number of Sensor Pins available
        self.PullUpDown : str = 'Up'              # use internal weak pull up or down resistor [Up / Down]

        # Define pins
        self.Sensor1 = Pin(3, Pin.IN)       # Spindle clamped sensor 
        self.Sensor2 = Pin(4, Pin.IN)       # Spindle unclamped sensor
        self.Sensor3 = Pin(5, Pin.IN)
        self.Sensor4 = Pin(6, Pin.IN)
        self.Sensor5 = Pin(7, Pin.IN)
        self.Sensor6 = Pin(8, Pin.IN)
        self.Sensor7 = Pin(9, Pin.IN)
        self.Sensor8 = Pin(10, Pin.IN)

        self.Sensor = [self.Sensor1, self.Sensor2, self.Sensor3, self.Sensor4, self.Sensor5, self.Sensor6, self.Sensor7, self.Sensor8]
        

class Button():
    def __init__(self):
        ## Public Variables ##
        # Define pins
        self.dummybutton = Pin(1, Pin.IN)

class ARGB():
    def __init__(self):
        ##Public Variables ##
        #Define pins
        self.RGBpin = Pin(38, Pin.OUT)

        #LED Settings
        self.NumLeds = 1            #Number of adressable LED's 