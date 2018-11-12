rMo = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
lMo = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def daysInMonth(month, isLeapYear = False):
    if isLeapYear:
        return lMo[month]
    return rMo[month]


def calcMonthDiff(yr, mo, dy):
    lstMo = []
    if isLeapYear(yr):
        for i in range(1,mo):
            lstMo.append(lMo[i]) #append day values corresponding to each month of the leap year
        lstMo.append(dy) #append day value for the month
    else:
        for i in range(1,mo):
            lstMo.append(rMo[i])
        lstMo.append(dy)
    return lstMo


def datediff(year1, month1, day1, year2, month2, day2):
    assert year1 <= year2, "Place later date as the latter date arguments"
    yrs = [] #years from [year1, year2)
    daysInYrs = {} #days in each of [year1, year2)
    for i in range(year1, year2):
        yrs.append(i)
    for j in yrs:
        if isLeapYear(j):
            daysInYrs[j] = 366
        else:
            daysInYrs[j] = 365
#if months are same, just take years in days and add difference in days
    if month1 == month2:
        daysBetweenYears = sum(daysInYrs.values())
        diffindates = daysBetweenYears + (day2 - day1)
        #print(diffindates)
        return diffindates
# if months are different, it gets a bit more complicated
    month2Lst = calcMonthDiff(year2, month2, day2)
    month1Lst = calcMonthDiff(year1, month1, day1)
    diffmo = sum(month2Lst) - sum(month1Lst)
    diffindates = sum(daysInYrs.values()) + diffmo
    #print(diffindates)
    return diffindates


a = datediff(2000, 1, 30, 2010, 1, 20)
b = datediff(2000, 1, 20, 2010, 1, 30)
c = datediff(1990, 5, 20, 2010, 1, 30)
d = datediff(1990, 2, 20, 2018, 4, 29)

print(a)
print(b)
print(c)
print(d)