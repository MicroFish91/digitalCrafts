# Algorithm 1
for count in range(0, 101):
    if (count % 3 == 0) and (count % 5 == 0):
        print("FizzBuzz")
    elif count % 5 == 0:
        print("Buzz")
    elif count % 3 == 0:
        print("Fizz")
    else:
        print(count)
