#banconote

banconota=int(input("Scrivi il valore di una banconota: $"))

if banconota==1:
    immagine="George Washington"
elif banconota==2:
    immagine="Thomas Jefferson"
elif banconota==5:
    immagine="Abraham Lincoln"
elif banconota==10:
    immagine="Alexander Hamilton"
elif banconota==20:
    immagine="Andrew Jackson"
elif banconota==50:
    immagine="Ulysses S.Grant"
elif banconota==100:
    immagine="Benjamin Franklin"
else:
    immagine=""

if immagine!="":
    print("Sulla banconota scelta è raffigurato", immagine)
else:
    print("Il valore inserito non è corretto.")