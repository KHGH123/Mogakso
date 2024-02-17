nn = int(input())
for rr in range(nn):
    n=input()
    ans=0
    t=0
    for r in n:
        if r == "O":
            t+=1
            ans+=t
        else:
            t=0
    print(ans)