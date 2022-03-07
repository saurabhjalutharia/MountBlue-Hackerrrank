import sys

def libraryfine(returnDay, returnMonth, returnYear, dueDay, dueMonth, dueYear):
    
    totalFine = 0
    if returnYear > dueYear:
        totalFine = 10000
    elif returnMonth > dueMonth and returnYear == dueYear:
        totalFine = 500 * (returnMonth - dueMonth)
    elif returnDay > dueDay and returnMonth == dueMonth and returnYear == dueYear:
        totalFine = 15 * (returnDay - dueDay)
        
    return totalFine

if __name__ == "__main__":
    returnDay, returnMonth, returnYear = input().strip().split(' ')
    returnDay, returnMonth, returnYear = [int(returnDay), int(returnMonth), int(returnYear)]
    dueDay, dueMonth, dueYear = input().strip().split(' ')
    dueDay, dueMonth, dueYear = [int(dueDay), int(dueMonth), int(dueYear)]
    result = libraryFine(returnDay, returnMonth, returnYear, dueDay, dueMonth, dueYear)
    print(result)