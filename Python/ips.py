#class ip

def main():
    ip="192.168.100.0"
    mask = 24 #/24
    ipBinario = ""
    ipBroadcast = ""
    for gruppo in ip.split("."):
        x=bin(int(gruppo))[2:].zfill(8)
        ipBinario = ipBinario + x
    print(f"Indirizzo ip di rete in binario: {ipBinario}")
    ipBroadcastBinario = ipBinario[:mask] + "1"*(32-mask) #32-mask = host's bits
    print(f"Indirizzo ip di broadcast in binario: {ipBroadcastBinario}")
    for i in range(0,32,8):
        gruppo = ipBroadcastBinario[i:i+8]
        ipBroadcast = ipBroadcast + str(int(gruppo,2))+"."
    ipBroadcast = ipBroadcast[:-1]
    print(f"Indirizzo ip di broadcast in decimale: {ipBroadcast}")

if __name__ == "__main__":
    main()