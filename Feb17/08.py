from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
a=deque()
b=1
for r in range(n):
    a.append([*map(int, input().split())])
a=deque(sorted(a, key=lambda x : (x[1], x[0])))
k = a.popleft()
while len(a)>0:
    while len(a)!=0:
        if a[0][0] < k[1] : 
            a.popleft()
        else:
            k=a.popleft()
            b+=1
            break
    
print(b)