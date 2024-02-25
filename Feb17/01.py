a={}
a[0]=[1, 0]
a[1]=[0, 1]
str=[]
nn=int(input())
for i in range(nn):
    n=int(input())
    def func(n):
        if n==0:
            return a[0]
        elif n==1:
            return a[1]
        else:
            if n not in a.keys():
                m1 = func(n-1)
                m2 = func(n-2)
                a[n] = [m1[0]+m2[0], m1[1]+m2[1]]
            return a[n]
    func(n)
    print(*a[n])