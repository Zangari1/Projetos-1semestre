import time
start = time.time()
cf =  float(input("Digite o custo de fábrica: "))
vc = (cf*0.45) + (cf*0.28) + cf
print("O valor do carro é: {:.2f}".format(vc))
finish = time.time ()
print("Tempo de execução: {:.2f} segundos".format(finish-start))