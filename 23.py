a = list(map(int, input("اعداد: ").split()))
x = a[0]
maxx = a[0]
for i in a[1:]:
    x = max(i, x + i)
    maxx = max(maxx, x)
print(x)