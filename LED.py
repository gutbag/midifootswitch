import digitalio

class LED:
    ### Represents an LED associated with a digital output

    def __init__(self, pin):
        self.pin = pin
        self.pin.direction = digitalio.Direction.OUTPUT

        self.off()

    def on(self):
        self.pin.value = False

    def off(self):
        self.pin.value = True
