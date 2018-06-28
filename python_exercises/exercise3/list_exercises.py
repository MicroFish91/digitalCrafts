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

# Matrix Addition I
list11 = [1, 3]
list12 = [2, 4]
matrixOne = []

list21 = [-5, 8]
list22 = [10, -15]
matrixTwo = []

newMatrix = []

# Holds [[1, 3], [2, 4]]
matrixOne.append(list11)
matrixOne.append(list12)

# Holds [[-5, 8], [10, -15]]
matrixTwo.append(list21)
matrixTwo.append(list22)

matrixHolder = []

for indexOne in range(0, 2, 1):
    for indexTwo in range(0, 2, 1):
        matrixHolder.append(matrixOne[indexOne][indexTwo] + matrixTwo[indexOne][indexTwo])

    newMatrix.append(matrixHolder)
    matrixHolder = []


print("2-D Matrix Addition: ")
print(newMatrix)


# Matrix Addition II
def matrixAddition(matrixOne, matrixTwo, dimension):

    matrixHolder = []
    newMatrix = []    
    
    for indexOne in range(0, dimension, 1):
        for indexTwo in range(0, dimension, 1):
            matrixHolder.append(matrixOne[indexOne][indexTwo] + matrixTwo[indexOne][indexTwo])

        newMatrix.append(matrixHolder)
        matrixHolder = []

    print(newMatrix)

matrixAddition(matrixOne, matrixTwo, 2)


# De-dup
print("De-dup: ")

originalArray = ["A", "B", "C", "B", "D", "A", 1, "HEY", "HAY", "G", "B", "H", "D"]
newArray = []

for index in originalArray:
    if index not in newArray:
        newArray.append(index)

print(newArray)