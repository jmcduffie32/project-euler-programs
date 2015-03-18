sumOfSquares = 0
squareOfSums = 0
for x in range (1,101):
    sumOfSquares += x*x
    squareOfSums += x
print sumOfSquares, squareOfSums*squareOfSums
print squareOfSums**2 - sumOfSquares
    
