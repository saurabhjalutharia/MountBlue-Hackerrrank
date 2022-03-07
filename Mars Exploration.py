def marsExploration(string):
    # Write your code here
    result = 0
    for i in range(0, len(string), 3):
        if string[i] != 'S':
            result += 1
        if string[i+1] != 'O':
            result += 1
        if string[i+2] != 'S':
            result += 1            
    return result