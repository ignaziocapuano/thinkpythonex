#triangoli

l1=input("Lunghezza lato :")
l2=input("Lunghezza lato :")
l3=input("Lunghezza lato :")


if l1== l2 and l2 == l3 and l3==l1:
    print("TRIANGOLO EQUILATERO")
elif l1== l2 or l2 == l3 or l3==l1:
    print("TRIANGOLO ISOSCELE")
else:
    print("TRIANGOLO SCALENO")


