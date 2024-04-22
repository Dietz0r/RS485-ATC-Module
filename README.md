## RS485 ATC Module ##

__Scope:__ 
This is meant to be a standalone ATC module for the [Waveshare ESP32-S3-relay-6CH](https://www.waveshare.com/esp32-s3-relay-6ch.htm) capable of adding additionl I/O capability to CNC Mills. The I/O, including 6 relay output channels, are controlled over the RS485 Interface to provide a reliable industry standard way of connecting it to existing CNC control hardware with minimal effort.

Developed with help and for the [PrintNC community](https://wiki.printnc.info/en/home) alongside the [grblHAL2000](https://github.com/Expatria-Technologies/grblhal_2000_PrintNC) and [flexiHAL](https://expatria.myshopify.com/products/flexi-hal) by [Expatria Technologies Inc.](https://github.com/Expatria-Technologies) boards for [grblHAL](https://github.com/grblHAL) by [TerjeIO](https://github.com/terjeio) with RS485 ModbusRTU support
Written in MicroPython for to allow for easy modification and adaption to other ESP32 or MicroPython capable of the shelf boards.

__Credits:__

Using the [MicroPython Modbus library](https://github.com/brainelectronics/micropython-modbus) by [brainelectronics](https://github.com/brainelectronics)(and being very thankfull for it existing!)
Much help from Drewnabobber - Expatria Technologies Inc.

---

__Current Implemenation:__ 
```
    - RS485 Settings (DeviceID, Baudrate, DataBits, Parity, StopBits)
    - 6 Relay Channels read and writeable as Coils on address 0x01 to 0x06
    - Basic ARGB StatusLeds
```

Git Commit - Minimum Viable Product: 22.04.2024 
