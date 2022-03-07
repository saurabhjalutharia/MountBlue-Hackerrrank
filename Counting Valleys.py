def countingValleys(steps, path):
    # Write your code here
    seaLevel = 0
    valley = 0
    for i in range(steps):
        if path[i] == 'U':
            seaLevel += 1
        elif path[i] == 'D':
            seaLevel -= 1
            if seaLevel == -1:
                valley += 1
    return valley