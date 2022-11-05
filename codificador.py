import os
from bitStream import BitStream
from ArbolHuffman import ArbolHuffman

class Codificador:
    def __init__(self):
        self.arbol = ArbolHuffman(1)

    def codificarArchivo(self, nombreArch, outNombreArch):
        if not os.path.exists(nombreArch):
            print('El archivo no existe.')
            return
        leerArchivo = open(nombreArch, 'rb')
        escribirArchivo = BitStream(outNombreArch, 'wb')
        escribirArchivo.escribir('{0:032b}'.format(os.stat(nombreArch).st_size))
        while True:
            codigo = self.arbol.codificador(leerArchivo)
            if not codigo:
                break
            escribirArchivo.escribir(codigo)
        self.arbol.printArbol()
        escribirArchivo.cerrar()
        leerArchivo.cerrar()

if __name__ == '__main__':
    codificador = Codificador()
    codificador.codificarArchivo('./readme.md','./codigo.txt')