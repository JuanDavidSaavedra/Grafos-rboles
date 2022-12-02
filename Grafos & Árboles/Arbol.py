#Un arbol tiene 2 hijos
class Nodo:
    def _init_(self,x):
        self.der=None
        self.izq=None
        self.valor=x        

def preorden(nodo):   #arranca en la raiz
    if nodo:
        print(nodo.valor)
        preorden(nodo.der)
        preorden(nodo.izq)
        
def inorden(nodo):    #mitad de la raiz
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor)
        inorden(nodo.der)

def postorden(nodo):    #ultimo de la raiz
    if nodo:
        postorden(nodo.der)
        postorden(nodo.izq)
        print(nodo.valor)
        
raiz=Nodo("1")
raiz.der=Nodo("2")
raiz.izq=Nodo("5")
raiz.der.der=Nodo("3")
raiz.der.izq=Nodo("4")
raiz.izq.der=Nodo("6")
raiz.izq.izq=Nodo("7")
raiz.izq.izq.der=Nodo("7")
raiz.izq.izq.izq=Nodo("7")

preorden(raiz)     # siempre la derecha inicia de 1

#inorden(raiz)       # recorrer del primero a la izquierda y empezar a subir hasta llegar al ultimo a la derecha 

#postorden(raiz)     # rama rama raiz, agotar los hijos y depues agota los padres