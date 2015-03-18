firstSundays = 0
year = 1901

def addDays(year, month,i):
    
    if year % 4 == 1 and year != 1901 and (i == 0 or i == 1) :
        month += 2
    elif year % 4 == 0 and i not in [0,1]:
        month += 2
    else:
        month += 1
    
    if month > 7:
        month -= 7
    return month

months = [2,5,5,1,3,6,1,4,7,2,5,7]



while year < 2001:
    for i in range(len(months)):
        months[i] = addDays(year,months[i],i)
        
    firstSundays += sum([month for month in months if month == 1])
    year += 1
print firstSundays
