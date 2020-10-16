#Pretend that you have just opened a new savings account that earns 4 percent interest
#per year. The interest that you earn is paid at the end of the year, and is added
#to the balance of the savings account. Write a program that begins by reading the
#amount of money deposited into the account from the user. Then your program should
#compute and display the amount in the savings account after 1, 2, and 3 years. Display
#each amount so that it is rounded to 2 decimal places.

balance=float(input("Inserisci bilancio all'apertura del conto: €"))
tasso=4
#primo anno
balance=balance+tasso/100*balance
print('Dopo un anno avrai: €', balance)
#secondo anno
balance=balance+tasso/100*balance
print('Dopo due anni avrai: €', balance)
#terzo anno
balance=balance+tasso/100*balance
print('Dopo tre anni avrai: €', balance)