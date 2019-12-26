"""
Tipo Float

Tipo real, decimal

Casas decimais

Obs: os separadores de casas decimais na programação é o ponto e não a vírgula
"""

# Errado
valor = 1, 44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
