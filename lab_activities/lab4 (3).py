av1 = float(input("Digite a nota da primeira avaliação: "))
av2 = float(input("Digite a nota da segunda avaliação: "))
av3 = float(input("Digite a nota de terceira avalição: "))
peso1 = (av1*2)
peso2 = (av2*3)
peso3 = (av3*5)

def calcular(peso1, peso2, peso3): 
    return ((peso1 + peso2 + peso3)/3)
resultado = calcular(peso1, peso2, peso3)

if resultado>=6 :
    print("Você foi aprovado!, sua nota foi: ", resultado)
else:
    print("Você foi reprovado!, sua nota foi de: ", resultado)