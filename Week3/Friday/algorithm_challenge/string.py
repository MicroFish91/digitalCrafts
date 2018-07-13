str1 = input("String 1? ")
str2 = input("String 2? ")

str3 = ""

if len(str2) > len(str1):
    str3 = str1
    str1 = str2
    str2 = str3

for letter in str1:
    if letter not in str2:
        print("This is the letter: " + letter)

