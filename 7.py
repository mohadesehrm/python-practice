x = ""
sen = input("enter: ")
for i in sen:
    if i == "=":
        x = x[ : -1]
    else:
        x = x + i
print(x)