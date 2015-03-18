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

def sum_of_abundants(num):
    for val in range(12,num):
        #print val, num-val
        if val in abundants and num - val in abundants:
            return False
    return True

abundants = []
for num in range(28124):
    if is_abundant(num):
        abundants.append(num)

abundants = set(abundants)

total = 0
not_sum_abundants = []
for num in range(28124):
    #print num
    if sum_of_abundants(num):
        
        total += num
        #print num


print total

            
        
    
