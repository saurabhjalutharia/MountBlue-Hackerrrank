import sys

def is_beautiful(number, divisor):
    reverseNumber = int(str(number)[::-1])
    tempRes = abs(number - reverseNumber)%divisor
    if tempRes == 0:
        return True
    else:
        return False

def beautifulDays(dayStart, dayEnd, divisor):
    totalBeautifulDays = 0
    for num in  range(dayStart, dayEnd + 1):
        if is_beautiful(num, divisor):
            totalBeautifulDays += 1
    return totalBeautifulDays

if __name__ == "__main__":
    i, j, k = raw_input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print result