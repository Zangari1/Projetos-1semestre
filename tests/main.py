v = float(input("Digite o valor total da compra: "))
ced = 0
while ced<v:
    c = int(input("Digite o valor da nota de dinheiro: "))
    ced = ced + c
    troco = ced-v
    vr = v-ced
    if v>ced:
        print("O valor restante a ser pago é de: ", vr)
print("Pagamento confirmado.")
if v<ced:
    print("O valor do troco é de: ", troco)
else:
    print("Obrigado por comprar conosco!")

    
    