"""Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos
    ou eliminar itens duplicados de um iterável

    Conjuntos em python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário
    convertes eles para uma lista.
"""
print(f""" Breve exemplos sobre o set e como se utiliza
      """)
exemplo_1 = set([1,2,3,1,3,4])
print(exemplo_1)
lista = list(exemplo_1)
print(lista[0])

exemplo_2 = set('abacaxi')
print(exemplo_2)

exemplo_3 = set(('palio', 'gol', 'celta', 'palio'))
print(exemplo_3)
for carro in exemplo_3:
    print(carro)
for indice, carro in enumerate(exemplo_3):
    print(f'{indice}: {carro}')
print()

print(""" Métodos para utilização junto aos conjuntos:
""")
# Método para união de conjuntos:
print('União de conjuntos:')
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))
print()

# Método para intersecção de conjuntos
print('Método para intersecção de conjuntos:')
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}
print(conjunto_c.intersection(conjunto_d))
print()

# Método para pegar a diferença entre as intersecções
print('Método para a diferença entre as intersecções:')
conjunto_e = {1, 2, 3}
conjunto_f = {2, 3, 4}
print(conjunto_e.difference(conjunto_f)) #Vale ressaltar que, neste caso pegamos o "restante" do conjunto e
print(conjunto_f.difference(conjunto_e)) #Vale ressaltar que, neste caso pegamos o "restante" do conjunto f
print()

# Método para diferença simétrica (diferença simétrica nada mais é do que retornar todos os valores - a intersecção)
print('Método para diferença simétrica:')
conjunto_g = {1, 2, 3}
conjunto_h = {2, 3, 4}
print(conjunto_g.symmetric_difference(conjunto_h))
print()

# .issubset é um método onde retorna True ou False. Para True, todo o conjunto deve estar dentro de outro conjunto_a
print('Método para saber se um conjunto é subset de outro: ')
conjunto_i = {1, 2, 3}
conjunto_j = {4, 1, 2, 5, 6, 3}
print(conjunto_j.issubset(conjunto_i)) #Ele irá testar se o primeiro conjunto passado é subset do segundo conjunto passado
print(conjunto_i.issubset(conjunto_j)) #Ele irá testar se o primeiro conjunto passado é subset do segundo conjunto passado
print()

# .issuperset é um metodo onde retorna True ou False. Para True, o primeiro conjunto deve ter todos os dados do conjunto menor
print('Método para saber se um conjunto é superset de outro: ')
conjunto_k = {1, 2, 3}
conjunto_l = {4, 1, 2, 5, 6, 3}
print(conjunto_k.issuperset(conjunto_l)) # Retorna true quando o primeiro conjunto possui todos os valores do segundo conjunto
print(conjunto_l.issuperset(conjunto_k))
print()

# .isdisjoint é um método onde retorna True quando não há nenhum tipo de intersecção entre os conjuntos.
print('Método para saber se os conjuntos não possuem nenhum tipo de intersecção: ')
conjunto_m = {1, 2, 3, 4, 5}
conjunto_n = {6, 7, 8, 9}
conjunto_o = {1, 0}
print(conjunto_m.isdisjoint(conjunto_n))
print(conjunto_m.isdisjoint(conjunto_o))
print(conjunto_n.isdisjoint(conjunto_m))
print(conjunto_n.isdisjoint(conjunto_o))
print(conjunto_o.isdisjoint(conjunto_m))
print(conjunto_o.isdisjoint(conjunto_n))
print()

# .add adiciona um elemente ao set. Caso já exista esse elemente, ele não fará nada.
# .clear ele limpará o set inteiro
# .copy copia os valores do conjunto
# .discard serve discartar um valor específico passado como argumento
# .pop discarta o PRIMEIRO valor do conjunto
# .remove um número passado como argumento
# .len mostra o tamanho do conjunto
# in para saber se algum elemento está ou não no conjunto
