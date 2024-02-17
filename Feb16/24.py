from sys import stdin
input = stdin.readline
input()
s = list(map(int, input().split()))
s = set(s)
input()
s2 = list(map(int, input().split()))
for r in s2:
    if r in s: print("1")
    else: print("0")