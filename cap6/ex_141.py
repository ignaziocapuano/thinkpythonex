#Write out Numbers in English

numbers={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
decine={1:"",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
eccezioni={10:"ten",11:"eleven",12:"twelve"}
decine2={3:"thir",5:"fif"}
centinaia_postfix= "hundred"
decina_postfix="teen"

check=int(input("Inserisci numero tra 0 e 999"))
check_str=str(check)
if check not in range(1000):
    print("cifra non valida")
    quit()
if len(check_str)==1:
    print(numbers[check])
elif len(check_str)==2:
    if 10<=check<=12:
        print(eccezioni[check])
    elif 12<check<20:
        if check_str[1]=="3" or check_str[1]=="5":
            print(decine2[int(check_str[1])]+decina_postfix)
        else:
            print(numbers[int(check_str[1])]+decina_postfix)
    elif check>19:
        if check_str[1]=="0":
            print(decine[int(check_str[0])])
        else:
            print(decine[int(check_str[0])]+numbers[int(check_str[1])])
elif len(check_str)==3:
    if check_str[1]=="0" and check_str[2]=="0":
        print(numbers[int(check_str[0])] + " "+centinaia_postfix)
    if check_str[1]=="0" and check_str[2]!="0":
        print(numbers[int(check_str[0])] + " " + centinaia_postfix+" and "+numbers[int(check_str[2])])
    if check_str[1] != "0":
        ultime_cifre=int(check_str[1]+check_str[2])
        print(numbers[int(check_str[0])] + " " + centinaia_postfix + " and ",end="")
        if 10 <= ultime_cifre <= 12:
            print(eccezioni[ultime_cifre])
        elif 12 < ultime_cifre < 20:
            if check_str[2] == "3" or check_str[2] == "5":
                print(decine2[int(check_str[2])] + decina_postfix)
            else:
                print(numbers[int(check_str[2])] + decina_postfix)
        elif ultime_cifre > 19:
            if check_str[2] == "0":
                print(decine[int(check_str[1])])
            else:
                print(decine[int(check_str[1])] + numbers[int(check_str[2])])