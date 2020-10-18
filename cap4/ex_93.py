#centra stringa

def centraStringhe(s,w):
    if len(s)>=w:
        return s
    if len(s)<w:
        spazi=""
        nspazi=(w-len(s))//2
        for i in range(nspazi):
            spazi+=" "
        return (spazi+s)

def main():
    str=input("Inserisci stringa da centrare: ")
    LARGHEZZA_FINESTRA_IN_CARATTERI=100
    print(centraStringhe(str,LARGHEZZA_FINESTRA_IN_CARATTERI))

main()