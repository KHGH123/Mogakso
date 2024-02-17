from sys import stdin
input = stdin.readline

a={}
input()
n1 = list(map(int, input().split()))

for i in range(len(n1)):
    if n1[-1] in a.keys():
        a[n1.pop()]+=1
    else:
        a[n1.pop()]=1


input()
n2 = list(map(int, input().split()))

for r in n2:
    if a.get(r)==None:print(0, end=' ')
    else: print(a[r], end= ' ')