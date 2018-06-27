import math

# Sum the numbers
myArray = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]
myArrayTwo = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]
outputArray = []
sum = 0

for numbers in myArray:
    sum += numbers

print("Sum of numbers: ")
print (sum)

# Largest Number
print("Largest number: ")
print(max(myArray))

# Smallest Number
print("Smallest number: ")
print(min(myArray))

# Even Numbers
print("Even Numbers: ")

for numbers in myArray:
    if numbers % 2 == 0:
        print(numbers)

# Positive Numbers
for numbers in myArray:
    outputArray.append(abs(numbers))

print("Converted to positive numbers: ")
print(outputArray)

# Positive Numbers 2
outputArray = []

for numbers in myArray:
    if numbers > 0:
        outputArray.append(numbers)

print("Transferred only positive numbers: ")
print(outputArray)

# Multiply a List
factor = 6
outputArray = []

print("Multiply a list: ")
print(myArray)
print("multiplication factor - " + str(factor))

for numbers in myArray:
    outputArray.append(numbers * factor)

print(outputArray)


# Multiply Vectors
outputArray = []

for index in range(0, len(myArray), 1):
    outputArray.append(myArray[index] * myArrayTwo[index])

print("Multiplying vectors: ")
print(outputArray)

# Matrix Addition
list11 = [1, 3]
list12 = [2, 4]


