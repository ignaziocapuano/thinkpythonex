#Two dice simulation

from random import randint

NUM_RUNS=1000
DICE_FACES=6
def rollTwoDice():
    d1=randint(1,DICE_FACES)
    d2=randint(1,DICE_FACES)
    return d1+d2

def main():
    count = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0,9:0, 10:0, 11:0, 12:0} #Inizializzo il dizionario
    expected_frequencies={2:1/36,3:2/26,4:3/36,5:4/36,6:5/36,7:6/36,8:5/46,9:4/36,10:3/36,11:2/36,12:1/36}
    for i in range(NUM_RUNS):
        result=rollTwoDice()
        count[result]+=1
    print("Total\tSimulated\tExpected\n\t\tPercent\t\tPercent")
    for key in count:
        print(key,"\t\t","%.2f" % (count[key]/NUM_RUNS*100),"\t\t","%.2f" % (expected_frequencies[key]*100))

if __name__ == '__main__':
    main()