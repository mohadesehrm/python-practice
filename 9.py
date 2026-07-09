hh = int(input("enter: "))
mm = int(input("enter: "))
k = int(input("enter: "))
min1 = mm + (hh*60)
min2 = min1 + k
h2 = min2//60 % 24
m2 = min2%60
print(h2 , m2)
