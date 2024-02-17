import sys
input = sys.stdin.readline

n=int(input())
str=[]
for i in range(n):
    nn=input()
    if 'push' in nn:
        nn=nn.split()
        str.append((int)(nn[1]))
    elif 'pop' in nn:
        if len(str)==0:print(-1)
        else:print(str.pop())
    elif 'size' in nn:
        print(len(str))
    elif 'empty' in nn:
        if len(str):print(0)
        else: print(1)
    elif 'top' in nn:
        if len(str)==0:print(-1)
        else:print(str[-1])
