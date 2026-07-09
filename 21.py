n, m = map(int, input("تعداد سطر و ستون رو وارد کنید: ").split())
jadval = []
for i in range(n):
    satr = []
    for j in range(m):
        satr.append(0)
    jadval.append(satr)
k = int(input("تعداد بمب ها: "))
for i in range(k):
    r, c = map(int, input("مختصات بمب: ").split())
    jadval[r][c] = "*"
for i in range(n):
    for j in range(m):
        if jadval[i][j] == "*":
            continue
        count = 0
        if i-1 >= 0:
            if jadval[i-1][j] == "*":
                count += 1
        if i+1 < n:
            if jadval[i+1][j] == "*":
                count += 1
        if j-1 >= 0:
            if jadval[i][j-1] == "*":
                count += 1
        if j+1 < m:
            if jadval[i][j+1] == "*":
                count += 1
        if i-1 >= 0 and j-1 >= 0:
            if jadval[i-1][j-1] == "*":
                count += 1
        if i-1 >= 0 and j+1 < m:
            if jadval[i-1][j+1] == "*":
                count += 1
        if i+1 < n and j-1 >= 0:
            if jadval[i+1][j-1] == "*":
                count += 1
        if i+1 < n and j+1 < m:
            if jadval[i+1][j+1] == "*":
                count += 1
        jadval[i][j] = count
for i in range(n):
    for j in range(m):
        print(jadval[i][j], end=" ")
    print()