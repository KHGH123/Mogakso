a, b=map(int, input().split())
m=0

for r in range(1, min(a,b)+1):
    if a%r==0 and b%r==0:
        m=r
n=max(a,b)
i=1
while (n*i)%min(a,b)!=0:
    i+=1
print(m)
print(n*i)