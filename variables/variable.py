"""

Um nome de variável deve começar com uma letra ou o caractere de sublinhado.
O nome de uma variável não pode começar com um número.
Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (A-z, 0-9 e _).
Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas (idade, idade e IDADE são três variáveis ​​diferentes).

"""

x = 5
y = "John"
print(x)
print(y)


"""
Nomes de variáveis com várias palavras
Nomes de variáveis com mais de uma palavra podem ser difíceis de ler.
Existem várias técnicas que você pode usar para torná-los mais legíveis:
"""

# Camel Case - Cada palavra, exceto a primeira, começa com uma letra maiúscula:

myVariableName = "John"

# Pascal Case - Cada palavra começa com uma letra maiúscula:

MyVariableName = "John"

# Snake Case - Cada palavra é separada por um caractere de sublinhado:

my_variable_name = "John"



# Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

# Você pode obter o tipo de dados de uma variável com a função type ().

print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)


def myfunc():
    print("Python is " + x)

myfunc()