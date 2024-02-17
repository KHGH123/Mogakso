nn = int(input())
d={}
for i in range(nn):
    n = list(input())
    a=0
    for r in n:
        if a<0:
            d[i]="NO"
        elif r=='(':
            a+=1
        elif r==')':
            a-=1
    if a==0:
        d[i] = "YES"
    else:
        d[i] = "NO"

for a in d.values():
    print(a)