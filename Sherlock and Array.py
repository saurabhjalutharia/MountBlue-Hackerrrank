import sys

def solve(inputArray):
    output = 'NO'
    right = sum(inputArray)
    left = 0
    
    for i in inputArray:
        right -= i
        #print("left = {} i = {} right = {}".format(left, i, right))
        if right == left:
            output = 'YES'
            break
        left += i
    return output

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)