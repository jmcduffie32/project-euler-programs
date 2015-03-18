def digitsProduct(n):
    product = 1
    for digit in n:
        product *= int(digit)
    return product

number = open('p8.txt').read()
i = 0
largest = 0
while i < 1000-12:
    #print number[i:i+13]
    if '0' in number[i:i+13]:
        i += 1
    else:
        currentProduct = digitsProduct(number[i:i+13])
        #print largest, currentProduct
        if currentProduct > largest:
            largest, digits = currentProduct, number[i:i+13]
        i += 1


print digits, largest
        
        

