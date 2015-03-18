def tryOne():
    for a in range(997,333,-1):
        for b in range(333,997):
            for c in range(333,997):
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    print "a =", a, "b =", b, "c ="


def pythagTrip():
    for m in range(1,32):
        for n in range(1,32):
            if m**2 + m*n == 500:
                return m,n

m,n = pythagTrip()
a = m**2 - n**2
b = 2*m*n
c = m**2 + n**2
print a, b, c
