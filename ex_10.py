#Create a program that reads two integers, a and b, from the user. Your program should
#compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#• The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log10 a
#• The result of a^b

import math

print('Inserisci due numeri interi:')
a=int(input())
b=int(input())

print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)
print(a,'mod',b,'=',a%b)
print('log10',a,'=',math.log10(a))
print(a,'^',b,'=',a^b)