p = float(input("Peso(kg): "))
v = float(input("Volume(m³): "))
d = float(input("Distância(Km): "))
diesel = 5.98
gasolina = 6.33

def calcular (diesel, d, gasolina):
    valor_caminhão = (d*0.03)*diesel
    valor_moto = (d*0.05)*gasolina
    valor_van = (d*0.12)*gasolina
    return valor_caminhão, valor_moto, valor_van

valor_caminhão, valor_moto, valor_van = calcular (diesel, d, gasolina)
    
if p<5 and v<0.03:
    veiculo = "moto"
    consumo = d*0.05
    frete = valor_moto
elif p>=5 and p<=30 and v>=0.03 and v<=0.15:
    veiculo = "Van"
    consumo = d*0.05
    frete = valor_van
else:
    veiculo = "Caminhão"
    consumo = d*0.3
    frete = valor_caminhão

print("Quantidade de Litros: ", consumo)
print("Veículo: ", veiculo)
print("Frete R$: ", frete)

