
class UnoInfo:

    def __init__(self):
        self.dataPins = 13
        self.analogInPins = 5
        self.GND = 3
        self.pow = [3.3, 5]
        self.TX = 1
        self.RX = 0

    def getMainInfo(self):
        return {"0": self.dataPins, "1": self.GND, "2": self.pow}

    def getDigitalPins(self):
        return self.dataPins

    def getAnalogPins(self):
        return self.analogInPins

    def getAmountGND(self):
        return self.GND

    def getPowOut(self):
        return self.pow

    def getTXSlot(self):
        return self.TX

    def getRXSlot(self):
        return self.RX
