import sys

def luckBalance(k, contests):
    con = contests
    con = sorted(con, reverse=True, key=lambda con: con[con[1] == 0])

    con_1 = [imp[0] for i, imp in enumerate(sorted(con)) if imp[1] == 0]

    con_2 = [imp[0] for j, imp in enumerate(sorted(con[0:k], reverse=True)) if imp[1] == 1]

    con_3 = [imp[0] for l, imp in enumerate(sorted(con[k:], reverse=True)) if imp[1] == 1]

    max_luck = sum(con_1)+sum(con_2)-sum(con_3)

    return max_luck

def luckBalance(n, importContest, inputList):
    output = sum(list(map(lambda x: x[0], filter(lambda x: x[1] == 0, inputList))))
    inputList = sorted(inputList, key=lambda x: (-x[1], -x[0]))
    important = len(list(filter(lambda x: x[1] == 1, inputList)))
    kCounter = 0
    
    for i in range(important):
        #print("output = {} adding {}".format(output, inputList[i][0]))
        if kCounter < importContest:
            output += inputList[i][0]
            kCounter += 1
        else:
            output -= inputList[i][0]
        
    #print(inputList)
    return output

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in range(n):
        contests_t = [int(contests_temp) for contests_temp in input().strip().split(' ')]
        contests.append(contests_t)
    result = luckBalance(n, k, contests)
    print(result)