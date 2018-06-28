# 1 to 10
print("1 to 10: ")
for num in range(1, 11, 1):
    print(num)

# n to m
print("n to m: ")
n = input("Start number? ")
m = input("End number? ")

for num in range(int(n), int(m) + 1, 1):
    print(num)

# Odd Numbers
print("Odd Numbers: ")
for num in range(1, 11, 1):
    if num % 2 == 1:
        print(num)

# Print a Square
print("Print a Square: ")
stars = "***** "

for dim1 in range(0, 5, 1):
    print (stars * 5)


# Print a Square II
print("Print a Square II: ")
dimensions = int(input("Please enter dimension of your square: "))

for dim1 in range(0, dimensions, 1):
    print(stars * dimensions)

# Print a Box
print("Print a Box: ")

# Print a Triangle
print("Print a Triangle: ")
star = "*"

for height in range(1, 8, 2):
    print((star * height).center(7, " "))


# Print a Triangle II
print("Print a Triangle II: ")
height = int(input("How high would you like your triangle? "))
index = 1

for construct in range(0, height, 1):
    total = construct + index
    index += 1
    print((star * total).center((2 * height) - 1, " "))


# Multiplication Table
print("Multiplication Table: ")

for num1 in range(1, 11):
    for num2 in range(1, 11):
        product = num1 * num2
        print(str(num1) + " X " + str(num2) + " = " + str(product))

