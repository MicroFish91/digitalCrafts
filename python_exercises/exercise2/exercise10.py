userResponse = "yes"
coins = 0

while userResponse == "yes":
    print("You have " + str(coins) + " coin(s).")
    userResponse = input("Do you want another? ")
    coins += 1

print ("Bye")

