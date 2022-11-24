import os
from bitStream import BitStream
from ArbolHuffman import ArbolHuffman


class Decodificador:
    def __init__(self):
        self.arbol = ArbolHuffman(1)

    def decoArchivo(self, fileName, outFileName):
        if not os.path.exists(fileName):
            print('El archivo no existe.')
            return
        leerArchivo = BitStream(fileName, 'rb')
        escribirArchivo = open(outFileName,'wb')
        self.arbol.contador = int(leerArchivo.leer(32), 2)
        while True:
            char = self.arbol.decodificador(leerArchivo)
            if not char:
                break
            escribirArchivo.write(char)

        leerArchivo.cerrar()
        escribirArchivo.close()

if __name__ == '__main__':
    decodificador = Decodificador()
    i = 1
    decodificador.decoArchivo(f'./textoCodificado/codigo_parte_{i}.txt',f'./decodificado_{i}.txt')
