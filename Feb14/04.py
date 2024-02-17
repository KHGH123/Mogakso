n=int(input())
s=list(map(int, input().split()))

s.sort()
answer=0
ans=0
for r in s:
    temp=answer
    answer=r+temp
    ans+=answer
print(ans)