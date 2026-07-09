check = []
while True:
    sd = input("ساعات را وارد کنید: ").strip()
    if sd == "done":
        break
    start, end = map(int, sd.split())
    check.append([start, end])
check.sort()
f = False
for i in range(len(check) - 1):
    if check[i][1] > check[i + 1][0]:
        f = True
        break
if f:
    print("Conflict")
else:
    print("No Conflict")