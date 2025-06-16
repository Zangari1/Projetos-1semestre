c = 0
s = 0
a = 0
contint = 0
intervalo = int(input("Quantos intervalos de tempo serão monitorados? "))
while contint<intervalo:
    valorint = int(input("Digite a porcentagem (0 - 100) do uso do dispositivo: "))
    s += valorint
    media = s/intervalo
    if valorint>80:
        a += 1
    if c<valorint:
        c = valorint
    else:
        c = c
    contint +=1
print("Uso Médio: ", media, "%")
print("Pico de Uso: ", c, "%")
print("O uso passou de 80% ", a," Vezes")

