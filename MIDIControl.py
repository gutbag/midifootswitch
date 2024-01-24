import Footswitch
import LED

class MIDIControl:
    ### Represents the MIDI-controlled feature that is enabled and
    ### disabled with a footswitch, and the state displayed with an LED.

    def __init__(self, aMidiChannel, aCC, anOffValue, anOnValue, aFootswitch, anLed, aMidiOut):
        self.midiChannel = aMidiChannel
        self.cc = aCC
        self.offValue = anOffValue
        self.onValue = anOnValue
        self.footswitch = aFootswitch
        self.led = anLed
        self.midiOut = aMidiOut
        self.currentOnState = False

        self.__off()

    def loop(self):
        if self.footswitch.hasChanged():
            print("Control has changed")
            if self.footswitch.wasPressed():
                if self.currentOnState:
                    self.__off()
                else:
                    self.__on()

                self.currentOnState = not self.currentOnState

    def __on(self):
        self.midiOut.write(bytes([0xb0 | (self.midiChannel-1), self.cc, self.onValue]))
        self.led.on()

    def __off(self):
        self.midiOut.write(bytes([0xb0 | (self.midiChannel-1), self.cc, self.offValue]))
        self.led.off()

