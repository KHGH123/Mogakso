n = int(input())
d = {}
answer = 0
for i in range(n):
    str = input()
    answer+=1
    for i in range(len(str)):
        if(i==0 or d.get(str[i]) == None or str[i-1] == str[i]):
            d[str[i]] = True
        else:
            answer -= 1
            break
    d = {}
    
print(answer)