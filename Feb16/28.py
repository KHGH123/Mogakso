from itertools import permutations
a = float("inf")
n, m = map(int, input().split())
s = list(map(int, input().split()))

for r in permutations(s, 3):
    if m-sum(r) == 0:
        ans = sum(r)
        break
    elif 0 < m-sum(r) < a :
        a = m-sum(r)
        ans = sum(r)

print(ans)