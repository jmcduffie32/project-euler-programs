def collatz(num):
    chainNum = 1
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        chainNum += 1
    return chainNum


longestChain = 0
num = 0
for x in range(1,1000000):
    thisChain = collatz(x)
    if thisChain > longestChain:
        longestChain = thisChain
        num = x

print num, longestChain
    
