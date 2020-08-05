from Pyduino.Utils.Event.EventTypes.OnPinHigh import *
from Pyduino.Utils.Event.EventTypes.OnPinLow import *
from Pyduino.Utils.Pins import *


class Listener:

    def __init__(self, t, pinsListFromMain):

        self.type = t
        self.pins = pinsListFromMain
        self.run = True
        self.stat = None

        while self.run:

            for i in self.pins:

                if i == str(self.type.getPin()):
                    stat = self.pins[i]

                    if stat == HIGH and self.type == onPinHigh:
                        self.stat = onPinHigh

                    if stat == LOW and self.type == onPinLow:
                        self.stat = onPinLow

    def cancel(self):
        self.run = False

    def getType(self):
        return self.type

    def getStat(self):
        return self.stat
