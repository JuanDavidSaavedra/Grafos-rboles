# Una clase para representar un conjunto disjunto
class DisjointSet:
    parent = {}
 
    # realiza la operación MakeSet
    def makeSet(self, n):
        # crear `n` conjuntos disjuntos (uno para cada vértice)
        for i in range(n):
            self.parent[i] = i
 
    # Encuentra la raíz del conjunto al que pertenece el elemento `k`
    def find(self, k):
        # si `k` es root
        if self.parent[k] == k:
            return k
 
        # recurre para el padre hasta que encontramos la raíz
        return self.find(self.parent[k])
 
    # Realizar unión de dos subconjuntos
    def union(self, a, b):
        # encontrar la raíz de los conjuntos a los que pertenecen los elementos `x` e `y`
        x = self.find(a)
        y = self.find(b)
 
        self.parent[x] = y
 
 
# Función # para construir MST usando el algoritmo de Kruskal
def runKruskalAlgorithm(edges, n):
 
    # almacena los bordes presentes en MST
    MST = []
 
    # Inicializa la clase `DisjointSet`.
    # Crea un conjunto singleton para cada elemento del universo.
    ds = DisjointSet()
    ds.makeSet(n)
 
    index = 0
 
    # ordena los bordes aumentando el peso
    edges.sort(key=lambda x: x[2])
 
    # MST contiene exactamente aristas `V-1`
    while len(MST) != n - 1:
 
        # considerar el borde siguiente con peso mínimo del graph
        (src, dest, weight) = edges[index]
        index = index + 1
 
        # encontrar la raíz de los conjuntos a los que se unen dos extremos
        # vértices de la siguiente arista pertenecen
        x = ds.find(src)
        y = ds.find(dest)
 
        # si ambos extremos tienen diferentes padres, pertenecen a
        # diferentes componentes conectados y se pueden incluir en MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)
 
    return MST
 
 
if __name__ == '__main__':
 
    # (u, v, w) el triplete representa un borde no dirigido desde
    # vértice `u` a vértice `v` con peso `w`
    edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    
    ]
 
    # número total de nodos en el graph (etiquetados de 0 a 6)
    n = 7
 
    # graph de construcción
    e = runKruskalAlgorithm(edges, n)
    
    print(e)