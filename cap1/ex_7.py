#Write a program that reads a positive integer, n, from the user and then displays the
#sum of all of the integers from 1 to n

n=int(input('Inserisci un numero intero:'))
somma=int((n*(n+1))/2)
print('La somma dei numeri da 1 a', n, 'è:', somma)