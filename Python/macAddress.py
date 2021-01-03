import random
import string

def genera_mac():
    lista=[]
    for _ in range(6):
        lista.append(random.choice(string.ascii_uppercase + string.digits) + random.choice(string.ascii_uppercase + string.digits))
    return lista

l=genera_mac()
print(':'.join(l))