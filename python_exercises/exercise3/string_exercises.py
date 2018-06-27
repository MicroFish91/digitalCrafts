import math

# Takes a string from the user
userInput = input("Please enter a string: ")

# Uppercase the string
print(userInput.upper())

# Capitalize the string
print(userInput.capitalize())

# Reverse the string
reverseText = ""
for character in range((len(userInput) - 1), -1, -1):
    reverseText += userInput[character]

print(reverseText)

# Leetspeak
userInputTwo = input("Please enter text to be converted into Leetspeak: ")
leetSpeak = ""

for character in userInputTwo:

    if character == "A":
        character = "4"
    elif character == "E":
        character = "3"
    elif character == "G":
        character = "6"
    elif (character == "I") or (character == "L"):
        character = "1"
    elif character == "O":
        character = "0"
    elif character == "S":
        character = "5"
    elif character == "T":
        character = "7"

    leetSpeak += character

print(leetSpeak)

# #Long-long vowels
# userInputThree = input("Please enter text to be converted into long-long vowels: ")

# totalVowels = 0
# index = 0
# count = 0
# changeLetter = ""

# while index <= (len(userInputThree) - 1):
    
#     startIndex = index
#     count = 0
#     changeLetter = ""

#     while userInputThree[index] == "A":
#         changeLetter = "A"
#         index += 1
#         count += 1

#     if changeLetter:
#         userInputThree = userInputThree[0:startIndex] + changeLetter * 5 +  userInputThree[index:len(userInputThree)]

#         index -= 1

#     print(index)

#     index += 1

# print (userInputThree)
        

#ROT13
userInputFour = input("What phrase would you like to convert to ROT13? ")

alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

rot13 = ""
index = 0

for userChar in userInputFour:
    for alphaChar in alphabet:
        if userChar == alphaChar:
            index = alphabet.index(alphaChar)
            index -= 13

            if index > 25:
                index = abs(25 - index)

    if userChar != " ":  
        print(index)  
        rot13 += alphabet[index]
    else:
        rot13 += " "

print(rot13)