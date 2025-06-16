import time
import math
start = time.time()
tam = int(input("Quantos metros quadrados serão pintados? "))
latas = math.ceil((tam/3)/18)
print("Terá de comprar ", math.ceil(latas) , "latas de tinta e custará ", (latas*120), " R$" )
finish = time.time ()
print("Tempo de execução: {:.2f} segundos".format(finish-start))

