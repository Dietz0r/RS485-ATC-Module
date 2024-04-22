# import modbus client classes
from lib.umodbus.serial import ModbusRTU

#import settings and functions
from Settings import RS485
import Relay

relay = Relay.RelayControl()

#define variables
rtu_pins = (RS485.TX, rs485.RX)         # (TX, RX)
slave_addr = RS485.deviceID             # address on bus as client
baudrate = RS485.baudrate               # baudrate from settings
uart_id = RS485.uart                    # uart channel from settings
bits = RS485.Bits                       # DataBits from settings
par = RS485.Parity                      # Parity from settings
stop = RS485.Stopbit                    # StopBit from settings

try:
    from machine import Pin
    import os
    from lib.umodbus import version

    os_info = os.uname()
    print('MicroPython infos: {}'.format(os_info))
    print('Used micropthon-modbus version: {}'.format(version.__version__))

except AttributeError:
    pass
except Exception as e:
    raise e

print('Using pins {} with UART ID {}'.format(rtu_pins, uart_id))

client = ModbusRTU(
    addr = slave_addr,      # address on bus
    pins = rtu_pins,        # given as tuple (TX, RX)
    baudrate = baudrate,    # optional, default 9600
    data_bits = bits,       # optional, default 8
    stop_bits = stop,       # optional, default 1
    parity = par,           # optional, default None
    # ctrl_pin = 12,        # optional, control DE/RE
    uart_id = uart_id       # optional, default 1, see port specific docs
)

def reset_data_registers_cb(reg_type, address, val):
    # usage of global isn't great, but okay for an example
    global client
    global register_definitions

    print('Resetting register data to default values ...')
    client.setup_registers(registers=register_definitions)
    print('Default values restored')


# common slave register setup, to be used with the Master example above
register_definitions = {
    "COILS": {
        "RESET_REGISTER_DATA_COIL": {
            "register": 42,
            "len": 1,
            "val": 0
        },
        "Relay1": {
            "register": 1,
            "len": 1,
            "val": 0,
            "on_set_cb": relay.SetRelay
        },
        "Relay2": {
            "register": 2,
            "len": 1,
            "val": 0,
            "on_set_cb": relay.SetRelay
        },
        "Relay3": {
            "register": 3,
            "len": 1,
            "val": 0,
            "on_set_cb": relay.SetRelay
        },
        "Relay4": {
            "register": 4,
            "len": 1,
            "val": 0,
            "on_set_cb": relay.SetRelay
        },
        "Relay5": {
            "register": 5,
            "len": 1,
            "val": 0,
            "on_set_cb": relay.SetRelay
        },                                
        "Relay6": {
            "register": 6,
            "len": 1,
            "val": 0,
            "on_set_cb": relay.SetRelay
        }    
    },
    "HREGS": {
#        "EXAMPLE_HREG": {
#            "register": 93,
#            "len": 1,
#            "val": 19
#        }
    },
      "ISTS": {
#       "EXAMPLE_ISTS": {
#            "register": 67,
#            "len": 1,
#            "val": 0
#        }
    },
    "IREGS": {
#        "EXAMPLE_IREG": {
#            "register": 10,
#            "len": 1,
#            "val": 60001
#        }
    }
}

# reset all registers back to their default value with a callback
register_definitions['COILS']['RESET_REGISTER_DATA_COIL']['on_set_cb'] = \
    reset_data_registers_cb

print('Setting up registers ...')
# use the defined values of each register type provided by register_definitions
client.setup_registers(registers=register_definitions)
# alternatively use dummy default values (True for bool regs, 999 otherwise)
# client.setup_registers(registers=register_definitions, use_default_vals=True)
print('Register setup done')

print('Serving as RTU client on address {} at {} baud'.
      format(slave_addr, baudrate))

while True:
    try:
        result = client.process()
    except KeyboardInterrupt:
        print('KeyboardInterrupt, stopping RTU client...')
        break
    except Exception as e:
        print('Exception during execution: {}'.format(e))

print("Finished providing/accepting data as client")