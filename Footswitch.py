from digitalio import Direction, Pull
import supervisor
import ticks

DEBOUNCE_MS = 20

class Footswitch:
    ### Represents a footswitch associated with a digital input

    def __init__(self, input):
        self.input = input
        self.input.direction = Direction.INPUT
        self.input.pull = Pull.UP
        self.storedState = True # pullup will make default True
        self.actualState = True
        self.stateChangeMs = 0

    def hasChanged(self):
        ### Returns True if the footswitch state has changed

        stateChanged = False
        stateNow = self.input.value
        nowMs = supervisor.ticks_ms()
        if stateNow != self.storedState: # the state has changed
            self.storedState = stateNow
            self.stateChangeMs = nowMs
        else: # has enough time elapsed since the last change?
            if ticks.diff(nowMs, self.stateChangeMs) >= DEBOUNCE_MS:
                if stateNow != self.actualState:
                    stateChanged = True

                self.actualState = stateNow

        return stateChanged

    def wasPressed(self):
        ### Returns True if the footswitch was pressed and released
        return self.actualState
