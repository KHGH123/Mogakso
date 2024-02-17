input()
n = list(map(int, input().split()))
ans=0
for r in n:
    if r==1:
        continue
    a=True
    for i in range(2, r):
        if r%i==0:
            a=False
            break
    if a: ans+=1

print(ans)