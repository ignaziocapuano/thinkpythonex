#ZODIACO CINESE

anno=int(input("Inserisci un anno: "))

#2000/12=166+8

if anno%12==8:
    segno="Dragone"
elif anno%12==9:
    segno="Serpente"
elif anno%12==10:
    segno="Cavallo"
elif anno%12==11:
    segno="Pecora"
elif anno%12==0:
    segno="Scimmia"
elif anno%12==1:
    segno="Gallo"
elif anno%12==2:
    segno="Cane"
elif anno%12==3:
    segno="Maiale"
elif anno%12==4:
    segno="Ratto"
elif anno%12==5:
    segno="Bue"
elif anno%12==6:
    segno="Tigre"
elif anno%12==7:
    segno="Lepre"

print("Anno cinese="+segno)