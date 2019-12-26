"""
Pep8 são propostas de melhorias para a linguagem Python.

The Zen of Python.

import this

A ideia da PEP8 é para que possamos escrever códigos Python de forma Pythonica.

1) Utilize Camel Case para nomes de classes:

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

2) Utilize nomes minúsculos e separados por underlines para funções e variáveis:

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

3) Utilize 4 espaços para identação! (Não use tab se você não souber quantos espaços ele consome, essa dica serve para quem trabalha em máquinas com configurações diferentes)

if 'a' in 'banana':
    print('tem')

4) Linhas em branco
    - Separar funções e definições de classe com duas linhas em branco.
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco.

5) Imports
    - Imports devem ser feitos em linhas separadas

# Import Errado:
import sys, os

# Import Certo:
import sys
import os

# Não há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

6) Espaços em expressões e instruções

# 6.1 Não Faça
funcao( algo[ 1 ], { outro: 2 } )

# 6.1 Faça
funcao(algo[1], {outro: 2})

# 6.2 Não Faça
algo (1)

# 6.2 Faça
algo(1)

# 6.3 Não Faça
dict ['chave] = lista [indice]

# 6.3 Faça
dict['chave'] = lista[indice]

# 6.4 Não Faça
x        = 1
a        = 2
variavel = 3

# 6.4 Faça
x = 1
a = 2
variavel = 3

7) Termine sempre uma instrução com uma nova linha
"""
