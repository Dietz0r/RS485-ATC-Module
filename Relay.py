from Settings import Relay

Relay = Relay()

class RelayControl():
    def __init__(self):
        self.Relay_Status = [False] * Relay.RelayNum  # Relay current status flag
        for i in range(Relay.RelayNum):
            Relay.Channel[i].off()
        print(f'Reset relays on boot.')

    # Relay Logic for RS485Callback
    # coils are bool (val = Union[true/false])
    def SetRelay(self, reg_type: any, address: int, val: list[bool]) -> None:
        """Set the state of a relay given an address and a value via callback.
        Args:
            address (int): The address to change.
            val (list[bool]): The desired state of the relay.  Only the first value of the array is used, the rest are ignored.
            reg_type (any): Not used by the function, but defined for compatibility reasons.
        """
        if val[0] and not self.Relay_Status[address-1]:
            Relay.Channel[address-1].on()
            self.Relay_Status[address-1] = True
            print(f'Relay {address} on')
        elif not val[0] and self.Relay_Status[address-1]:
            Relay.Channel[address-1].off()
            self.Relay_Status[address-1] = False
            print(f'Relay {address} off')
        else:
            print(f'Channel {address} command received - No change.')
