
_ = input()
arr = sorted(map(int, input().split()))
diff = 2*10**9
for i in range(1, len(arr)):
    diff = min(diff, arr[i] - arr[i-1])
print(diff)