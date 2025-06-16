def intersecao(listaA, listaB):
    resultado = []

    for i in range(len(listaA)):
        for j in range(len(listaB)):
            if listaA[i] == listaB[j]:
                repetido = False
                for k in range(len(resultado)):
                    if resultado[k] == listaA[i]:
                        repetido = True
                        break
                if not repetido:
                    resultado.append(listaA[i])
    
    return resultado

tamanhoA = int(input("Quantos números você quer na lista A? "))
listaA = []

for i in range(tamanhoA):
    num = int(input(f"{i + 1}º número de A: "))
    listaA.append(num)

tamanhoB = int(input("Quantos números você quer na lista B? "))
listaB = []

for i in range(tamanhoB):
    num = int(input(f"{i + 1}º número de B: "))
    listaB.append(num)

resultado = intersecao(listaA, listaB)
print("Interseção entre A e B:", resultado)
