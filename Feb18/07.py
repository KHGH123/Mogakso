from sys import stdin
input = stdin.readline

n, m = (map(int, input().split()))
k = [*map(int, input().split())]
ans=[0]*(n+1)
for i in range(0, n):
    ans[i+1]+=ans[i]+k[i]
for r in range(m):
    a, b = (map(int, input().split()))
    print(ans[b]-ans[a-1])