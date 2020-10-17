#ordinamento 3 interi

n1=int(input("Numero 1:"))
n2=int(input("Numero 2:"))
n3=int(input("Numero 3:"))

min=min(n1,n2,n3)
max=max(n1,n2,n3)

middle=n1+n2+n3-min-max

print("Ordinati:",min, middle, max)