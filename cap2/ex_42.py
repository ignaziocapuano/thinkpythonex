#note musicali 2
freq=float(input("Scrivi una frequenza"))

epsilon=1

if freq>261.63-epsilon and freq<261.63+epsilon:
    nota= "C"
elif freq>293.66-epsilon and freq<293.66+epsilon:
    nota= "D"
elif freq>329.63-epsilon and freq<329.63+epsilon:
    nota= "E"
elif freq>349.23-epsilon and freq<349.23+epsilon:
    nota= "F"
elif freq>392.00-epsilon and freq<392.00+epsilon:
    nota="G"
elif freq>440.00-epsilon and freq<440.00+epsilon:
    nota="A"
elif freq>493.88-epsilon and freq<493.88+epsilon:
    nota="B"
else:
    nota="Non conosciuta"

if nota=="Non conosciuta":
    print("La frequenza digitata non corrisponde ad alcuna nota")
else:
    print("La frequenza corrisponde alla nota", nota)