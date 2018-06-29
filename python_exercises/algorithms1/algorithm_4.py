num = 600851475143

factors = []
i = 2

while i <= num:
    if num % i == 0:
        factors.append(i)
        num /= i
    i += 1

print(factors)
print(max(factors))