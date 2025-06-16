nte = int(input("Digite o número total de eleitores: "))
nvp = int(input("Quantidade de votos do primeiro candidato: "))
nvs = int(input("Quantidade de voto do segundo candidato: "))
pvp = (nvp*nte)/100
svp = (nvs*nte)/100
vtn = nte-(nvp+nvs)
print("Primeiro candidato: ", pvp, "%", "Segundo candidato: ", svp, "%", " Votos Nulos: ", vtn, "%")