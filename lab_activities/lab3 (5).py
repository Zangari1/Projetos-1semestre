import random
import math
import string

def g_s(tm=6):
    c = string.ascii_letters + string.digits + "!@#$%^&*"
    s = ''.join(random.choice(c) for _ in range(tm))
    return s

s_a = g_s ()
print("Senha gerada: ", s_a)