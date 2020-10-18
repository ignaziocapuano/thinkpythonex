#calcolo costo spedizione

def calcoloCostoSpedizione(qt_elementi):
    COSTO_PRIMOELEMENTO=10.95
    COSTO_ELEMENTIAGGIUNTIVI=2.95
    qt_elementi-=1 #NON CONTO IL PRIMO ELEMENTO
    costoTot=COSTO_PRIMOELEMENTO+qt_elementi*COSTO_ELEMENTIAGGIUNTIVI
    return costoTot

def main():
    qt=int(input("Inserisci quantitativo elementi comprati:"))
    costoSpedizione=calcoloCostoSpedizione(qt)
    print("Il prezzo di spedizione è $:","%.2f" % costoSpedizione)

main()