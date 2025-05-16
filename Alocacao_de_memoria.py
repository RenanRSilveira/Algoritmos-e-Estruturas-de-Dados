x = 2337
y = x
print(id(x))

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
indice = 0

for x in range(len(lista)):
    if lista[x] % 2 == 0:
        lista.insert(indice, lista.pop(x))
        indice += 1

print(lista)

