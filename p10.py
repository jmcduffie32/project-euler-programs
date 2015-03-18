def is_prime(n):
    if n == 3: return True
    if n == 5: return True
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

total = 2
for x in range(3,2000000,2):
    if is_prime(x):
        #print x
        total += x

print total
