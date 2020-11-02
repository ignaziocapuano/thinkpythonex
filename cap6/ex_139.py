#Morse code

dictionary={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..",\
            "M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",\
            "0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"---."}

string=input("Inserisci stringa da convertire in sequenza numerica per tastierino telefonico:")
string=string.upper()
num_string=""
for i in range(len(string)):
    for key in dictionary:
        if string[i]==key:
            num_string+=dictionary[key]+" "
print(num_string)