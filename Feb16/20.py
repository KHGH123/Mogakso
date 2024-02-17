a, b = map(int, input().split())
n = list(map(int, input().split()))

for r in n:
    if r < b: print(r, end=' ')
