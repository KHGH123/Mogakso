from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
p=[]
s1 = {}
s2 = {}
for r in range(n+m):
    p.append(input().rstrip())
    
s1 = set(p[0:n])
s2 = set(p[n:])
p = list(s1&s2)
p.sort()
print(len(p), *p, sep='\n')