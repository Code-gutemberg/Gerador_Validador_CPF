from gerador import gerador_cpf
from validador import validador_cpf
from random import randint

print()
print('======== GERADOR DE CPF ========')
# Gerador de Números aleatórios
numero = str(randint(10000000000, 99999999999))
gerador_cpf(numero)

# validador do número gerado na função anterior  
print('=' * 32)   
validador_cpf(gerador_cpf(numero))
print('=' * 32)   