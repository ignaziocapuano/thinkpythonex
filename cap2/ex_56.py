#Frequenza e onde

frequenza=float(input("Inserisci frequenza della radiazione in GigaHz (Hz*10^9): "))

frequenza*=10**9

if frequenza < 3*(10**9):
    categoriaOnde= "Onde Radio"
elif 3*(10**9) <= frequenza < 3*(10**12):
    categoriaOnde= "Microonde"
elif 3*(10**12) <= frequenza < 4.3*(10**14):
    categoriaOnde= "Infrarossi"
elif 4.3*(10**14) <= frequenza < 7.5*(10**14):
    categoriaOnde= "Luce Visibile"
elif 7.5*(10**14) <= frequenza < 3*(10**17):
    categoriaOnde= "Ultravioletto"
elif 3*(10**17) <= frequenza < 3*(10**19):
    categoriaOnde= "Raggi X"
elif frequenza>=3*(10**19):
    categoriaOnde= "Raggi gamma"

print("L'onda di frequenza", frequenza,"Hz appartiene a:", categoriaOnde)