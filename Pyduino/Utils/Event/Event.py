from Pyduino.Utils.Event.EventTypes.OnPinHigh import *
from Pyduino.Utils.Event.EventTypes.OnPinLow import *
from Pyduino.Utils.Event.Listener import Listener


class Event:

    def __init__(self, Type, pinsFromPyduino, execute, *args):

        self.type = Type
        self.pins = pinsFromPyduino
        self.run = True

        if self.type is onPinHigh or self.type is onPinLow:
            self.pin = self.type.getPin()

        L = Listener(self.type, self.pins)

        while self.run:
            if L.getStat() is self.type:
                execute(*args)

    def setCancelled(self):

        if self.type is onPinHigh:
            return onPinLow(self.pin)
        elif self.type is onPinLow:
            return onPinLow(self.pin)

    def getPin(self):
        return self.pin

    def cancel(self):
        self.run = False
