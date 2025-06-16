# Listas para armazenar os dados dos exercícios
exc = []           # Nomes dos exercícios realizados
temp = []          # Tempo gasto em minutos
call = []          # Calorias queimadas
dias = []          # Dia da semana em que o exercício foi realizado
meta_semanal = []  # Meta semanal de calorias

# Lista de frases motivacionais
frases = [
    "Você está cada vez mais perto do seu objetivo!",
    "Não pare agora, o progresso é constante!",
    "Cada treino é uma vitória!",
    "A consistência vence a motivação!",
    "Seu esforço vale a pena!"
]

# Função para cadastro de exercícios
def cadastro():
    print("------------------------------")
    print("     Cadatro de Exercícios    ")
    print("------------------------------")
    # Entrada de dados do usuário
    nome = str(input("Exercício realizado: "))
    tempo = int(input("Tempo gasto (minutos): "))
    calorias = int(input("Calorias gastas no dia: "))
    dia = str(input("Dia da semana: "))
    # Armazenamento nas listas correspondentes
    exc.append(nome)
    temp.append(tempo)
    call.append(calorias)
    dias.append(dia)

# Função para gerar relatório de um dia específico
def relatorio():
    drel = str(input("Deseja o relatório de qual dia da semana? "))
    temptt = 0    # Soma do tempo total
    calltt = 0    # Soma das calorias totais
    validacao = False  # Verifica se encontrou exercícios no dia informado

    for i in range(len(exc)):
        if drel == dias[i]:
            print("- " + exc[i] + ": " + str(temp[i]) + " min, " + str(call[i]) + " cal")
            temptt += temp[i]
            calltt += call[i]
            validacao = True

    # Exibe os totais ou mensagem de ausência
    if validacao:
        print(f"Tempo total: {temptt} min")
        print(f"Calorias totais: {calltt} cal")
    else:
        print("Nenhum exercício registrado para esse dia.")

# Função para cálculo do IMC
def imc():
    peso = float(input("Informe seu peso (kg): "))
    altura = float(input("Informe sua altura (m): "))
    calculo = peso / (altura * altura)

    # Classificação do IMC
    if calculo <= 18.5:
        print(f"Baixo Peso! IMC: {calculo:.2f}")
    elif 18.5 < calculo <= 24.9:
        print(f"Peso Normal! IMC: {calculo:.2f}")
    elif 24.9 < calculo <= 30:
        print(f"Excesso de Peso! IMC: {calculo:.2f}")
    elif 30 < calculo <= 35:
        print(f"Obesidade! IMC: {calculo:.2f}")
    elif calculo > 35:
        print(f"Obesidade Extrema! IMC: {calculo:.2f}")

# Função para definir ou verificar a meta semanal de calorias
def meta():
    total_calorias = 0
    for cal in call:
        total_calorias += cal

    # Caso ainda não exista uma meta
    if len(meta_semanal) == 0:
        print("Nenhuma meta definida ainda.")
        nvmeta = int(input("Informe uma meta semanal de calorias: "))
        meta_semanal.append(nvmeta)          
        print(f"Meta semanal de calorias: {nvmeta} cal.")

    else:
        # Exibe meta atual e progresso
        print(f"Meta semanal atual: {meta_semanal[0]} cal")
        print(f"Calorias queimadas até agora: {total_calorias} cal")

        if total_calorias >= meta_semanal[0]:
            print("Parabéns! Você atingiu sua meta!")
        else:
            print(f"Ainda faltam {meta_semanal[0] - total_calorias} cal para atingi-la.")

        # Permite alterar a meta
        altmeta = input("Deseja alterar a meta? (s/n): ")
        if altmeta == "s" or altmeta == "S":
            nvmeta = int(input("Digite a nova meta semanal de calorias: "))
            meta_semanal[0] = nvmeta
            print(f"Nova meta de calorias: {nvmeta} cal.")

# Função para mostrar uma frase motivacional por vez
def frasemot(fraseatual):
    print(frases[fraseatual])
    proxfrase = fraseatual + 1
    if proxfrase == len(frases):
        proxfrase = 0
    return proxfrase

# Função para calcular a média de calorias por exercício
def media():
    if len(exc) == 0:
        print("Nenhum exercício registrado.")
        return

    print("Média de calorias por exercício:")

    nomes_unicos = []
    # Coleta nomes únicos de exercícios
    for nome in exc:
        if nome not in nomes_unicos:
            nomes_unicos.append(nome)

    # Calcula média para cada exercício
    for nome in nomes_unicos:
        calltotal = 0
        quantidade = 0
        for i in range(len(exc)):
            if exc[i] == nome:
                calltotal += call[i]
                quantidade += 1
        media = calltotal / quantidade
        print(f"- {nome}: {media:.2f} cal")

# Função para gráfico de barras
def grafico():
    print("------------------------------")
    print(" Gráfico de Calorias Queimadas ")
    print("------------------------------")
    if not exc: 
        print("Nenhum exercício cadastrado para exibir o gráfico.")
        return

    print("Representação visual (cada '#' representa aprox. 10 calorias):")
    
    for i in range(len(exc)): 
        nome_exercicio = exc[i] 
        calorias_exercicio = call[i] 
        
        num_hashes = calorias_exercicio // 10 
        
        barra_grafico = ""
        for _ in range(num_hashes): # Loop para construir a barra
            barra_grafico += "#"
        
        print(f"{nome_exercicio}: {barra_grafico} ({calorias_exercicio} cal)")
    print("--- Fim do Gráfico ---")


# Função principal com menu de opções
def menu():
    sair = False
    fraseatual = 0
    while sair == False:
        print("------------------------------")
        print("              MENU            ")
        print("------------------------------")
        print("1 - Cadastro de Exercícios")
        print("2 - Relatório Diário")
        print("3 - Calcular IMC")
        print("4 - Meta Semanal")
        print("5 - Frases Motivacionais")
        print("6 - Média de Calorias")
        print("7 - Gráfico de Calorias")
        print("0 - Sair")

        opcao = int(input("Digite uma opção: "))
        # Direciona para a função escolhida
        if opcao == 1:
            cadastro()
        elif opcao == 2:
            relatorio()
        elif opcao == 3:
            imc()
        elif opcao == 4:
            meta()
        elif opcao == 5:
           fraseatual = frasemot(fraseatual)
        elif opcao == 6:
            media()
        elif opcao == 7:
            grafico()
        elif opcao == 0:
            sair = True
        else:
            print("Opção Inválida! Digite uma opção válida!")

# Chamada da função principal
menu()
