l = []
for pos in range(20):
  l.append(int(input("Digite um número: ")))
print("Maior valor")
print(max(l))
print()
print("Menor valor")
print(min(l))
print("Média")
print(sum(l) / len(l))