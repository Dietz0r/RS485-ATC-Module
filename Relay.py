from Settings import Relay

relay = Relay()


class RelayControl:
    def __init__(self):
        self.relay_status = [False] * relay.channels  # Relay current status flag
        for i in range(relay.channels):
            # Relay.Channel[i].off()
            relay.get_channel(i).off()
        print(f'Reset relays on boot.')

    # Relay Logic for RS485Callback
    # coils are bool (val = Union[true/false])
    def set_relay(self, reg_type: any, address: int, val: list[bool]) -> None:
        """Set the state of a relay given an address and a value via callback.
        Args:
            address (int): The address to change.
            val (list[bool]): The desired state of the relay.  Only the first value of the array is used, the rest are ignored.
            reg_type (any): Not used by the function, but defined for compatibility reasons.
        """
        channel = relay.get_channel(address - 1)
        if val[0] and not self.relay_status[address - 1]:
            channel.on()
            self.relay_status[address - 1] = True
            print(f'Relay {address} on')
        elif not val[0] and self.relay_status[address - 1]:
            channel.off()
            self.relay_status[address - 1] = False
            print(f'Relay {address} off')
        else:
            print(f'Channel {address} command received - No change.')
