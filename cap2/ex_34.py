#anni del cane

n=int(input("Inserisci età cane in anni umani:"))

if n<3:
    n=n*10.5
else:
    n=10.5*2+(n-2)*4

print("Il tuo cane ha", n, "anni canini!")