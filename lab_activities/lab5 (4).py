def calcular_ir (lucro, dias):
    lucro = valor_final - valor_inicial
    if dias <=180:
        ir = 0.225
    elif 181 <= dias <=360:
        ir = 0.2
    elif 361 <= dias <= 720:
        ir = 0.175
    else: 
        ir = 0.15
    
    return lucro*ir

valor_inicial = float(input("Digite o valor inicial do investimento: "))
valor_final = float(input("Digite o valor final após o período do investimento: "))
dias = int(input("Digite o período do investimento (dias): "))

lucro = valor_final - valor_inicial

valor_ir = calcular_ir (lucro, dias)
print("Imposto de Renda devido: R$", valor_ir)

