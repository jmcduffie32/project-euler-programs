def is_prime(n):
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    #print n
    return True




i = 5
n = 11
primes = [2,3,5,7,9]
while len(primes) < 10002:
    if is_prime(n):
        primes.append(n)
    n += 2
    #print primes

print primes[-1]


