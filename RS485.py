#import settings and functions
from Sensors import sensor_functions as sensors
from Settings import register_definitions
from Reporting import Report
from Relay import RelayControl

import RGBLed

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

from client import client, modbus_rtu_config
print('Using pins {} with UART ID {}'.format(modbus_rtu_config["pins"], modbus_rtu_config["uart_id"]))

relay = RelayControl()
report = Report()

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
        } ,        
        "Update Inputs": {
            "register": 256,
            "len": 1,
            "val": 0,
            "on_set_cb": sensors.update
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
        "Sensor1": {
            "register": 257,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        },
        "Sensor2": {
            "register": 258,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        },
        "Sensor3": {
            "register": 259,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        },
        "Sensor4": {
            "register": 260,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        },
        "Sensor5": {
            "register": 261,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        },                                
        "Sensor6": {
            "register": 262,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        },
        "Sensor7": {
            "register": 263,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        },                                
        "Sensor8": {
            "register": 264,
            "len": 1,
            "val": 0,
            "on_get_cb": report.SensorRep
        }  
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
      format(modbus_rtu_config["addr"], modbus_rtu_config["baudrate"]))
RGBLed.setRGBsolid(10, 0, 0)

while True:
    try:
        result = client.process()
    except KeyboardInterrupt:
        print('KeyboardInterrupt, stopping RTU client...')
        break
    except Exception as e:
        print('Exception during execution: {}'.format(e))

print("Finished providing/accepting data as client")
