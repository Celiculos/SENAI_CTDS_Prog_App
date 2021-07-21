def bubbleSort(lista):
    for numero in range(len(lista) -1, 0,-1):
        for i in range(numero):
            if(lista[i] > lista[i+1]):
                temp = lista[i]
                lista[i]   = lista[i+1]
                lista[i+1] = temp

print("BUBBLESORT")
lista   = []
tamanho = int(input("Informe o tamanho da lista: "))
for i in range(tamanho):
    lista.append(int(input("Informe um valor para a lista: ")))
bubbleSort(lista)
print("Lista ordenada: ")
print(lista)