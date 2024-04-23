class Report():
    def Echo(self, reg_type: any, address: int, val: list[bool]) -> None:
        """Report Coil value to Terminal when read via Modbus given an address and a value via callback.
        Args:
            address (int): The address to change.
            val (list[bool]): The desired state of the relay.  Only the first value of the array is used, the rest are ignored.
            reg__type (any): Type of the register read.
        """
        if address <= 255:
            print(f'Read Register {address} as {reg_type} with value {val}.')
        if address >= 256:
            print(f'Read Sensor {address-256} as {reg_type} with value {val}.')
        