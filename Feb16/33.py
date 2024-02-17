ans=1
a,b = map(int, input().split())
for r in range(0, b):
    ans*=(a-r)/(b-r)
print(round(ans))