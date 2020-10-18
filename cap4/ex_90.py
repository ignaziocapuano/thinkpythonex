#twelve days of christmas

from ex_89 import int_to_Ordinale

def creaCanzone(n):
    print("Nel", int_to_Ordinale(n),"Giorno di Natale\nMy true love sent to me:")
    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a-leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a-milking,")
    if n >= 7:
        print("Seven swans a-swimming,")
    if n >= 6:
        print("Six geese a-laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two Turtle Doves")
    if n==1:
        print("A partridge in a pear tree.")
    else:
        print("And a partridge in a pear tee.")
    print()

def main():
    for i in range(1,12+1):
        creaCanzone(i)

main()