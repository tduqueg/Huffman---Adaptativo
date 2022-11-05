# bit <-> str
import string


class BitStream:
    def __init__(self, fileName, mode):
        self.file = open(fileName, mode)
        self.buffer = 0
        if mode[0] == 'r':
            self.pos = -1
        elif mode[0] == 'w':
            self.pos = 7
        self.mode = mode

    def leer(self, size):
        a= ''
        for i in range(size):
            if self.pos == -1:
                self.buffer = self.file.read(1)
                if self.buffer == b'':
                    return ''
                else:
                    self.buffer = ord(self.buffer)
                    self.pos = 7
            if self.buffer & (1 << self.pos):
                a += '1'
            else:
                a += '0'
            self.pos -= 1
        return a

    def escribir(self, str):
        for char in str:
            if char == '0':
                self.buffer <<= 1
                self.pos -= 1
            elif char == '1':
                self.buffer <<= 1
                self.buffer += 1
                self.pos -= 1
            else:
                continue
            if self.pos == -1:
                self.vaciar()

    def cerrar(self):
        if self.mode[0] == 'w':
            self.vaciar()
        self.file.close()

    def vaciar(self):
        if self.pos != 7:
            while self.pos > -1:
                self.buffer <<= 1
                self.pos -= 1
            self.file.write(self.buffer.to_bytes(1, byteorder='little'))
        self.pos = 7
        self.buffer = 0
