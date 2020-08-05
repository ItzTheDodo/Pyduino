# Function Credits: https://github.com/lekum/pyduino/blob/master/pyduino/pyduino.py (lekum (as of 2014))
# Written By: ItzTheDodo

from Pyduino.Boards.Uno import UnoInfo
from Pyduino.Boards.Mega import MegaInfo
from Pyduino.Boards.Diecimila import DiecimilaInfo
from Pyduino.Boards.Due import DueInfo
from Pyduino.Boards.Nano import NanoInfo
from Pyduino.Boards.Mini import MiniInfo
from Pyduino.Boards.Lilypad import LilypadInfo
from Pyduino.Boards.CustomBoardProfile import BoardProfileInfo
from Pyduino.Utils.Pins import *
from Pyduino.Utils.ReadWrite import *
from Pyduino.Utils.ReadOnly import *
import serial
import time
import sys


class Pyduino(object):

    def __init__(self, board, serial_port='COM5', baud_rate='9600', read_timeout=5):

        __metaclass__ = ReadOnly

        self.serialPort = serial_port
        self.baudRate = baud_rate
        self.readTimeout = read_timeout

        self.board = board
        self.run = True
        self.pinnames = {}
        self.pins = {}
        self.pinModes = {}
        self.conn = serial.Serial(self.serialPort, self.baudRate)
        self.conn.timeout = self.readTimeout

        if self.board.lower() == "uno":
            self.boardinfo = UnoInfo()
        elif self.board.lower() == "mega":
            self.boardinfo = MegaInfo()
        elif self.board.lower() == "diecimila":
            self.boardinfo = DiecimilaInfo()
        elif self.board.lower() == "due":
            self.boardinfo = DueInfo()

    def getBoardType(self):
        return self.board

    def getBoardInfo(self):
        return self.boardinfo

    def getPinsInUse(self):
        return self.pins

    def mainloop(self, loop, *params):

        while self.run:

            loop(*params)

    def setup(self, definition, *params):

        definition(*params)

    def define(self, name, pin):

        if pin > self.boardinfo.getMainInfo()[0]:
            return

        self.pinnames[name] = pin
        return name

    def setPin(self, pin, option):

        if option != HIGH or option != LOW:
            return

        dv = None

        if option == HIGH:
            dv = 1
        elif option == LOW:
            dv = 0

        if type(pin) is str:
            a = self.pinnames[pin]

            self.pins[str(a)] = option

            command = ("DW:" + str(a) + ":" + str(dv)).encode()
            self.conn.write(command)

        elif type(pin) is int:

            if pin > self.boardinfo.getMainInfo()[0]:
                return

            self.pins[str(pin)] = option

            command = ("DW:" + str(pin) + ":" + str(dv)).encode()
            self.conn.write(command)
        else:
            return

    def newSerial(self, serial_port, baud_rate, read_timeout):
        self.conn = serial.Serial(serial_port, baud_rate)
        self.conn.timeout = read_timeout

    def pinMode(self, pin, mode):

        if mode != INPUT or mode != OUTPUT or mode != INPUT_PULLUP:
            return

        m = ""

        if mode == INPUT:
            m = "I"
        elif mode == OUTPUT:
            m = "O"
        elif mode == INPUT_PULLUP:
            m = "P"
        else:
            return

        if type(pin) is str:
            a = self.pinnames[pin]

            self.pins[str(a)] = mode

            command = ("M:" + str(a) + ":" + m).encode()
            self.conn.write(command)

        elif type(pin) is int:

            if pin > self.boardinfo.getMainInfo()[0]:
                return

            self.pins[str(pin)] = mode

            command = ("M:" + str(pin) + ":" + m).encode()
            self.conn.write(command)
        else:
            return

    def newReadWrite(self, pin, digitalval=None, analogval=None):

        if digitalval is not None and analogval is not None:
            return ReadWrite(self.conn, pin, digitalval=digitalval, analogval=analogval)
        elif digitalval is not None:
            return ReadWrite(self.conn, pin, digitalval=digitalval)
        elif analogval is not None:
            return ReadWrite(self.conn, pin, analogval=analogval)
        else:
            return ReadWrite(self.conn, pin)

    def createCustomBoardProfile(self, datapins, analogInPins, GND, pow, TX, RX):
        self.boardinfo = BoardProfileInfo(datapins, analogInPins, GND, pow, TX, RX)

    def delay(self, t):
        a = int(t) / 1000
        time.sleep(a)

    def stop(self):
        sys.exit(2)


if __name__ == "__main__":

    # set all pins high for 1 sec then low for 0.5 sec

    p = Pyduino("Uno")

    for i in range(p.getBoardInfo().getMainInfo()["0"]):
        p.pinMode(i, OUTPUT)

    while True:
        for i in range(p.getBoardInfo().getMainInfo()["0"]):
            p.setPin(i, HIGH)
        p.delay(1000)
        for i in range(p.getBoardInfo().getMainInfo()["0"]):
            p.setPin(i, LOW)
        p.delay(500)
