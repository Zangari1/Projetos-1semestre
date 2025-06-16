peso = float(input("Digite o peso dos peixes em kg : "))
excesso = (peso-50)
def calcular(excesso):
    return (excesso*4)

resultado = calcular(excesso)

if peso<=50:
    print("Dentro do regulamento")
else:
    print("Fora do regulamento, o peso excedeu em: ", excesso, "Kg, e você deverá pagar uma multa de: ", resultado, "R$" )
