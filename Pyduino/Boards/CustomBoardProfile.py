
class BoardProfileInfo:

    def __init__(self, datapins, analogInPins, GND, pow, TX, RX):
        self.dataPins = datapins
        self.analogInPins = analogInPins
        self.GND = GND
        self.pow = pow
        self.TX = TX
        self.RX = RX

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
