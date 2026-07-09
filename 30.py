best = ""
weak = ""
best_avg = -1
weak_avg = 100
sum_all = 0
count = 0
fail = 0
while True:
    x = input("اطلاعات کلاس را وارد کنید: ")
    if x == "done":
        break
    lst = x.split()
    sum1 = 0
    for i in range(1, len(lst)):
        num = int(lst[i])
        sum1 += num
        sum_all += num
        count += 1
        if num < 10:
            fail += 1
    avg = sum1 / (len(lst) - 1)
    if avg > best_avg:
        best_avg = avg
        best = lst[0]
    if avg < weak_avg:
        weak_avg = avg
        weak = lst[0]
print("Best class:", best)
print("Weakest class:", weak)
print("Average:", sum_all / count)
print("Failed students:", fail)