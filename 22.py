n, m = map(int, input("تعداد سطر و ستون: ").split())
a = []
for i in range(n):
    a.append(list(map(int, input("سطر: ").split())))
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if a[x][y] == 0:
        return
    a[x][y] = 0
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans += 1
            dfs(i, j)
print(ans)