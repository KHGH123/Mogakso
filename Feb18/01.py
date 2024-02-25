a = int(input())
b = 1
m=[]
for i in range(a):
    m.append([*map(int, input().split())])

ap=0
bp=0
def func(m):
    global ap, bp
    v = True
    l = len(m)
    k = m[0][0]
    kk = 1-k
    for s in m:
        if kk in set(s):
            v = False
            break
    if v:
        if k == 0:
            ap+=1
            return
        else:
            bp+=1
            return
    else:
        ak=[]
        for r in m[0:l//2]:
            ak.append(r[0:l//2])
        func(ak)

        ak=[]
        for r in m[0:l//2]:
            ak.append(r[l//2:l])
        func(ak)

        ak=[]
        for r in m[l//2:l]:
            ak.append(r[0:l//2])
        func(ak)

        ak=[]
        for r in m[l//2:l]:
            ak.append(r[l//2:l])
        func(ak)

func(m)
print(ap, bp, sep='\n')