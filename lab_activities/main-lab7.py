def inverter(numeros):
    tamanho = len(numeros)
    for i in range(tamanho // 2):
        numero_guardado = numeros[i]
        numeros[i] = numeros[tamanho - 1 - i]
        numeros[tamanho - 1 - i] = numero_guardado
    return numeros

minha_lista = []

for i in range(10):
    valor = int(input(f"Digite o {i + 1}º número: "))
   
    if valor not in minha_lista:
        minha_lista.append(valor)


inverter(minha_lista)

print("Lista invertida:", minha_lista)
