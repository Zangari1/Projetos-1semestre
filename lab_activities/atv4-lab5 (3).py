p = [
    "Telefonou para a vítima?", 
    "Esteve no local do crime?", 
    "Mora perto da vítima?",
    "Devia para a vítima?" ,
    "Já trabalhou com a vítima?",
] 

rs = 0

for pgt in p:
    r = input(pgt + " (sim/não): ").strip().lower()
    if r == "sim":
        rs += 1

if rs == 2:
    print("Suspeito")
elif 3<= rs <= 4:
    print("Cúmplice")
elif rs == 5:
    print("Assassino")
else:
    print("Inocente")

    

