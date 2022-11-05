class Nodo:
    def __init__(self, char=None):
        self.peso = 0
        self.padre = None
        self.der = None
        self.izq = None
        self.nivel = 0

        if char == None:
            self.char = b''
        else:
            self.char = char

    def setIzq(self, nodo):
        self.izq = nodo
        nodo.padre = self
        nodo.actNivel()

    def setDer(self, nodo):
        self.der = nodo
        nodo.padre = self
        nodo.actNivel()

    def remplazarHijo(self, hijo, nodo):
        if self.izq == hijo:
            self.setIzq(nodo)
        elif self.der == hijo:
            self.setDer(nodo)

    def actNivel(self):
        self.nivel = self.padre.nivel +1
        if self.der:
            self.der.actNivel()
        if self.izq:
            self.izq.actNivel()
    
    def sinHijo(self):
        return self.izq == None and self.der == None

    def esAncestro(self, nodo):
        ancestro = self.padre
        while ancestro:
            if ancestro == nodo:
                return True
            ancestro = ancestro.padre
        return False
    
    def cambio(self,nodo):
        if self == nodo or nodo.esAncestro(self) or self.esAncestro(nodo):
            return
        padre1 = self.padre
        padre2 = nodo.padre
        padre2.remplazarHijo(nodo, self)
        padre1.remplazarHijo(self, nodo)



