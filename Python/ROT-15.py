def cript(cod):
    fin=""
    for k in range(len(cod)):
        if(ord(cod[k])+15>ord('z')):
            fin+=chr(96+(ord(cod[k])+15-ord('z')))
        else:
            fin+=chr(ord(cod[k])+15)
    return fin

def decript(cod):
    fin=""
    for k in range(len(cod)):
        if(ord(cod[k])-15<ord('a')):
            fin+=chr(123-(ord('a')-(ord(cod[k])-15)))
        else:
            fin+=chr(ord(cod[k])-15)
    return fin

print(cript("ciao"))