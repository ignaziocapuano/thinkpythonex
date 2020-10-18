#precedenza degli operatori

def precedence(op):
    if len(op)==1:
        if op=="+"  or op=="-":
            return 1
        elif op=="*" or op=="/":
            return 2
        elif op=="^":
            return 3
        else:
            return -1
    else:
        return -1

def main():
    operatore=input("Inserisci operatore per scoprire il suo grado di precedenza tra + - / * ^: ")
    print("Precedenza=",precedence(operatore))

if __name__ == '__main__':
    main()