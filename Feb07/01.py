def solution():
    str = set()
    n = (int)(input())

    for i in range(n):
        str.add(input())
    
    str = list(str)
    idx = sorted(str, key=lambda x : (len(x), x))

    for r in idx:
        print(r)

solution()