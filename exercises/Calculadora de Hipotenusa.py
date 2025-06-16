import math
import time
start = time.time()
A = float(input("Digite o Valor de A: "))
B = float(input("Digite o Valor de B: "))
hipo = math.sqrt(math.pow(A,2)+math.pow(B,2))
print (hipo)
finish = time.time ()
print("Tempo de execução: {:.2f} segundos".format(finish-start))