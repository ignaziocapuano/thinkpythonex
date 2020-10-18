#tariffa taxi

def calcoloCostoTaxi(distanza):
    TARIFFA_BASE=4.00
    SCARTO_METRI=140
    COSTO_SCARTI=0.25
    scartoKm=distanza/SCARTO_METRI
    costoViaggio=TARIFFA_BASE+COSTO_SCARTI*scartoKm
    return costoViaggio

def main():
    kmPercorsi=float(input("Inserire distanza percorsa in taxi in KM:"))
    costoViaggio=calcoloCostoTaxi(kmPercorsi)
    print("Il costo del viaggio è","%.2f" % costoViaggio, "$")

main()