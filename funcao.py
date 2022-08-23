def gerador_cpf(cpf):
    cpf_teste01 = cpf[:-2]
    range_01 = 11
    acumulador_01 = 0
    
    for x in cpf_teste01:
        range_01 -= 1
        resultado_01 = int(x) * range_01
        acumulador_01 += resultado_01
        
    formula_01 = 11 - (acumulador_01 % 11)
    
    if formula_01 <= 9:
        digito_1 = formula_01
    else: 
        digito_1 = 0
    
    cpf_teste02 = cpf_teste01 + str(digito_1)
    range_02 = 12
    acumulador_02 = 0
    
    for y in cpf_teste02:
        range_02 -= 1
        resultado_02 = int(y)*range_02
        acumulador_02 += resultado_02
        
    formula_02 = 11 - (acumulador_02 % 11)
    
    if formula_02 <= 9:
        digito_2 = formula_02
    else: 
        digito_2 = 0
        
    cpf_valido = cpf_teste02 + str(digito_2)
    return cpf_valido


def validador_cpf(cpf):
    cpf_teste01 = cpf[:-2]
    range_01 = 11
    acumulador_01 = 0
    
    for x in cpf_teste01:
        range_01 -= 1
        resultado_01 = int(x) * range_01
        acumulador_01 += resultado_01
        
    formula_01 = 11 - (acumulador_01 % 11)
    
    if formula_01 <= 9:
        digito_1 = formula_01
    else: 
        digito_1 = 0
    
    cpf_teste02 = cpf_teste01 + str(digito_1)
    range_02 = 12
    acumulador_02 = 0
    
    for y in cpf_teste02:
        range_02 -= 1
        resultado_02 = int(y)*range_02
        acumulador_02 += resultado_02
        
    formula_02 = 11 - (acumulador_02 % 11)
    
    if formula_02 <= 9:
        digito_2 = formula_02
    else: 
        digito_2 = 0
        
    cpf_valido = cpf_teste02 + str(digito_2)
    if cpf == cpf_valido and cpf != str(cpf[0]) * 11:
        print('O CPF foi VALIDADO COM SUCESSO!')
        print(cpf_valido)
    else:
        print('O CPF é INVALIDO')
