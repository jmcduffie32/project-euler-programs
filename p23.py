def divisor_count(num):
    divisors = []
    for x in range(1,int(num**0.5)+1):
        if num % x == 0:
            if x**2 == num or x == 1:
                divisors.append(x)
            else:
                divisors.extend([x,num/x])
    return sum(divisors)
def is_abundant(num):
    if divisor_count(num) > num:
        return True
    else:
        return False
def additives(num):
    numsToAdd = []
    abundant = []
    for i in range(num):
        if is_abundant(num-i):
            abundant = True
            return 1, abundant
        else:
            numsToAdd.append(i)
    return numsToAdd, abundant

total = 0
for num in range(28124):
    numsToAdd, abundant = additives(num)
    if not abundant:
        numTotal = sum(numsToAdd)
        total += numTotal
    
