def divisor_count(num):
    divisors = []
    for x in range(1,int(num**0.5)+1):
        if num % x == 0:
            if x**2 == num or x == 1:
                divisors.append(x)
            else:
                divisors.extend([x,num/x])
    return sum(divisors)
                
def is_amicable(num):
    if num == divisor_count(divisor_count(num)) and num != divisor_count(num):
        return True
    else:
        return False
amNums = []
for x in range(10000):
    if x not in amNums and is_amicable(x):
        amNums.append(x)

print sum(amNums)
