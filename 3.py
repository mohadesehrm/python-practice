count = 0
while True:
    h = input("ساعت ورود دانش آموز را وارد کنید: ")
    if h.lower() == "end":
        break
    else:
        count += 1
print(count)