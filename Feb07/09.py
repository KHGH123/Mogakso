n=int(input())
str=[]
for i in range(n):
    str.append(input().split())

str = sorted(str, key = lambda x: int(x[0]))
for r in str:
    print(r[0], r[1])