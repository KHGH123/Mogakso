n = int(input())
answer = 9999
for i in range(n//5+1):
    for j in range(n//3+1):
        if i*5+j*3 == n and i+j<answer:
            answer = i+j

if answer == 9999 : print(-1)
else: print(answer)
