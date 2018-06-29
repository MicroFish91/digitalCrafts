# hello
def hello(name):
    print("Hello " + name)
hello("Matt")

# y = x + 1
import matplotlib.pyplot as plot

def f(x): 
     return x + 1

xs = list(range(-3, 4)) 
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()

# Square of x
def g(x):
    return x * x

xs = list(range(-100, 101))
ys = []

for x in xs:
    ys.append(g(x))

plot.plot(xs, ys)
plot.show()

# Odd or Even
def h(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

xs = list(range(-5, 6))
ys = []

for x in xs:
    ys.append(h(x))

plot.bar(xs, ys)
plot.show()

# Sine
import math

def i(x):
    return math.sin(x)

xs = list(range(-5, 6))
ys = []

for x in xs:
    ys.append(i(x))

plot.plot(xs, ys)
plot.show()

# Sine 2
from numpy import arange
def i(x):
    return math.sin(x)

xs = arange(-5, 6, 0.1)
ys = []

for x in xs:
    ys.append(i(x))

plot.plot(xs, ys)
plot.show()

# Degree Conversion
def j(x):
    return x * 1.8 + 32


xs = arange(-50, 150, 1)
ys = []

for x in xs:
    ys.append(j(x))

plot.plot(xs, ys)
plot.show()

# Play again & play again again
def playAgain():
    play = input("Do you want to play again ('Y' or 'N')? ")
    invalid = True

    while invalid:
        if play == "Y":
            return True
            invalid = False
        elif play == "N":
            return False
            invalid = False
        else:
            play = input("Invalid input. Do you want to play again ('Y' or 'N')? ")
