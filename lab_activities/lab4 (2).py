sal = int(input("Digite o valor so seu salário atual: "))
temp = int(input("Digite a quantos meses você está na empresa: "))
bonus5 = (sal*0.2)
bonusmnr5 = (sal*0.1)
salatt5 = (bonus5 + sal)
salattmnr5 = (bonusmnr5 + sal)

if temp>=60 :
    print("O seu salário atual será de: ", salatt5, "Você recebeu um bonus de: ", bonus5, "R$")
else:
    print("O seu salário atual será de: ", salattmnr5, "Você recebeu um bonus de: ", bonusmnr5)
