def pallindromic():
    pall = []
    a, b = 999, 999
    product = a * b
    while b > 99:
        while a > 99:
            if str(product) == str(product)[::-1]:
                pall.append(product)
            a -= 1
            product = a * b
            #print a , b , product
        a = 999
        b -= 1
    print max(pall)
    
        
