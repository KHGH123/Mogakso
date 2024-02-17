from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
q = deque()
for r in range(n):
    s = list(input().split())
    if 'push' in s:
        q.append(int(s[1]))
    elif 'pop' in s:
        if not len(q): print(-1)
        else: print(q.popleft())
    elif 'size' in s:
        print(len(q))
    elif 'empty' in s:
        if len(q)==0: print(1)
        else: print(0)
    elif 'front' in s:
        if not len(q): print(-1)
        else: print(q[0])
    else:
        if not len(q): print(-1)
        else :print(q[-1])
