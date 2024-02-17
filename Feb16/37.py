n, m = map(int, input().split())
s = []
for r in range(n):
    s.append(int(input()))
if m==1:
    print(max(s))
    exit()
a=max(s)*2
b=0
c=0
ans=0
while a!=b:
    ans=0
    if a-b<=1:
        for r in s:
            ans += r//a
        if ans >= m: ans=a
        else: ans=b
        break
    c = round((a+b)/2)
    for r in s:
        ans += r//c
    if ans>=m:
        ans=c
        b=c
    else:
        a=c
print(ans)