num = int(input("Digite um número: "))
soma = 0
par = 0
impar = 0
while num>0:
    digito = num % 10
    soma+=digito
    if digito % 2 == 0:
        par += 1
    else:
        impar += 1
    num //= 10
print("A soma de todos os dígitos do número é: ", soma)
print("dígitos pares: ", par)
print("dígitos ímpares: ", impar)