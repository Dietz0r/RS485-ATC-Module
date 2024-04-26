# import modbus client classes
from lib.umodbus.serial import ModbusRTU

#import Settings
from Settings import RS485

rs485 = RS485()

#define variables
modbus_rtu_config = {
    "pins": (rs485.TX, rs485.RX),   # (TX, RX)
    "addr": rs485.deviceID,         # address on bus as client
    "baudrate": rs485.baudrate,     # baudrate from settings
    "uart_id": rs485.uart,          # uart channel from settings
    "data_bits": rs485.Bits,        # DataBits from settings
    "parity": rs485.Parity,         # Parity from settings
    "stop_bits": rs485.Stopbit,     # StopBit from settings
    # "ctrl_pin": 12,               # optional, control DE/RE
}

client = ModbusRTU(**modbus_rtu_config)