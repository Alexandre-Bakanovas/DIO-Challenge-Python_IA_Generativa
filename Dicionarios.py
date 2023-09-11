"""
Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância
do dicionário. Dicionários são delimitados por chaves: {} e contém uma lista de pares chave: valor separada 
por vírgulas.

Exemplo: 
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

Quando já tem o dicionário criado, para incluir valores faz-se:

pessoa["telefone"] = "3333-1234"
"""

"""
Para acessar os valores do dicionário, basta utilizar o nome da chave.
Ex:
print(dados["nome"])
"""

# Dicionários aninhados
# Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja
# um objeto imutável como Strings e números



contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave,valor)


# Métodos de dict
# .clear - Limpa todo o dicionário
# .copy - Tira uma cópia do dicionário, fazendo com que os dicionários não apontem para o mesmo local
# .fromkeys é utilizado para criar chaves. Por padrão, é criado chaves com o valor None.
#     dict.fromkeys(['nome', 'telefone']) #{'nome': None, 'telefone': None}
#     dict.fromkeys(['nome', 'telefone'], 'vazio') # {'nome': 'vazio', 'telefone': 'vazio'}
# .get é utilizado quando não se sabe se existe ou não a chave. sua sintaxe é:
#     get("chave", {valor padrão caso não encontre a chave})
# .items() retorna uma lista de tuplas
# .keys retorna quais são as chaves presentes no dicionários
# .pop remove uma chave do dicionário. Quando não houver, pode colocar um valor padrão para aparecer
# .pop("chave", {valor caso não apareça})
# .popitem
# .setdefault('chave', valor que deseja passar)
# .update é utilizado para atualizar os valores do dicionário
# .values retorna todos os valores das chaves

# resultado = 'telefone' in contatos['melaine@gmail.com']
# print(resultado) #jeito para verificar se há um valor dentro do dicionário para a chave especificada

# del contatos['guilherme@gmail.com']['telefone'] #Assim fará a deleção o valor de telefone da chave guilherme@gmail.com