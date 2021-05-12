#udp non è affidabile

import socket as sck
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

while True:
    frase=input("inserisci: ")
    f=frase.encode()
    s.sendto(f,('127.0.0.1',1123))

s.close()