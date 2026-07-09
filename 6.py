students1 = list(input("enter: ").split())
students2 = []
for i in students1:
    if students1.count(i) == 1:
        students2.append(i)
print(students2)