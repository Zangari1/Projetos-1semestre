# Cadastro de Infração
placa = input("Informe a placa do veículo: ")
nome = input("Nome Completo do Motorista: ")
velocidade = float(input("Informe a velocidade registrada do veículo (Km/hr): "))
velocidade_maxima = float(input("Informe a velocidade máxima permitida na via (Km/hr): "))
multa = input("O motorista já foi multado anteriormente? (Sim/Não): ")
pagamento = input("Deseja pagar a multa agora? (Sim/Não): ")

# Verifica se está formatado corretamente
if multa == "Sim" or multa == "Não":
    print("O motorista já foi multado anteriormente? (Sim/Não):", multa)
    if pagamento == "Sim" or pagamento == "Não":
        print("Deseja pagar a multa agora? (Sim/Não):", pagamento)

    # Calcula a diferença entre a velocidade registrada e a máxima permitida na via.
        def calcular_velocidade (velocidade,velocidade_maxima):
            return  velocidade - velocidade_maxima
    # Calcula o percentual de excesso de velocidade.    
        def calcular_percentual (diferenca, velocidade_maxima):
            return (diferenca / velocidade_maxima) * 100
    
    # Valores das multas
        multa_gravissima = 880.41
        multa_grave = 195.23
        multa_leve = 130.16

    # Exibição dos dados da multa
        print("---------Dados da Multa---------")
        print("Placa do veículo:", placa)
        print("Motorista:", nome)
        print("A velocidade registrada foi de:", velocidade, "km/h")
        print("A velocidade máxima permitida foi de:", velocidade_maxima, "km/h")

    #atribuição das funções para as variáveis
        diferenca = calcular_velocidade(velocidade, velocidade_maxima)
        percentual = calcular_percentual(diferenca, velocidade_maxima)

    # Função para calcular, classificar e exibir a multa
        def main(diferenca, percentual, multa, multa_leve, pagamento, multa_grave, multa_gravissima):
        # Sem multa
            if diferenca <= 0:
                print("Nenhuma infração cometida.")
                return

            valor_multa = 0  # Variável para exibir o valor da multa

        # Multa leve
            if percentual <= 20:
                print("Infração leve - Multa de R$", multa_leve)
                valor_multa = multa_leve

        # Multa grave
            elif 20 < percentual < 50:
                print("Infração grave - Multa de R$", multa_grave, "5 pontos na CNH.")
                valor_multa = multa_grave

        # Multa gravíssima
            elif percentual > 50:
                print("Infração gravíssima - Multa de R$", multa_gravissima, "7 pontos na CNH e suspensão da carteira.")
                print("Atenção: CNH suspensa! Compareça ao Detran.")
                print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
                valor_multa = multa_gravissima

        # Verificação de reincidência
            if multa == "Sim":
                valor_multa *= 2
                print("Atenção: Multa DOBRADA por reincidência!")

        # Cálculo do desconto aplicado
            if pagamento == "Sim":
                valor_final = valor_multa * 0.8
                print(f"Você recebeu um desconto de 20%. Valor final: R$ {valor_final:.2f}")
            else:
                print(f"Valor total da multa: R$ {valor_multa:.2f}")

    # Chamando a função
        main(diferenca, percentual, multa, multa_leve, pagamento, multa_grave, multa_gravissima)

    else:
        print("Erro: Responda apenas com 'Sim' ou 'Não'.")
else:
    print("Erro: Responda apenas com 'Sim' ou 'Não'.")
