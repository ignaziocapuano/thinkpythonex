#media


count=0
media=0
while True:
    x = int(input("Inserisci serie di numeri(0 per terminare)"))
    if x==0:
        break
    count+=1
    media=(media+x)/count


print("La media dei valori digitati è :",media)
