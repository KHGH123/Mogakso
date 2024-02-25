from queue import PriorityQueue

n, m, x =  map(int, input().split())

e = {i:[] for i in range(1, n+1)}

for i in range(m):
    a, b, c = map(int, input().split())
    e[a].append([b, c])

def func1(a):
    key = {i:float("inf") for i in range(1, n+1)}

    q = PriorityQueue()
    key[a] = 0
    q.put((0, a))
    while q.qsize() != 0:
        c, k = q.get()
        for i in e[k]:
            nc = i[1]+c
            if key[i[0]] > nc: 
                key[i[0]] = nc
                q.put((nc, i[0]))
    return key


answer = 0
ans = func1(x)

for i in range(1, n+1):
    temp = ans[i] + func1(i)[x]
    if answer < temp:
        answer = temp
    
print(answer)
