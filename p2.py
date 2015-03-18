def fibonacci():
    a, b = 0, 1
    while True:
        if a > 4000000:
            return
        yield a
        a, b = b, a+b

total = 0
for x in fibonacci():
    if x % 2 == 0:
        total += x

print total
    
        

