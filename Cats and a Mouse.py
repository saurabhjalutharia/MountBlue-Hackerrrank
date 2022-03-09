def catAndMouse(catA, catB, mouseC):
    distanceFromCatA = abs(catA - mouseC)
    distanceFromCatB = abs(catB - mouseC)
    if distanceFromCatA > distanceFromCatB:
        print('Cat B')
    elif distanceFromCatA == distanceFromCatB:
        print('Mouse C')
    else:
        print('Cat A')


n = int(input())
for i in range(n):
    catA, catB, mouseC = map(int, input().split())
    catAndMouse(catA, catB, mouseC)