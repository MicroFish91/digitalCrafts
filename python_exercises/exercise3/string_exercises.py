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

#Long-long vowels
userInputThree = input("What phrase would you like to have long vowels? ")

vowels = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")
vowelCheck = False

outputThree = ""
    
for character in userInputThree:
    for vowel in vowels:
        if character == vowel:
            outputThree = outputThree + (vowel * 5)
            vowelCheck = True

    if vowelCheck == False:
        outputThree += character

    vowelCheck = False    
    
print(outputThree)

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

            # if index < 0:
            #     index = 26 + index

    if userChar != " ":  
        rot13 += alphabet[index]
    else:
        rot13 += " "

print(rot13)