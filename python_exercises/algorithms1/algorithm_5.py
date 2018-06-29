primes = []
num = 2

while len(primes) < 10001:
    factor = 2
    while factor < num:
        if num % factor == 0:
            break
        factor += 1
    if factor == num:
        primes.append(num)
    num += 1

print(primes[len(primes) - 1])