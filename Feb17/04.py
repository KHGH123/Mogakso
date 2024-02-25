from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
name = {}
id = {}

for i in range(1, n+1):
    nn = input().rstrip('\n')
    name[i] = nn
    id[nn] = i

for i in range(m):
    nn = input().rstrip('\n')
    if nn.isdecimal():
        nn = int(nn)
        print(name[nn])
    else:
        print(id[nn])