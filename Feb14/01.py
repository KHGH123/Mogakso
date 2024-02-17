n=int(input())
answer=0
for i in range(1, n+1):
    s=list(map(int, str(i)))
    if len(s)<=2 : answer+=1
    else:
        a = True
        d = s[1]-s[0]
        for j in range(2, len(s)):
            if s[j]-s[j-1] != d:
                a=False
                break
        if a:
            answer+=1

print(answer)