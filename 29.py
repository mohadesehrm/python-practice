lst = []
while True:
    x = input("دستور مورد نظر:")
    if x == "done":
        break
    y = x.split()
    if y[0] == "add":
        lst.append(y[1])
    elif y[0] == "remove":
        if len(lst) > 0:
            lst.pop(0)
for i in lst:
    print(i, end=" ")