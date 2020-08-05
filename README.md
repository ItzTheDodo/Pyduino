# Pyduino
A python library for controlling an Arduino over serial connection

This Library supports a range of boards and functions aimed at people with variable knowlege of python and good knowlege of the arduino language

Constants:
 - HIGH
 - LOW
 - INPUT
 - OUTPUT
 - INPUT_PULLUP

Functions:
 - getBoardType()
 - getBoardInfo()
 - getPinsInUse()
 - mainloop(loop, *params)
 - setup(func, *params)
 - define(name, pin)
 - setPin(pin, option)
 - newSerial(serialPort, baudRate, readTimeout)
 - pinMode(pin, mode)
 - newReadWrite(pin, *digitalValue, *analogValue)
 - createCustomBoardProfile(dataPins, analogInPins, GND, pow, TX, RX)
 - delay(time)
 - stop()
 
 Boards Supported:
  - Diecimila
  - Due
  - Lilypad
  - Mega
  - Mini
  - Nano
  - Uno
