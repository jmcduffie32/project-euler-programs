num = 20
rem = 0

while True:
    num += 20
    d = 1
    rem = 0
    while rem == 0:
        rem = num % d
        #print num, d, rem
        if d == 20:
            print num
            break
        d += 1
    
