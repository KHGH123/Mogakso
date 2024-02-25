from sys import stdin

input = stdin.readline

n=int(input())

s=set()
for r in range(n):
    ii = input().split() 

    if 'add' in ii:
        s.add(int(ii[1]))
    elif 'check' in ii:
        if int(ii[1]) in s: print(1)
        else: print(0)
    elif 'remove' in ii:
        if int(ii[1]) in s: s.remove(int(ii[1]))
    elif 'toggle' in ii:
        if int(ii[1]) in s: s.remove(int(ii[1]))
        else: s.add(int(ii[1]))
    elif 'all' in ii:
        s = set((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    elif 'empty' in ii:
        s = set()
    print(s)