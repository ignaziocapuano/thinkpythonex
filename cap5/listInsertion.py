#funzione per l'inserimento di una lista, con parametri il tipo e il carattere terminatore

def listInsertion(type, terminal_char):
    list = []
    if type=="int":
        num = input("Inserisci primo elemento della List: ")
        while num != terminal_char:
            list.append(int(num))
            print("Inserisci numero da aggiungere alla List(", terminal_char, " per interrompere): ")
            num = input()
    elif type=="str":
        string = input("Inserisci primo elemento della List: ")
        while string != terminal_char:
            list.append(string)
            if terminal_char== "":
                terminal_str= "''"
            print("Inserisci numero da aggiungere alla List(" + terminal_str + " per interrompere): ")
            string = input()
    return list