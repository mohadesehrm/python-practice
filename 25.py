shop = {}
while True:
    x = input("وارد کنید: ")
    if x == "total":
        break
    y = x.split()
    if y[0] == "add":
        shop[y[1]] = int(y[2])
    elif y[0] == "remove":
        if y[1] in shop:
            del shop[y[1]]
total = 0
for i in shop:
    print(i, ":", shop[i])
    total += shop[i]

print("Total =", total)