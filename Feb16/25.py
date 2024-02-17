n = int(input())
for i in range(20):
    if n==2**i:
        print(2**i)
        break
    if n<2**i:
        print(2**i - 2*(2**i-n))
        break