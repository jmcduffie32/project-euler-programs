def tri_num(num):
    if num % 2 == 0:
        return (num + 1)* num/2
    else:
        return (num + 1) * (num/2) + num/2 + 1

i = 2
while True:
    triNum = tri_num(i)
    divisors = 0
    for x in range(1,int(triNum**0.5)+1):
        if triNum % x == 0:
            if x**2 == triNum:
                divisors += 1
            else:
                divisors += 2
    print divisors, triNum        
    if divisors >= 500:
        print True, triNum
        break
    i += 1
    
