while True:
    a = input()
    b = True
    if a == "0": break
    for i in range(len(a)//2):
        if a[i] != a[-1*(i+1)]:
            b = False
            break
    if b: print("yes")
    else: print("no")