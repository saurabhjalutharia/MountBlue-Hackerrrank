import sys

def findDigits(inputNumbeer):
    # Write your code here
    output = 0
    for i in list(str(inputNumbeer)):
        if int(i) != 0 and inputNumbeer % int(i) == 0:
            output += 1
    return output

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = input().strip()
        result = findDigits(n)
        print(result)