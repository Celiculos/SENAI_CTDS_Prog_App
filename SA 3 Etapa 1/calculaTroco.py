def calculaTroco(valorCompra, valorRecebido):
    troco = round(valorRecebido - valorCompra, 2)
    if troco < 0:
        print("O valor recebido não pode ser inferior ao da compra")
    elif troco == 0:
        print("Sem troco")
    else:
        print("Troco: R$ ", troco)
        imprimeTroco(minCedulas(troco))

def minCedulas(valor):
    cedulas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    troco = {}
    for cedula in cedulas:
        while(valor >= cedula):
            valor = round(valor - cedula, 2)
            if cedula in troco:
                troco[cedula] += 1
            else:
                troco[cedula] = 1
    return troco

def imprimeTroco(troco):
    for valor in troco:
        tipo = "Nota" if valor > 1 else "Moeda"
        print(troco[valor], tipo, ": R$ ", valor)

valorCompra =   float(input("Valor Total das Compras: R$ "))
valorRecebido = float(input("Valor Recebido: R$ "))
calculaTroco(valorCompra, valorRecebido)