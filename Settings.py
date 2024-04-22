from machine import Pin, PWM, UART

class Relay():
    def __init__(self):
        ## Public Variables ##
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
        self.uart = 1
        self.deviceID = 2
        self.baudrate = 19200
        self.Bits = 8
        self.Parity = None
        self.Stopbit = 1

class Sensor():
    def __init__(self):
        ## Public Variables ##
        # Define pins
        self.dummysesnor = Pin(1, Pin.IN)

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