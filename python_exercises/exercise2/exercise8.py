bill = float(input("Total bill amount? "))
service = input("Level of service? ")
people = int(input("Split how many ways? "))
tip = 0

if service == "good":
    tip = bill * 0.2
elif service == "fair":
    tip = bill * 0.15
elif service == "bad":
    tip = bill * 0.1
else:
    tip = 0

total = bill + tip
totalEach = total / people

print("Tip amount: $" + str("{0:.2f}".format(tip)) + " Total amount: $" + str("{0:.2f}".format(total)) + " Amount per person: $" + str("{0:.2f}".format(totalEach)))