n = int(input())    
for r in range(n):
    a = list(map(int, input().split()))
    f = a[2]%a[0]
    l = a[2]//a[0]+1
    if f==0: 
        f=a[0]
        l-=1
    if l<10: l="0"+str(l)
    print(str(f),str(l), sep='')