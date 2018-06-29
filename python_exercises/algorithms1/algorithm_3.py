numOne = 1
numTwo = 2

numberSwitch = False
sum = 0
arrayOne = [1, 2]

while (numOne < 4000000) and (numTwo < 4000000):
    if not numberSwitch:
        numOne += numTwo
        arrayOne.append(numOne)
        numberSwitch = True
    else:
        numTwo += numOne
        arrayOne.append(numTwo)
        numberSwitch = False

arrayOne.pop()

for fib in arrayOne:
    if fib % 2 == 0:
        sum += fib

print(sum)