import sys

def camelcase(inputString):
    finalResult = 1
    if not inputString:
        finalResult = 0
    for letter in inputString:
        if letter.isupper():
            finalResult += 1
    return finalResult

if __name__ == "__main__":
    inputString = input().strip()
    result = camelcase(inputString)
    print(result)