s=input().upper()

cnt=-1
ans='a'
for i in range(65, 91):
    if s.count(chr(i)) > cnt:
        cnt = s.count(chr(i))
        ans = chr(i)
    elif s.count(chr(i)) == cnt:
        ans = '?'

print(ans)