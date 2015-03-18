def fibonacci():
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b
    



fib = fibonacci()
num = 1
i = 1
while len(str(num)) != 1000:
    num = next(fib)
    i += 1
    #print num
print num



