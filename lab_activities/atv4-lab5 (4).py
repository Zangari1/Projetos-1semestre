codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    print("Alimento não-perecível")
elif 2<codigo<4:
    print("Alimento perecível")
elif 5<codigo<=6:
    print("Vestuário")
elif codigo == 7:
    print("Higiene pessoal")
elif 8<codigo<=10:
    print("Utensílios domésticos")
else:
    print("Categoria Inválida")