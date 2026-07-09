va = list(map(str , input("وضعیت حضور و غیاب را وارد کنید: ").split()))
cntp = 0
cnta= 0
for i in va:
    if i == "present":
        cntp +=1
    elif i == "absent":
        cnta +=1
print(f"present: {cntp}\n absent: {cnta}")