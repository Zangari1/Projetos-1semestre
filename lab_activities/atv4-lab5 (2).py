p = float(input("Peso(kg): "))
v = float(input("Volume(m³): "))
d = float(input("Distância(Km): "))

if p<5 and v<0.03:
    veiculo = "moto"
    print("Quantidade de Litros: ", d*0.05, "Veiculo: ", veiculo)
elif p>=5 and p<=30 and v<0.03 and v<=0.15:
    veiculo = "Van"
    print("Quantidade de Litros: ", d*0.12, "Veiculo: ", veiculo)
else:
    veiculo = "Caminhão"
    print("Quantidade de Litros: ", d*0.3, "Veiculo: ", veiculo)
