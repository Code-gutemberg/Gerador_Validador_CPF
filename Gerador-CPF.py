from funcao import gerador_cpf
from funcao import validador_cpf
from random import randint

numero = str(randint(10000000000, 99999999999))
gerador_cpf(numero)     
validador_cpf(gerador_cpf(numero))