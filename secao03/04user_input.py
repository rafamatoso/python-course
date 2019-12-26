"""
Recebendo Input do Usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples
- Aspas duplas
- Aspas simples triplas
- Aspas duplas triplas

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
- ...
"""

# Input de Dados
#print("Qual seu nome? ")
# nome = input()  # Input -> Entrada
# Input em uma linha apenas
nome = input("Qual seu nome? ")


#print("Qual a sua idade? ")
#idade = input()
idade = int(input("Qual sua idade? "))

# Processamento

# Saída de Dados
# Exemplo de print antigo versão 2.x python
# print('%s têm %s anos' % (nome, idade))

# Exemplo de print moderno versão 3.x python
# print('{0} têm {1} anos'.format(nome, idade))

# Exemplo de print atual versão => 3.6
print(f'{nome} têm {idade} anos')

"""
# int(idade) => cast

Cast é a "conversão" de um tipo de dado para outro
"""
print(f'{nome} nasceu em {2019 - idade}')
