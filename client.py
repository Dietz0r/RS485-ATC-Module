# import modbus client classes
from lib.umodbus.serial import ModbusRTU

#import Settings
from Settings import rs485_settings as rs485

#define variables
modbus_rtu_config = {
    "pins": (rs485["TX"], rs485["RX"]),   # (TX, RX)
    "addr": rs485["device_id"],         # address on bus as client
    "baudrate": rs485["baudrate"],     # baudrate from settings
    "uart_id": rs485["uart"],          # uart channel from settings
    "data_bits": rs485["bits"],        # DataBits from settings
    "parity": rs485["parity"],         # Parity from settings
    "stop_bits": rs485["stop_bit"],     # StopBit from settings
    # "ctrl_pin": rs485["ctrl_pin"],               # optional, control DE/RE
}

client = ModbusRTU(**modbus_rtu_config)
