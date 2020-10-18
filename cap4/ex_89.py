#da intero a ordinale (letterale primo secondo ecc..)

def int_to_Ordinale(n):
    if n==1:
        return "Primo"
    elif n==2:
        return "Secondo"
    elif n==3:
        return "terzo"
    elif n==4:
        return "Quarto"
    elif n==5:
        return "Quinto"
    elif n==6:
        return "Sesto"
    elif n==7:
        return "Settimo"
    elif n==8:
        return "Ottavo"
    elif n==9:
        return "Nono"
    elif n==10:
        return "Decimo"
    elif n==11:
        return "Undicesimo"
    elif n==12:
        return "dodicesimo"
    else:
        return ""

def main():
    RANGE=12
    for i in range(1,RANGE+1):
        print(int_to_Ordinale(i))

if __name__ == "__main__":
    main()

