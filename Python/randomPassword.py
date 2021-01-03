import random
import string

while True:    
    opz=int(input())
    if(opz==0 or opz==1):
        break

password=''

if(opz==0):
    for k in range(8):
        password+=random.choice(string.ascii_letters + string.digits)

if(opz==1):
    for k in range(20):
        password+=random.choice(string.printable)

print(password)
