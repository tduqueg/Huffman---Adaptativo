class Nodo:
    def __init__(self, char=None):
        self.peso = 0
        self.padre = None
        self.derecha = None
        self.izquierda = None
        self.nivel = 0

        if char == None:
            self.char = [b'*']
        else:
            self.char = char

    def setIzq(self, nodo):
        self.izquierda = nodo
        nodo.padre = self
        nodo.updateLevel()

    def setDer(self, nodo):
        self.derecha = nodo
        nodo.padre = self
        nodo.updateLevel()

    def remplazarHijo(self, hijo, nodo):
        if self.izquierda == hijo:
            self.setIzq(nodo)
        elif self.derecha == hijo:
            self.setDer(nodo)

    def actNivel(self):
        self.nivel = self.padre.nivel +1
        if self.derecha:
            self.derecha.actNivel()
        if self.izquierda:
            self.izquierda.actNivel()
    
    def sinHijo(self):
        return self.izquierda == None and self.derecha == None

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
        padre1.rempazarHijo(self, nodo)



