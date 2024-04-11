### Main module for the MIDI footswitch.
### Supports three footswitches wth associated LEDs,
### each one toggles a controlled feature using the
### MIDI Control Change message.

import board
import digitalio
import LED
import Footswitch
import MIDIControl
import busio
import time

# The MIDI parameters for each footswitch can be changed here

FSW1_MIDI_CHANNEL = 1 # 1-indexed
FSW1_CC = 25
FSW1_OFF_VALUE = 0
FSW1_ON_VALUE = 127

FSW2_MIDI_CHANNEL = 1
FSW2_CC = 50
FSW2_OFF_VALUE = 0
FSW2_ON_VALUE = 127

FSW3_MIDI_CHANNEL = 1
FSW3_CC = 28
FSW3_OFF_VALUE = 0
FSW3_ON_VALUE = 127

# instantiate everything

led1 = LED.LED(digitalio.DigitalInOut(board.D0))
led2 = LED.LED(digitalio.DigitalInOut(board.D10))
led3 = LED.LED(digitalio.DigitalInOut(board.D9))

midiOut = busio.UART(board.TX, board.RX, baudrate=31250)

fsw1 = Footswitch.Footswitch(digitalio.DigitalInOut(board.D5))
fsw2 = Footswitch.Footswitch(digitalio.DigitalInOut(board.D4))
fsw3 = Footswitch.Footswitch(digitalio.DigitalInOut(board.D3))

fsw1Control = MIDIControl.MIDIControl(FSW1_MIDI_CHANNEL, FSW1_CC, FSW1_OFF_VALUE, FSW1_ON_VALUE, fsw1, led1, midiOut)
fsw2Control = MIDIControl.MIDIControl(FSW2_MIDI_CHANNEL, FSW2_CC, FSW2_OFF_VALUE, FSW2_ON_VALUE, fsw2, led2, midiOut)
fsw3Control = MIDIControl.MIDIControl(FSW3_MIDI_CHANNEL, FSW3_CC, FSW3_OFF_VALUE, FSW3_ON_VALUE, fsw3, led3, midiOut)

# flash LEDs to confirm power
led1.on()
led2.on()
led3.on()
time.sleep(2)
led1.off()
led2.off()
led3.off()

# a bit more flashing
for i in range(3/0.3):
    led1.on()
    time.sleep(0.1)
    led1.off()
    led2.on()
    time.sleep(0.1)
    led2.off()
    led3.on()
    time.sleep(0.1)
    led3.off()

# loop forever, servicing footswitch state changes
while True:
    fsw1Control.loop()
    fsw2Control.loop()
    fsw3Control.loop()
