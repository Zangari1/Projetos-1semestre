p = int(input("Digite o preço do produto: "))
n = [100, 50, 20, 10, 5, 2, 1]
qn = {}

for nota in n:
    quantidade = p // nota
    if quantidade > 0:
        qn[nota] = quantidade
    p %= nota

print("Menor quantidade de notas necessárias para o pagamento:")
for nota, quantidade in qn.items():
    print("Notas de R$",nota,":",quantidade)