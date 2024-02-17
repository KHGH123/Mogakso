n=int(input())
str=[]
for i in range(n):
    str.append(list(map(int, input().split())))

str = sorted(str, key = lambda x: (x[0], x[1]))
for r in str:
    print(r[0], r[1])