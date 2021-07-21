l = []
l.append(int(input("Digite um número: ")))
l.append(int(input("Digite outro número: ")))
l.append(int(input("Digite mais um número: ")))
l.append(int(input("Digite um último número: ")))
print ("Positivo" if sum(l) / len(l) > 1 else "Negativo")