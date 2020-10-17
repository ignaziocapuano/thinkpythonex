#note musicali
notastr=input("Scrivi una nota musicale in formato inglese con l'ottava (es C4)")

if notastr[0]=="C":
    notaf=261.63
elif notastr[0]=="D":
    notaf=293.66
elif notastr[0]=="E":
    notaf=329.63
elif notastr[0]=="F":
    notaf=349.23
elif notastr[0]=="G":
    notaf=392.00
elif notastr[0]=="A":
    notaf=440.00
elif notastr[0]=="B":
    notaf=493.88

ottava=int(notastr[1])
notaf=notaf/(2**(4-ottava))

print("La frequenza della nota scelta è",notaf)