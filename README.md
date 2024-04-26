## RS485 ATC Module ##

__Scope:__ 

This is meant to be a standalone ATC module for the [Waveshare ESP32-S3-relay-6CH](https://www.waveshare.com/esp32-s3-relay-6ch.htm) capable of adding additional I/O capability to CNC Mills. The I/O, including but not limited to the 6 relay output channels of the Waveshare board, are controlled over the RS485 Interface to provide a reliable industry standard way of connecting it to existing CNC control hardware with minimal effort.

Developed with help and for the [PrintNC community](https://wiki.printnc.info/en/home) alongside the [grblHAL2000](https://github.com/Expatria-Technologies/grblhal_2000_PrintNC) and [flexiHAL](https://expatria.myshopify.com/products/flexi-hal) by [Expatria Technologies Inc.](https://github.com/Expatria-Technologies) boards for [grblHAL](https://github.com/grblHAL) by [TerjeIO](https://github.com/terjeio) with RS485 ModbusRTU support

Written in MicroPython to allow for easy modification and adaption to other ESP32 or MicroPython capable 'off-the-shelf' boards.

__Credits:__

Using the [MicroPython Modbus library](https://github.com/brainelectronics/micropython-modbus) (Version: 2.3.7) by [brainelectronics](https://github.com/brainelectronics) (and being very thankfull for it existing!)\
Much help from Drewnabobber - Expatria Technologies Inc.\
Even more help, words of encouragement and swearing from JamesTheBard - sorry!

---

__Current Implemenation:__ 
```
    - RS485 Settings (DeviceID, Baudrate, DataBits, Parity, StopBits)
    - 6 Relay channels read and writeable as Coils
    - 8 Sensor Input Channels (Including internal PullUp/Down setting) readable as Discrete Input Registers
    - Basic ARGB statusLeds
```

__Roadmap:__

```
    - Implement button inputs for manual toolchange capability
    - Additional control schemes for tool magazine options
```
__Register Adresses:__

```
    - Relay Channels 1-6    - Modbus Register 1-6       (HexAddress: 0x0001 to 0x0006)
    - Sensor Inputs 1-8     - Modbus Register 257-264   (HexAddress: 0x0101 to 0x0108)
```

```
    - Example Modbus Command to enable Relay 3 on Modbus Device ID 2:

        0x02 0x05 0x00 0x03 0xFF 0x00 0x7C 0x09

    First Byte: Device ID                                           (Device ID 2)
    Second Byte: Function Code                                      (5 Write Coil)
    Third Byte: Register HighAddress Bit                            (00 = Address below 255)
    Fourth Byte: Register LowAddress Bit                            (03 = Register 3)
    Fifth Byte: DATA High Bit                                       
    Sixth Byte: DATA LOW BIT                                        (0xFF00 to turn on relay)
    Seventh and eigth Byte: 16 bits CRC16 Checksum

    - Example Modbus Command to Read Sensor 2 on Modbus Device ID 5:

        0x05 0x02 0x01 0x02 0x00 0x01 0x18 0x72

    First Byte: Device ID                                           (DeviceID 5)
    Second Byte: Function Code                                      (2 Read Discrete Input)
    Third and Fourth Byte: Register Adress to Start reading from    (Register: 258)
    Fifth and Sixth Byte: How many registers to read.                   (Read 1 Coil)
    Seventh and eigth Byte: 16 bits CRC16 Checksum                  

```

Git Commit - Minimum Viable Product: 22.04.2024\
Update - Sensors poll- and readable: 27.04.2024
