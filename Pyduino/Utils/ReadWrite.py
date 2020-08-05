
class ReadWrite:

    def __init__(self, conn, pinnum, digitalval=None, analogval=None):

        self.pin_number = pinnum
        self.conn = conn

        if digitalval is not None:
            self.digital_value = digitalval
        if analogval is not None:
            self.analog_value = analogval

    def digitalread(self):
        comm = ("DR:" + str(self.pin_number)).encode()
        self.conn.write(comm)
        lirec = self.conn.readline().decode().strip()
        header, val = lirec.split(':')
        if header == ('D' + str(self.pin_number)):
            return int(val)

    def digitalwrite(self):
        if type(self.digital_value) is not int:
            return
        if type(self.pin_number) is not int:
            return
        command = ("DW:" + str(self.pin_number) + ":" + str(self.digital_value)).encode()
        self.conn.write(command)

    def analogread(self):
        comm = ("AR:" + str(self.pin_number)).encode()
        self.conn.write(comm)
        lirec = self.conn.readline().decode().strip()
        header, val = lirec.split(':')
        if header == ('A' + str(self.pin_number)):
            return int(val)

    def analogwrite(self):
        comm = ("AW:" + str(self.pin_number) + ":" + str(self.digital_value)).encode()
        self.conn.write(comm)
