def func(ss, n):
    if (not n%400) or (n%100 and not n%4):
        ss[2]=29
    else:
        ss[2]=28
    return ss

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

ss = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if s1[0]+1000<s2[0] or (s1[0]+1000==s2[0] and s1[1]<s2[1]) or (s1[0]+1000==s2[0] and s1[1]==s2[1] and s1[2]<=s2[2]):
    print("gg")
    exit()

elif s1[0] == s2[0] and s1[1] == s2[1]:
    answer = s2[2] - s1[2]

elif s1[0] == s2[0]:
    answer=0
    ss = func(ss, s1[0])
    answer+=ss[s1[1]]-s1[2]+s2[2]
    for i in range(s1[1]+1, s2[1]):
        answer+=ss[i]
    
else:
    answer = 0
    for i in range(s1[0]+1, s2[0]):
        ss = func(ss, i)
        if ss[2] == 29:
            answer += 366
        else:
            answer += 365

    ss = func(ss, s2[0])
    for i in range(1, s2[1]):
        answer+=ss[i]

    ss = func(ss, s1[0])
    for i in range(s1[1]+1, 13):
        answer+=ss[i]
    answer+=ss[s1[1]]-s1[2]+s2[2]

print("D-",answer,sep='')




    
