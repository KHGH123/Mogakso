import sys
input = sys.stdin.readline

n = int(input())
str = []
for i in range(n):
    str.append(int(input()))
    
str.sort()
for s in str:
    print(s)