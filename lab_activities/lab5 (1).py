def verificar_resgate(valor_inicial, taxa_anual, dias, prazo_minimo):
    taxa_diaria = (1 + taxa_anual) ** (1 / 365) - 1

    rendimento_final = valor_inicial * (1 + taxa_diaria) ** dias

    if dias < prazo_minimo:
        valor_com_penalidade = valor_inicial * 0.95
        rendimento_antecipado = valor_com_penalidade * (1 + taxa_diaria) ** dias

        print("Resgate antecipado! Aplicada penaidade sobre o valor investido.")
        print("O rendimento com a penalidade foi de:", rendimento_antecipado)
    else:
        rendimento_antecipado = rendimento_final  
        print("O rendimento foi de:", rendimento_final)


    if rendimento_antecipado > rendimento_final:
        print("Compensa resgatar antecipadamente.")
    else:
        print("Compensa esperar até o vencimento.")


valor_inicial = float(input("Digite o valor investido: "))
taxa_anual = float(input("Digite a taxa de rentabilidade ao ano (%): ")) / 100 
dias = int(input("Digite a quantidade de dias investidos: "))
prazo_minimo = int(input("Digite o prazo mínimo em dias: "))


verificar_resgate(valor_inicial, taxa_anual, dias, prazo_minimo)
