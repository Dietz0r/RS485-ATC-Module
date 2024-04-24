from Sensors import SensorHandling as sensor

class Report():
    def Sensor(self, reg_type: any, address: int, val: list[bool]) -> None:
        """Report Coil value to Terminal when read via Modbus given an address and a value via callback.
        Args:
            address (int): The address to change.
            val (list[bool]): The desired state of the relay.  Only the first value of the array is used, the rest are ignored.
            reg__type (any): Type of the register read.
        """
        sensor.Update(address, val)
        print(f'Read Sensor {address-256} as {reg_type} with value {val}.')
        