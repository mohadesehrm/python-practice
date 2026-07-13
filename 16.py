x = list(map(int,input("enter: ").split()))
maxx = max(x)
x.remove(maxx)
print(max(x))
