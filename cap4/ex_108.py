#riduci unità di misura
"""
Crea una funzione che esprime un unità di volume imperiale (cup, tablespoon, teaspoon)
usando la più larga unità possibile. Ad esempio, in una ricetta, se sono consigliati 4 tablespoon
per una persona ma si sta cucinando per 4 persone saranno necessari 16 tablespoon=
a quel punto è meglio definire 16 tablespoon come 1 cup. Creiamo una funizone per quello.
"""
def maxImperialUnit(qt, measureUnit):
    # 1 cup=16 tablespoons
    # 1 tablespoons= 3 teaspoons
    measureUnit=measureUnit.lower() #rendo minuscolo il testo del secondo parametro per poter fare il controllo di validità
    if (measureUnit!="cup" and measureUnit!="tablespoons" and measureUnit!="teaspoons"):
        print("unità di misura non valida!")
        quit()
    if measureUnit=="teaspoons":
        cups=qt//48
        qt=qt%48
        tablespoons=qt//3
        qt=qt%3
        teaspoons=qt
        return (cups,"cup",tablespoons,"tablespoons",teaspoons, "teaspoons")
    if measureUnit=="tablespoons":
        cups=qt//16
        qt=qt%16
        tablespoons=qt
        return (cups,"cup",tablespoons,"tablespoons")
    if measureUnit=="cup":
        cups=qt
        return (cups,"cup")

def main():
    qt=int(input("Inserisci quantità per ricetta: "))
    unity=input("Inserisci unità di misura (cup, tablespoons, teaspoons): ")
    print(maxImperialUnit(qt, unity))

if __name__ == '__main__':
    main()


