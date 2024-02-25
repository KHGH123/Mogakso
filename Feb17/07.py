from sys import stdin
input = stdin.readline
import heapq
n = int(input())

a=[]
for r in range(n):
    k = int(input())
    if k==0:
        if not len(a):print(0)
        else:
            print(heapq.heappop(a))
    else:
        heapq.heappush(a, k)