from queue import Queue
from nodo import Nodo

class ArbolHuffman:
    def __init__(self, order=1):
        self.raiz = Nodo()
        self.bytes = {}
        self.nodoVacio = self.raiz
        self.order = order
        self.contador = 0

    def existe(self, char):
        return char in self.bytes

    def addChar(self, char):
        nodo = Nodo(char)
        self.bytes[char] = nodo
        self.nodoVacio.setIzq(Nodo())
        self.nodoVacio.setDer(nodo)
        self.nodoVacio = self.nodoVacio.izq


#codificador
    def codificador(self, file):
        char = b''
        char = file.read(self.order)
        if char==b'':
            return b''
        
        if not self.existe(char):
            codigo = self.codigoHuffman(self.nodoVacio)
            for i in range(len(char)):
                codigo += '{0:08b}'.format(char[i]) #Binario
            self.addChar(char)
        else:
            nodo = self.bytes[char]
            codigo = self.codigoHuffman(nodo)

        self.actualizarArbol(self.bytes[char])
        return codigo

    def finArchivo(self):
        return self.codigoHuffman(self.nodoVacio)

    def codigoHuffman(self, nodo):
        codigo = ''
        if nodo == self.raiz:
            return '0'
        padre = nodo.padre
        while padre:
            if padre.izq == nodo:
                codigo += '0'
            else:
                codigo += '1'
            nodo = padre
            padre = nodo.padre

        return codigo[::-1] # Reversa

    def encontrarElMasLejano(self, peso):
        q = Queue()
        q.put(self.raiz)
        while not q.empty():
            nodo = q.get()
            if nodo.peso == peso:
                return nodo
            if nodo.der:
                q.put(nodo.der)
            if nodo.izq:
                q.put(nodo.izq)
            
    def actualizarArbol(self, nodo):
        while nodo:
            nodo.cambio(self.encontrarElMasLejano(nodo.peso))
            nodo.peso += 1
            nodo = nodo.padre


# Decodificador
    def decodificador(self, file):
        if self.contador <= 0:
            return ''
        nodo = self.reHuffmancod(file)
        if nodo == self.nodoVacio:
            codigo = ''
            for i in range(self.order):
                codigo += file.leer(8)
            
            char = nodo.char
            for i in range(int(len(codigo)/8)):
                ch= int(codigo[i*8:i*8+8], 2)
                char += ch.to_bytes(1, byteorder='little')
            self.addChar(char)
        else:
            char = nodo.char
        self.actualizarArbol(self.bytes[char])
        self.contador -= len(char)
        return char 

    def reHuffmancod(self, file):
        if self.raiz.sinHijo():
            file.leer(1)
            return self.raiz
            
        nodo = self.raiz
        while not nodo.sinHijo():
            ch = file.leer(1)
            if ch == '0':
                nodo = nodo.izq
            elif ch == '1':
                nodo = nodo.der
            else:
                return self.nodoVacio

        return nodo

    def printArbol(self):
        print('-------- El Mejor Árbol --------')
        q = Queue()
        q.put(self.raiz)
        nivel = 0
        while not q.empty():
            nodo = q.get()
            if nodo.nivel > nivel:
                nivel = nodo.nivel
                print()
            print("[",str(nodo.char),nodo.peso,"]")
            if nodo.izq:
                q.put(nodo.izq)
            if nodo.der:
                q.put(nodo.der)
        print('\n')
    