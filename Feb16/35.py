from sys import stdin
input = stdin.readline
a={}

input()
n = list(map(int, input().split()))
n1 = n[:]
n=list(set(n))
n.sort()

for i in range(len(n)):
    if i==0: a[n[i]] = 0
    else: a[n[i]] = i

print(a)
for r in n1:
    print(a[r], end=' ')