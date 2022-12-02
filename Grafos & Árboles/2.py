grafo={"A": ["B", "C"], "B": ["C","D"], "C": ["D","E"], "D": ["E"], "E":["F","G"], "F":[], "G":[], "D":["H", "I"], "H":[], "I":[]}

origen = input("Digite orígen: ")
if origen.upper() not in grafo:
    print("Nodo Origen no está en grafo")
else:
    C = 0
    recorrido = []
    terminales = []
    visitados = [origen]

    while(len(visitados) != 0):
        nodo = visitados.pop()
        if nodo.upper() not in recorrido:
            recorrido.append(nodo.upper())
            C = C + 1
    
        if nodo.upper() not in grafo:
            continue

        if len(grafo[nodo.upper()])==0:
            if nodo.upper() not in terminales:
                terminales.append(nodo.upper())
                C = C + 1

        for i in grafo[nodo.upper()]:
            visitados.append(i)

    print(recorrido)