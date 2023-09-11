letras = list("Python")

print(letras)
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

frutas = ["Maça", "laranja", "Uva", "pera"]
print(frutas[0])
print(frutas[-1])
print(frutas[2])
print(frutas[-3])

matriz =[
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

carros = ["goal", "celta", 'palio']
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

"""
List Comprehension
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
"""

numeros = [1, 30, 21, 2, 9, 65, 34]
# Números pares
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Números impares
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)


""" Métodos da classe list
    .append(Aqui vai o elemento que vai ser adicionado. Lembrando que o append adiciona na última posição)
    .clear() limpa os valores dentro da lista
    .copy() copia os valores d lista e joga para outro lugar, sem apontar para o mesmo lugar daa ram
    .count(objeto) conta quantas vezes o objeto que colocou aparece na lista
    .extend([objeto]) Serve para juntar mais de um valor ao mesmo tempo, no final da lista
    .index(objeto) mostra a posição em que o objeto primeiro se encontra dentro da lista
    .pop() retira o último objeto dentro da lista, ou, se passar algum número para ele, o número desejado
    .remove(objeto) retira o objeto em si, ou seja, o que você passou.
    .reverse() inverte a posição da lista, é como se fosse o fatiamento ::-1
    .sort() coloca a lista ordenada pelo alfabeto
    .sort(reverse = True) ela faz o espelhamento
    .sort(key = lambda x: len(x)) faz para organizar de forma crescente no número de caracteres
    len() mostra a quantidade de elementos na lista

"""