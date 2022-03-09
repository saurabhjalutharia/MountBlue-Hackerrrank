_ = input()
calories = list(map(int, input().split()))
calList = sorted(calorie, reverse=True)        #sort the calories in descending order
totaMiles = 0
for index, cupcakeNum in enumerate(calList):
    miles = 2**index*cupcakeNum
    totaMiles += miles
print(totaMiles)