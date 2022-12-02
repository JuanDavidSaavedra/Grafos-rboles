# Función recursivo para imprimir la ruta del vértice `u` dado desde el vértice fuente `v`
def printPath(path, v, u, route):
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])
 
 
# Función # para imprimir el costo más corto con ruta
# Información # entre todos los pares de vértices
def printSolution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                printPath(path, v, u, route)
                route.append(u)
                print(f'Camino mas corto {v} —> {u} es', route ,  " -> El tamaño es: ",str(sum(route)))
 
 
# Función # para ejecutar el algoritmo de Floyd-Warshall
def floydWarshall(adjMatrix):
 
    # Caja base
    if not adjMatrix:
        return
 
    # número total de vértices en `adjMatrix`
    n = len(adjMatrix)
 
    # La matriz de ruta y costo # almacena la ruta más corta
    # Información de # (costo más corto/ruta más corta)
 
    # inicialmente, el costo sería el mismo que el peso de un borde
    cost = adjMatrix.copy()
    path = [[None for x in range(n)] for y in range(n)]
 
    # inicializa el costo y la ruta
    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1
 
    # ejecuta Floyd-Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # Si el vértice `k` está en el camino más corto de `v` a `u`,
                # luego actualice el valor de cost[v][u] y path[v][u]
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
 
            # si los elementos diagonales se vuelven negativos, el
            # El graph # contiene un ciclo de peso negativo
            if cost[v][v] < 0:
                print('Peso negativo encontrado')
                return
 
    # Imprime el camino más corto entre todos los pares de vértices
    printSolution(path, n)
 
 
if __name__ == '__main__':
 
    # definir infinito
    I = float('inf')
 
    # Dada la representación de adyacencia de la matriz
    adjMatrix =  [  
            [0,    1,  3,  I, I],  
            [1,    0,  1,   4 , I],
            [3,    1,  0,  I, 6  ],
            [I,  4, I,   0, 5  ],
            [I,I,   6,   5, 0]
        ]
 
    # Ejecutar el algoritmo de Floyd-Warshall
    floydWarshall(adjMatrix)