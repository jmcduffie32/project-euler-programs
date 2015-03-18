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

def not_sum_of_abundants(num):
    for val in range(num):
        #print val, num-val
        if val in abundants and num - val in abundants:
            return False
    return True

abundants = []
for num in range(28124):
    if is_abundant(num):
        abundants.append(num)

abundants = set(abundants)

sum_of_abundants = []


for num1 in abundants:
    for num2 in abundants:
        new_sum = num1 + num2
        if new_sum > 28124:
            break
        if new_sum not in sum_of_abundants:
            sum_of_abundants.append(new_sum)

print sum_of_abundants
    
