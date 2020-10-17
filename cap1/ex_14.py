#cambio lunghezze

IN_PER_FT=12
CM_PER_IN=2.54

n_feet=int(input("Inserire piedi:"))
n_inches=int(input("Inserire pollici:"))

altezzacm=(n_feet*IN_PER_FT+n_inches)*CM_PER_IN

print("La tua altezza in cm è", altezzacm)


