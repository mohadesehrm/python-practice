x = list(map(int,input("enter: ").split()))
big = max(x)
while big in x:
    x.remove(big)
print(x[len(x)-1: ])
