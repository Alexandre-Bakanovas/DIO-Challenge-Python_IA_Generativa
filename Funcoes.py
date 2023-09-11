"""
Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros
podem ou não ter valores padrões. Usar funções tornaa o código mais legível e possibilita o reaproveitamento
de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada

Para retornar um valor, utilizamos a palavra reservada return. Toda Função python retorna None por padrão.
Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

Args e Kwargs
Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs),
o método recebe os valores como tupla e dicionário, respectivamente.

Para fazer o preenchimento dos argumentos da posição serem feitos aapenas por posição, deve-se
utilizar a /. Exemplo:
    def criar_carro(modelo, ano, placa, /, marca, motor, combustivel)
    No exemplo acima, tudo o que vem ATÉ a barra, deve ser passado por posição. O que vem depois, pode
    ser colocado por posição ou nomeado.

PAra fazer o preenchimento dos arumentos apenas pelo nome, deve-se utilizar o "*". Exemplo:
    def criaar_carro(*, modelo, ano, placa, marca, motor, combustivel)
    Tudo o que vem depois do *, deve ser obrigatoriamente preenchido utilizando o nome do argumento
    
Para fazer de forma híbrida, basta utilizar ambos os caracteres "/ e *", lembrando que para o de posição
é os argumentos ATÉ a barra, e o de nome é TODOS depois do asterisco.


Objetos de primeira classe:
Em python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe.
Com isso, podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores
em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para um função
(closures).

"""

# Exemplos:

def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Seja bem vindo {nome}!')

def exibir_mensagem_3(nome='Anônimo'): #Aqui estamos atribuindo um valor já para a função, ou seja
    # no final ele torna-se opcional
    print(f'Seja bem vindo {nome}!')

exibir_mensagem()
exibir_mensagem_2('Chappie')
exibir_mensagem_2(nome='Guilherme')
exibir_mensagem_3()
exibir_mensagem_3(nome='Chappie')

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))


def func_3():
    print('Olá mundo!') #Como ela não retorna nada, deve retornar None.

print(func_3())


# Exemplo de objeto de primeira classe
def somar(c, d):
    return c + d

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

exibir_resultado(10, 10, somar)

