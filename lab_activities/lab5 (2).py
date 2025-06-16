def calcular_cdi (valor_investido, percentual_cdi, dias):
    return  valor_investido*(1 + (percentual_cdi/100) * (dias/252))

valor_investido = float(input("Valor a ser investido: "))
percentual_cdi = float(input("Percentual do CDI (%): "))
dias = int(input("Tempo de investimento (dias): "))

resultado = calcular_cdi (valor_investido, percentual_cdi, dias)

print("O valor será de: R$", resultado)

if valor_investido <= 10000:
    print("Você pode conseguir taxas melhores em investimentos privados!")
