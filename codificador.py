import os
from bitStream import BitStream
from ArbolHuffman import ArbolHuffman
import time
import concurrent.futures
import dividirArchivos





class Codificador:
    
    def __init__(self):
        self.arbol = ArbolHuffman(1)
        self.file_number = 1

    def codificarArchivo(self, nombreArch, outNombreArch,file_number):
        path_archivo = "./archivos"
        nombreArch = f'/texto_parte_{file_number}.txt'
        path_archivo = path_archivo + nombreArch
        
        if not os.path.exists(path_archivo):
            print('El archivo no existe.')
            return
        leerArchivo = open(path_archivo, 'rb')
        escribirArchivo = BitStream(outNombreArch, 'wb')
        escribirArchivo.escribir('{0:032b}'.format(os.stat(path_archivo).st_size))
        while True:
            codigo = self.arbol.codificador(leerArchivo)
            if not codigo:
                break
            escribirArchivo.escribir(codigo)
        self.arbol.printArbol()
        escribirArchivo.cerrar()
        leerArchivo.close()
        




if __name__ == '__main__':
    start = time.perf_counter()
    codificador = Codificador()
    file_number = 1
    for _ in range(file_number):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(codificador.codificarArchivo(f'./archivos/texto_parte_{file_number}.txt',f'./textoCodificado/codigo_parte_{file_number}.txt',1),range(file_number))
        file_number += 1
        

# {    codificador.codificarArchivo('./README.md','./codigo.txt')}
    finish = time.perf_counter()
    print(f'FInalizado en  {round(finish-start, 2 )} segundo(s)')