def comparar_cdb_poupanca(dias, valor):
    valorcdb = valor*(1 + (110/100) * (dias/252))
    if selic > 0.085: 
        poupanca = (1 + 0.005) ** (1/30) - 1  
        valorpoupanca = valor * ((1 + poupanca) ** dias)
    else:  
        selic = (1 + (0.7 * selic) / 252) - 1
        valorpoupanca = valor * ((1 + selic) ** dias)
    
    if valorcdb > valorpoupanca:
        print("O CDB foi a melhor opção.")
    elif valorpoupanca > valorcdb:
        print("A Poupança foi a melhor opção.")
    else: 
        print("Ambos os investimentos tiveram o mesmo retorno.")

selic = float(input("Digite a taxa anual da Selic (%): "))
valor = float(input("Valor a ser investido: "))
dias = int(input("Tempo de investimento (dias): "))

if dias < 30:
    print("A poupança não terá rendimento, pois exige aniversário mensal.")




