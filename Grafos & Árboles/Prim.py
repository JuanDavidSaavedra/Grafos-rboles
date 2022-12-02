#Algoritmo de recorrido de grafos Prim 

def prim(p,n,x):
    #P = "pesos de las aristas"
    #N = "cantidad de vertices"
    #X = "Vertice por el que se empieza"

    v=[]
    while(len(v) !=n):
        v.append(0)
    v[x] = 1

    # C es el conjunto de aristas 
    c= []
    for i in range(0,n-1):
        min = 10
        agregar_vertice =0
        e = []
        for j in range(0,n):
            if(v[j]==1):
                for k in range(0,n):
                    if(v[k]==0 and p[j][k] < min):
                        agregar_vertice = k
                        e =[j,k]
                        min = p[j][k]
        v[agregar_vertice] = 1
        c.append(e)
    return c

print("Bienvenido")
print("Codigo para recorrido de grafos Prim")
n = int(input("Digite la cantidad de vertices del grafo: "))
x= int(input("Digite el vertice inicial: "))
p=[
    [9,4,2,9,3,9],#0
    [4,9,9,5,9,9],#1
    [2,9,9,1,6,3],#2
    [9,5,1,9,9,6],#3
    [3,9,6,9,9,2],#4
    [9,9,3,6,2,9],#5
    [8,3,2,3,4,5],#6
]
print("El camino más corto es: ")
print(prim(p,n,x))