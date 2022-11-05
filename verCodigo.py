import os
from bitStream import BitStream

class Observador:
    def __init__(self):
        pass

    def ver(self, fileName):
        if not os.path.exists(fileName):
            print('El archivo no existe.')
            return
        leerArchivo = BitStream(fileName, 'rb')
        for i in range(100):
            c = leerArchivo.leer(8)
            if not c:
                break
            print(c)
        leerArchivo.cerrar()

if __name__ == '__main__':
    observador = Observador()
    observador.ver('./codigo.txt')
