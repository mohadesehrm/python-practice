students1 = list(input("enter: ").split())
students2 = []
for i in students1:
    if i not in students2:
        students2.append(i)
        count = students1.count(i)
        print(f'{i} : {count}')
students1 = list(input("enter: ").split())
for i in students1:
    count = students1.count(i)
    print(f'{i} : {count}')
    students1.remove(i)